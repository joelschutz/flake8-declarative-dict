import ast
from flake8_plugin_utils import Visitor
from ._checker import _get_large_dict, _get_to_many_args, _get_large_list

class Visitor(Visitor):
    def visit_Dict(self, node: ast.Dict) -> None:
        error, size = _get_large_dict(node, self.config.dict_size_limit, self.config.allow_nested_empty_dicts)
        if error:
            self.error_from_node(
                error=error,
                node=node,
                size=size,
                max_size=self.config.dict_size_limit
            )
        self.generic_visit(node)
    
    def visit_Call(self, node: ast.Call) -> None:
        error, size = _get_to_many_args(node, self.config.args_size_limit)
        if error:
            self.error_from_node(
                error=error,
                node=node,
                size=size,
                max_size=self.config.args_size_limit
            )
        self.generic_visit(node)
        
    
    def visit_List(self, node: ast.List) -> None:
        error, size = _get_large_list(node, self.config.list_size_limit, self.config.allow_nested_empty_lists)
        if error:
            self.error_from_node(
                error=error,
                node=node,
                size=size,
                max_size=self.config.list_size_limit
            )
        self.generic_visit(node)
