from pathlib import Path
from pprint import pprint

from iris import conf
from iris.core import resolve
from iris.core.dt.entity import Entity
from iris.libs import utils


def find(search_type : str, filters : dict[str, str] = None) -> list[Entity]:

    """
    For a given type and filter, return a list of Entity instances.

    Args:
        search_type: search type
        filters: dict of filters

    Returns:
        list of Entity instances

    """

    glob_expression = conf.template.get(search_type).get("glob")
    keys = utils.get_pattern_keys(glob_expression)
    formatter = {key: "*" for key in keys}
    if filters:
        formatter.update(filters)

    glob_expression = glob_expression.format(**formatter)

    found = Path(conf.root).glob(glob_expression)
    result : list[Entity] = []
    for path in found:
        temp_dict = resolve(search_type, path)

        if temp_dict:
            result.append(Entity(search_type, temp_dict))

    return result


if __name__ == "__main__":
    print("Main test starting...")
    print("Main test starting...")

    search_input = "asset_type"
    pprint(find(search_input))
    