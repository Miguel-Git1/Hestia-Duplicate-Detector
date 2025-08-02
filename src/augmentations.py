from typing import List, Dict
import numpy as np
import math
import logging
import albumentations as A

logger_aug = logging.getLogger(__name__)

def get_cropping_dims(image: np.ndarray, scale_factor: float) -> List[int]: 
    scaled_width: int = math.floor(image.shape[1] * scale_factor)
    scaled_height: int = math.floor(image.shape[0] * scale_factor)
    logger_aug.debug(f"Scaled factor: {scaled_width}x{scaled_height}")
    return scaled_width, scaled_height

def augment_image(raw_image: np.ndarray, scale_factor: float = 0.5) -> np.ndarray:
    '''
        Pass the image through the augmentation pipeline and return it

        Args:
            image (ndarray): The image represented in a numpy array.
    '''
    try:
        if not (0 < scale_factor <= 1):
            raise ValueError(f"Scaling factor is {scale_factor} which is not acceptable. \
                            The value must be between 0 and 1.")

        crop_width, crop_height = get_cropping_dims(raw_image, scale_factor)


        pipeline = A.Compose([
            A.CenterCrop(crop_height, crop_width, p=1),
        ])

        transformed_data: Dict = pipeline(image=raw_image)
        transformed_image: np.ndarray = transformed_data['image']
        return transformed_image
    except Exception as e:
        logger_aug.error(f"Exception on augment_image: {e}")