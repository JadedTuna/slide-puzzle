import sys
def reload_lib():
    for name in ("button", "namespace", "puzzlescene", "settings", "tile"):
        reload("lib." + name)

reload_lib()

from lib.puzzlescene import PuzzleScene

puzzle = PuzzleScene()
puzzle.run()
