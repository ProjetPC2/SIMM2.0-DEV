from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ['BDD', 'Interface/FenetresEnPython'], includes = ["BDD"] ,include_files = [
"fichier_stats.yaml","fichier_conf.yaml","fichier_pieces.yaml", "fichier_fenetre_personnalisable.yaml", "Images/", "PDF/"], excludes = [])

import sys
base = 'None' if sys.platform=='win32' else None

executables = [
    Executable('Accueil.py', icon = "Images\SIMM2.0.ico")
]

setup(name='SIMM',
      version = '2.0',
      description = "Logiciel d'inventorisation pour les equipements medicaux",
      options = dict(build_exe = buildOptions),
      executables = executables)
