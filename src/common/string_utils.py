import json
from typing import Union


def ellipsis(string: Union[str, dict, list], num: int) -> str:
    if isinstance(string, (dict, list)):
        string = json.dumps(string, default=str)
    if len(string) <= num:
        return string
    return f"{string[:num]}..."
