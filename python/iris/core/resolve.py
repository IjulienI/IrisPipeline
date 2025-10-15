import re
from pathlib import Path
from iris import conf


#path = "PipelinePath/assets/character/hero"
#pattern = "{root}/assets/(?P<asset_type>.*)/(?P<asset_name>.*)"

def resolve(entity_type : str, path : Path) -> dict[str, str]:

    pattern = conf.template.get(entity_type).get("regex")
    path = path.as_posix()
    re_pattern = re.compile(pattern)
    match = re_pattern.search(str(path))
    result = {}

    if match:
        result = match.groupdict()

    return result

if __name__ == "__main__":

    entity_type = "asset_type"
    path = Path("C:/Users/julien.soum/Documents/PipelinePath/assets/character/hero")

    result = resolve(entity_type , path)
    print(result)