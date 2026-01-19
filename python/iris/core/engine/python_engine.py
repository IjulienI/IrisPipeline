import os
from pathlib import Path
import platform
from iris.core.engine.abstract_engine import AbstractEngine


class PythonEngine(AbstractEngine):

    def open(self, path: Path) -> None:

        """
        Opens the given file
        Args:
            path:

        Returns:

        """

        if platform.system() == "Windows":
            os.startfile(str(path))


    def explore(self, path: Path) -> None:

        """
        Opens the folder containing the given file


        Args:
            path:

        Returns:

        """


        if platform.system() == "Windows":
            os.startfile(str(path.parent))

if __name__ == "__main__":

    engine = PythonEngine()
    engine.explore(Path(__file__))
    engine.open(Path(__file__))