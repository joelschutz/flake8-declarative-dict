import ast
from typing import Tuple
from flake8_plugin_utils import Error
from .error import DCD001, DCD002, DCD003


def _get_large_dict(node: ast.Dict, dict_size_limit: int, allow_nested_empty_dicts: bool) -> Tuple[Error, int]:
    '''Detects if the dict is larger that an allowed value'''

    # If a negative value is provided no check will be done
    if dict_size_limit < 0:
        return None, None
    
    dict_size = len(node.keys)
    if dict_size > dict_size_limit:

        values_are_empty_dicts = []

        for i in node.values:
            if isinstance(i, ast.Dict) and not i.values:
                values_are_empty_dicts.append(True)
                
            else:
                values_are_empty_dicts.append(False)

        if (not allow_nested_empty_dicts) or (not all(values_are_empty_dicts)):
            return DCD001, dict_size
    
    return None, None

def _get_to_many_args(node: ast.Call, args_size_limit: int) -> Tuple[Error, int]:
    '''Detects if to many arguments are being passed to a function call'''
    
    # If a negative value or one is provided no check will be done
    if args_size_limit < 1:
        return None, None
    
    starred_args = []
    for i in node.args:
        if isinstance(i, ast.Starred): starred_args.append(i)
    
    args_size = len(node.keywords) + len(node.args)
    if any(
        (
            len(starred_args) > 1,
            args_size > args_size_limit and len(node.args) > len(starred_args),
            args_size - len(starred_args) > args_size_limit,
        )
    ):
        return DCD002, args_size
    
    return None, None

def _get_large_list(node: ast.List, list_size_limit: int, allow_nested_empty_lists: bool) -> Tuple[Error, int]:
    '''Detects if the list is larger that an allowed value'''

    # If a negative value is provided no check will be done
    if list_size_limit < 0:
        return None, None
    
    list_size = len(node.elts)
    if list_size > list_size_limit:

        values_are_empty_lists = []

        for i in node.elts:
            if isinstance(i, ast.List) and not i.elts:
                values_are_empty_lists.append(True)
                
            else:
                values_are_empty_lists.append(False)

        if (not allow_nested_empty_lists) or (not all(values_are_empty_lists)):
            return DCD003, list_size
    
    return None, None
