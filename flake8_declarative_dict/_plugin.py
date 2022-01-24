from flake8_plugin_utils import Plugin as BasePlugin

from .visitor import Visitor
from .config import Config

class Plugin(BasePlugin):
    name = 'flake8-declarative-dict'
    version = "0.1.0"
    visitors = [Visitor]

    @classmethod
    def add_options(cls, option_manager):
        option_manager.add_option(
            '--allow-nested-empty-dicts',
            type='choice',
            default=True,
            parse_from_config=True,
            help='Allow large dicts only with when it nests empty dicts')
        
        option_manager.add_option(
            '--dict-size-limit',
            type='int',
            default=0,
            parse_from_config=True,
            help='Maximum allowed size of a regular dict')
        
        option_manager.add_option(
            '--args-size-limit',
            type='int',
            default=1,
            parse_from_config=True,
            help='Maximum allowed args to be passed to a function')
        
        option_manager.add_option(
            '--list-size-limit',
            type='int',
            default=1,
            parse_from_config=True,
            help='Maximum allowed size of a regular list')
        
        option_manager.add_option(
            '--allow-nested-empty-lists',
            type='choice',
            default=True,
            parse_from_config=True,
            help='Allow large lists only with when it nests empty lists')
        

    @classmethod
    def parse_options_to_config(cls, option_manager, options, args):
        return Config(
            dict_size_limit=options.dict_size_limit,
            allow_nested_empty_dicts=options.allow_nested_empty_dicts,
            args_size_limit=options.args_size_limit,
            list_size_limit=options.list_size_limit,
            allow_nested_empty_lists=options.allow_nested_empty_lists
        )