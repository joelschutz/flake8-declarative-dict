"""Tests for DCD002 case in `flake8_declarative_dict` package."""
# Core Library
from flake8_plugin_utils import assert_error, assert_not_error

# First party
from flake8_declarative_dict.visitor import Visitor
from flake8_declarative_dict.error import DCD002


def test_valid_call(default_config):
    case = 'f(a)'
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_invalid_call(default_config):
    case = 'f(a, b)'
    assert_error(
        Visitor,
        case,
        DCD002,
        default_config,
        size=2,
        max_size=default_config.args_size_limit
    )

def test_valid_nested_call(default_config):
    case = 'f(a=ff(b))'
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_invalid_nested_call(default_config):
    case = 'f(a=ff(b, c))'
    assert_error(
        Visitor,
        case,
        DCD002,
        default_config,
        size=2,
        max_size=default_config.args_size_limit
    )

def test_valid_call_unpack_1(default_config):
    case = '''
f(**a)
    '''
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_valid_call_unpack_2(default_config):
    case = '''
f(*b, **a)
    '''
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_invalid_call_unpack_1(default_config):
    case = '''
f(a, **b)
    '''
    assert_error(
        Visitor,
        case,
        DCD002,
        default_config,
        size=2,
        max_size=default_config.args_size_limit
    )

def test_invalid_call_unpack_2(default_config):
    case = '''
f(a, *b)
    '''
    assert_error(
        Visitor,
        case,
        DCD002,
        default_config,
        size=2,
        max_size=default_config.args_size_limit
    )

def test_invalid_call_unpack_3(default_config):
    case = '''
f(a, *b, **c)
    '''
    assert_error(
        Visitor,
        case,
        DCD002,
        default_config,
        size=3,
        max_size=default_config.args_size_limit
    )

def test_invalid_call_unpack_4(default_config):
    case = '''
f(*a, *b)
    '''
    assert_error(
        Visitor,
        case,
        DCD002,
        default_config,
        size=2,
        max_size=default_config.args_size_limit
    )

def test_invalid_call_unpack_5(default_config):
    case = '''
f(**a, **b)
    '''
    assert_error(
        Visitor,
        case,
        DCD002,
        default_config,
        size=2,
        max_size=default_config.args_size_limit
    )
