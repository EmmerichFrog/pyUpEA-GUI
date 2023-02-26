from cx_Freeze import setup, Executable
import sys
import os

sys.path.append(os.path.relpath("./pyUpEA"))


setup(
    name = "GUI to pyUpEA",
    version = "0.1",
    executables = [Executable("pyUpEA-GUI.py")],
   )
