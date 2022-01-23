# Core Library
from pytest import fixture
from flake8_plugin_utils import assert_error, assert_not_error

# First party
from flake8_declarative_dict.config import Config
from flake8_declarative_dict.visitor import Visitor


@fixture(scope='session')
def default_config():
    return Config(
        dict_size_limit=0,
        allow_nested_empty_dicts=True,
        args_size_limit=1,
        list_size_limit=1,
        allow_nested_empty_lists=True
    )

def test_trivial_case(default_config):
    case = ''
    assert_not_error(
        Visitor,
        case,
        default_config
    )
