from pathlib import Path
from iris.core.engine.python_engine import PythonEngine
import maya.cmds as cmds

class MayaEngine(PythonEngine):

    def open(self, path: Path) -> None:
        cmds.file(path, open = True, force = True)


if __name__ == "__main__":

    engine = MayaEngine()
    exemple = Path("C:/Users/julien.soum/Documents/maya/projects/Test.mb")
    engine.open(exemple)