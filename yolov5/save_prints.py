import cv2
import os

def save_image_with_incremental_filename(save_dir, image):
    """
    Save an image with an incremental filename in a specified directory.
    If a file with the same name exists, it will increment the filename.

    Args:
        save_dir (str): Directory where the image will be saved.
        image (numpy.ndarray): The image (numpy array) to save.
    """
    # Create the save directory if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    # Determine the filename
    base_filename = "image"
    index = 1
    while True:
        filename = os.path.join(save_dir, f"{base_filename}{index}.jpg")
        if not os.path.exists(filename):
            cv2.imwrite(filename, image)
            break
        index += 1

# Example usage:
# Assuming you have an image you want to save
# image_to_save = ...
# save_image_with_incremental_filename("output_images", image_to_save)
