import sys

# Plugins can obviously import from ufotest itself
from ufotest.hooks import Action, Filter

# Since the whole plugin system uses a lot of python dynamic import magic, importing from other modules
# within the same plugin IS POSSIBLE but should be done as a relative import like this:
from .util import print_hello_world


@Action('pre_command', 10)
def hello_world():
    print_hello_world()
    sys.exit(0)


@Filter('get_version', 10)
def modify_version(value: str):
    return '1.3.3.7'

