from pathlib import Path

class AbstractEngine(object):
    def open(self, path : Path) -> None:
        pass

    def explore(self, path : Path) -> None:
        pass

