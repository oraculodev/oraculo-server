def check_argument_is_not_none(param, param_name):
    if param is None:
        raise ValueError(f"Parameter '{param_name}' is missing.")


def check_argument_is_not_none_or_empty(param, param_name):
    if param is None or param == "":
        raise ValueError(f"Parameter '{param_name}' is missing.")
