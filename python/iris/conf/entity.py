# config
root = "C:/Users/julien.soum/Documents/PipelinePath"

template = {
    "asset_type" : { "glob" : "assets/{asset_type}", "regex" : "assets/(?P<asset_type>.*)"},
    "asset_name" : { "glob" : "assets/{asset_type}/{asset_name}", "regex" : "assets/(?P<asset_type>.*)/(?P<asset_name>.*)"}
}