# Basic installation:
```sh
pip install git+https://github.com/jakkdl/flake8-trio-anthropic.git
```

should now show up in
```
flake8 --version
```

although quite possible that it's gonna complain about versions.

# Usage
TRIO001: trio.move_on_after with no await: complains if you open a move_on_after block but there's no `await` statement within it.

Currently WIP, and will not see awaits that are not at the top level of the With block.
