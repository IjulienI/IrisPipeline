import re

#path = "PipelinePath/assets/character/hero"
#pattern = "{root}/assets/(?P<asset_type>.*)/(?P<asset_name>.*)"

def resolve(path, pattern):

    r = re.compile(pattern)

    found = [match.groupdict() for match in r.finditer(path)]
    if found:
        return found[0]
    else:
        return None