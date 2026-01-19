# -*- coding: utf-8 -*-

name = "iris"

version = "0.0.1"

requires = [
    "qtpy",
]

description = "https://github.com/IjulienI/IrisPipeline"

author = ["SOUM Julien"]

def commands():
    env.PYTHONPATH.append('{root}/python')