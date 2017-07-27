import os

import sys
from cx_Freeze import setup, Executable

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"    # Tells the build script to hide the console.
print(base)
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ['BDD', 'Interface/FenetresEnPython'], includes = ["BDD"] ,include_files = [
"fichier_conf.yaml","fichier_fenetre_personnalisable.yaml", "Images/", "PDF/", "fichier_stats.yaml",
    os.path.join(sys.base_prefix, 'DLLs', 'sqlite3.dll')], excludes = [])



executables = [
    Executable('Accueil.py', icon = "Images\SIMM2.0.ico", base=base)
]

setup(name='SIMM',
      version = '2.0',
      description = "Logiciel d'inventorisation pour les equipements medicaux",
      options = dict(build_exe = buildOptions),
      executables = executables)
