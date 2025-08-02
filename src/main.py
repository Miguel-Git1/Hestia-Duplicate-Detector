from pathlib import Path
from typing import List, LiteralString
from preprocess import SiameseOrganizer

CWD = Path.cwd()

if __name__ == "__main__":
    organizer = SiameseOrganizer(CWD, Path("data/Houses-dataset/Houses Dataset"))

    organizer.create_siamese_folder()
    organizer.organize_siamese_data()