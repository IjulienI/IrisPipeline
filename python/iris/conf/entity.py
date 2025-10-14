import pathlib

root = "C:/Users/julien.soum/Documents/PipelinePath"
target = "assets/character/publish/geo"

template = {
    "asset_type" : "...",
    "asset_name" : "...",
    "asset_department" : "...",
    "asset_task" : "..."
}

found = pathlib.Path(root).glob(target)

for f in found:
    print(f)