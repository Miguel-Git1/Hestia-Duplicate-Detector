from pathlib import Path
from typing import List, LiteralString

CWD = Path.cwd()

def create_siamese_folders(base_path: Path):
    '''
        Creates a folder tree for pre-process data for a siamese network. \
        
        Args:
            base_path (Path): Path for storing all the siamese base path and subfolders
    '''

    siamese_folder = base_path.joinpath("siamese")
    siamese_folder.mkdir(parents=True, exist_ok=True)

    subfolders: List[LiteralString] = ["anchors", "positive", "negative"]

    for subfolder in subfolders:
        siamese_folder.joinpath(subfolder).mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    create_siamese_folders(CWD)