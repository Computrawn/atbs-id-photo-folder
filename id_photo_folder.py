#! python3
# id_photo_folder.py — An exercise in using Pillow to manipulate images.
# For more information, see projet_details.txt.

# Import modules and write comments to describe this program.
import os
import logging
from PIL import Image

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.DEBUG)  # Note out to enable logging.


for foldername, subfolders, filenames in os.walk("/Users/josh/Media"):
    num_photo_files = 0
    num_nonphoto_files = 0
    file_total = num_nonphoto_files + num_photo_files
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not filename.endswith((".png", ".PNG", ".jpg", ".JPG")):
            num_nonphoto_files += 1
            continue  # skip to next filename
        # Open image file using Pillow.
        path_name = os.path.join(foldername, filename)
        img = Image.open(path_name)
        img_width, img_height = img.size
        # Check if width & height are larger than 500.
        if img_width >= 500 or img_height >= 500:
            # Image is large enough to be considered a photo.
            num_photo_files += 1
        else:
            # Image is too small to be a photo.
            num_nonphoto_files += 1

        # # If more than half of files were photos,
        # # print the absolute path of the folder.

    if num_photo_files != 0:
        if num_photo_files >= file_total / 2:
            logging.info(foldername)
