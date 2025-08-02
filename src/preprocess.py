from pathlib import Path
from typing import List, Generator, Optional
import random
import logging
import shutil

logger_org = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class SiameseOrganizer():
    def __init__(self,
                 base_path: Path,
                 data_folder: Path):
        self.base_path: Path = base_path
        self._data_folder: Path = data_folder
        self._siamese_folder: Path = base_path.joinpath("siamese")


    def create_siamese_folder(self) -> None:
        '''
            Creates a folder tree for pre-process data for a siamese network.
            
            Args:
                base_path (Path): Path for storing all the siamese base path and subfolders
        '''
        self._siamese_folder.mkdir(parents=True, exist_ok=True)

    def _get_all_house_ids(self) -> List[int]:
        house_ids: List[int] = []
        for house in self._data_folder.iterdir():
            house_id = house.stem.split("_")[0]
            logger_org.info(f"Getting house id {house_id}")

            if not house_id:
                logger_org.warning(f"Could not get house id nº {house_id}. Skipping...")
                continue

            house_ids.append(int(house_id))
        return sorted(house_ids)

    def _find_houses_by_id(self, id: int) -> Generator[Path, None, None]:
        for house_file in self._data_folder.iterdir():
            house_file_id = house_file.stem.split("_")[0]
            if house_file.is_file() and id == int(house_file_id):
                yield house_file

    def _store_apns(self, house_ids: List[int]):
        """ last_id: Optional[int] = None """
        for id in house_ids:
            current_house_folder = self._siamese_folder.joinpath(f"{id}_house")

            """             if last_id is not None and last_id > id:
                logger_org.debug("True")
                negatives = list(self._find_houses_by_id(random.randint(last_id, 535)))
                if negatives:  
                    shutil.copy(random.choice(negatives), current_house_folder) """

            house_gen = self._find_houses_by_id(id)

            """ last_id = id """
            for house in house_gen:
                shutil.copy(house, current_house_folder)



    def _create_house_folders(self):
        house_ids: List[int] = sorted(self._get_all_house_ids())
        for id in house_ids:
            logger_org.info(f"Created folder with house id {id}")

            house_folder = self._siamese_folder.joinpath(str(id) + "_house")
            house_folder.mkdir(exist_ok=True)
    
        self._store_apns(house_ids)

    def organize_siamese_data(self) -> None:
        '''
            Organizes within the siamese network context, by anchors, positives and negatives.
        '''
        try:
            if not self._data_folder.is_dir():
                raise ValueError("Data folder is not a folder.")
     
            self._create_house_folders()

        except Exception as e:
            logger_org.error(f"Exception raised at organize_siamese_data: {e}")
            return None
        



            

            

        
        