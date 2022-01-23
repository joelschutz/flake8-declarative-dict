# Core Library
from flake8_plugin_utils import assert_not_error

# First party
from flake8_declarative_dict.visitor import Visitor


def test_trivial_case(default_config):
    case = ''
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_set_case(default_config):
    case = 'a = {1,2,3,4}'
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_tuple_case(default_config):
    case = 'a = (1,2,3,4)'
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_list_compreenssion_case(default_config):
    case = 'a = [i for i in x]'
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_tuple_compreenssion_case(default_config):
    case = 'a = (i for i in x)'
    assert_not_error(
        Visitor,
        case,
        default_config
    )

def test_dict_compreenssion_case(default_config):
    case = 'a = {k:v for k, v in x.items()}'
    assert_not_error(
        Visitor,
        case,
        default_config
    )
