from flake8_plugin_utils import Error


class DCD001(Error):
    code = 'DCD001'
    message = 'Dict too large {size}>{max_size}.'


class DCD002(Error):
    code = 'DCD002'
    message = 'Too many args passed in call {size}>{max_size}.'


class DCD003(Error):
    code = 'DCD003'
    message = 'List too large {size}>{max_size}.'
