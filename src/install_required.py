import subprocess as sp
import os, venv
try:
    from pip import main as pipmain
except ImportError:
    from pip._internal import main as pipmain

current_dir_path = os.path.dirname(os.path.realpath(__file__))

def initiate_virtualenv():
    dir_path = os.path.join(current_dir_path, 'kodi_env')
    # sp.run(['python', '-m', 'venv', os.path.join(dir_path, 'kodi_env')])
    venv.create(dir_path, with_pip=True)
    if os.path.exists(os.path.join(dir_path, 'Scripts')): # TODO: Check for windows
        sp.run([os.path.join(dir_path, 'Scripts', 'activate')])
    else: # For UNIX environments
        sp.run([os.path.join(dir_path, 'bin', 'activate')])

def update_requirements():
    with open(os.path.join(current_dir_path, 'requirements.txt'), 'r') as f:
        requirements = [l.strip() for l in f.readlines()]
        print(requirements)
        # for requirement in requirements:
        #     pipmain(['install', requirement])
        pipmain(['install', requirements[0]])