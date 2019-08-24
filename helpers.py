from pathlib import Path

def path_file(file):
    path = Path
    complete_path = path.cwd() / file
    return complete_path
    