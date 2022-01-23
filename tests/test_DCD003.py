"""Tests for DCD003 case in `flake8_declarative_dict` package."""
# Core Library
from flake8_plugin_utils import assert_error, assert_not_error

# First party
from flake8_declarative_dict.visitor import Visitor
from flake8_declarative_dict.error import DCD003


def test_valid_list_1(default_config):
    case = 'a = []'
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_valid_list_2(default_config):
    case = 'a = [my_object]'
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_invalid_list(default_config):
    case = 'a = [1, 2]'
    assert_error(
        Visitor,
        case,
        DCD003,
        default_config,
        size=2,
        max_size=default_config.list_size_limit
    )

def test_valid_nested_list(default_config):
    case = 'a = [[], [], []]'
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_invalid_nested_list(default_config):
    case = 'b = [1, 2, []]'
    assert_error(
        Visitor,
        case,
        DCD003,
        default_config,
        size=3,
        max_size=default_config.list_size_limit
    )

def test_valid_list_assign_1(default_config):
    case = '''
a = []
a.append(1)
    '''
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_valid_list_assign_2(default_config):
    case = '''
a = [[], [], []]
a[0],append(1)
    '''
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_invalid_list_assign(default_config):
    case = '''
a = [1, 2]
a[0] = 2
    '''
    assert_error(
        Visitor,
        case,
        DCD003,
        default_config,
        size=2,
        max_size=default_config.list_size_limit
    )

def test_valid_list_in_function(default_config):
    case = 'f(a=[[],[],[]])'
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_invalid_list_in_function(default_config):
    case = 'f(a=[1,2,3])'
    assert_error(
        Visitor,
        case,
        DCD003,
        default_config,
        size=3,
        max_size=default_config.list_size_limit
    )
