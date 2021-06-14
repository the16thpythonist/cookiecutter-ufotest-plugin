from ufotest.hooks import Action, Filter
from ufotest.util import cprint


@Action()
def hello_world():
    cprint('hello_world')


@Filter()
def modify_version(value: str):
    return '1.3.3.7'

