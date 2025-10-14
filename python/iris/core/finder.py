import pathlib
from iris import conf
from libs.utils import get_pattern_keys


def find(search_type, filters = None):
    glob_expression = conf.template.get(search_type).get("glob")
    print(glob_expression)

    keys = get_pattern_keys(glob_expression)
    print(keys)
    default_filters = {key: "*" for key in keys}
    if filters:
        default_filters.update(filters)
    print(default_filters)

    glob_expression = glob_expression.format(**default_filters)
    print(glob_expression)

    found = pathlib.Path(conf.root).glob(glob_expression)
    print(f"search type: {search_type}")
    return list(found)


if __name__ == "__main__":
    print("Main test starting...")

    search_input = "asset_name"
    print(find(search_input, filters = {"asset_type" : "character"}))
    print(find(search_input, filters={"asset_type": "prop"}))
