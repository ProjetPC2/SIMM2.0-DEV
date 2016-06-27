from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ["C:\\Users\\Alexandre MAO\\Documents\\GitHub\\SIMM2.0-DEV\\BDD", "Images"],include_files = ["DataBase_Equipement.json",
"fichier_stats.yaml","fichier_conf.yaml","DataBase_BDT.json"], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('AccueilUI.py', base=base, targetName = 'SIMM.exe')
]

setup(name='test',
      version = '1.0',
      description = 'test de deploiement',
      options = dict(build_exe = buildOptions),
      executables = executables)
