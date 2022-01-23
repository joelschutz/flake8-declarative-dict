"""Tests for DCD001 case in `flake8_declarative_dict` package."""
# Core Library
from flake8_plugin_utils import assert_error, assert_not_error

# First party
from flake8_declarative_dict.visitor import Visitor
from flake8_declarative_dict.error import DCD001


def test_valid_dict(default_config):
    case = 'a = {}'
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_invalid_dict(default_config):
    case = 'a = {"a":1}'
    assert_error(
        Visitor,
        case,
        DCD001,
        default_config,
        size=1,
        max_size=default_config.dict_size_limit
    )

def test_valid_nested_dict(default_config):
    case = 'a = {"a":{}, "b":{}}'
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_invalid_nested_dict(default_config):
    case = 'b = {"a":1, "b":{}}'
    assert_error(
        Visitor,
        case,
        DCD001,
        default_config,
        size=2,
        max_size=default_config.dict_size_limit
    )

def test_valid_dict_assign_1(default_config):
    case = '''
a = {}
a['a'] = 1
    '''
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_valid_dict_assign_2(default_config):
    case = '''
a = {'a': {}, 'b': {}}
a['a']['a'] = 1
    '''
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_invalid_dict_assign(default_config):
    case = '''
a = {'a': 1}
a['a'] = 2
    '''
    assert_error(
        Visitor,
        case,
        DCD001,
        default_config,
        size=1,
        max_size=default_config.dict_size_limit
    )

def test_valid_dict_in_function(default_config):
    case = 'f(a={"a":{}})'
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_invalid_dict_in_function(default_config):
    case = 'f(a={"a":1})'
    assert_error(
        Visitor,
        case,
        DCD001,
        default_config,
        size=1,
        max_size=default_config.dict_size_limit
    )
