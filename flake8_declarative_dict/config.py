class Config:
    def __init__(
        self,
        dict_size_limit,
        allow_nested_empty_dicts,
        args_size_limit, list_size_limit,
        allow_nested_empty_lists
    ) -> None:
        self.dict_size_limit = dict_size_limit
        self.allow_nested_empty_dicts = allow_nested_empty_dicts
        self.args_size_limit = args_size_limit
        self.list_size_limit = list_size_limit
        self.allow_nested_empty_lists = allow_nested_empty_lists
