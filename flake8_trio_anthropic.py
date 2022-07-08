"""Checks for bad Trie code"""
import ast
import importlib.metadata
from typing import Type, Any, Generator

ERROR_STRING = "TRIO001: trio.move_on_after with no await"


class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.problems: list[tuple[int, int]] = []

    def check_move_on_after_no_await(self, node: ast.With):
        for withitem in node.items:
            if not isinstance(withitem.context_expr, ast.Call):
                continue
            if not isinstance(withitem.context_expr.func, ast.Attribute):
                continue
            if withitem.context_expr.func.attr == "move_on_after":
                break
        else:
            return
        # We can either recursively parse the AST looking for an Await
        for expr in node.body:
            if isinstance(expr, ast.Expr):
                if isinstance(expr.value, ast.Await):
                    break
        else:
            self.problems.append((node.lineno, node.col_offset))

        # or assume there's no Await, and in a visit_Await, pop all with's from the
        # problem list that are parents to it. (although I suppose we then have the
        # same problem in reverse, although parsing upwards is easier than the
        # other way around

    def visit_With(self, node: ast.With) -> None:  # pylint: disable=invalid-name
        self.check_move_on_after_no_await(node)
        self.generic_visit(node)


class Plugin:  # pylint: disable=too-few-public-methods
    name = __name__
    version = importlib.metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor()
        visitor.visit(self._tree)
        for line, col in visitor.problems:
            yield line, col, ERROR_STRING, type(self)
