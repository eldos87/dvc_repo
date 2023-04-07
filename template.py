import os

dirs = [
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "models",
    "notebook",
    "src"
]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py"),
    os.path.join("src","utils.py"),
    os.path.join("src","get_data.py"),
    os.path.join("src","train.py")
]

for file_ in files:
    with open(file_,"w") as f:
        pass
