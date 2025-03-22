import pillow_heif
from PIL import Image
import os

input_folder = "./images"
output_folder = "./images"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    if file.lower().endswith(".heic"):
        heic_path = os.path.join(input_folder, file)

        try:
            heif_file = pillow_heif.open_heif(heic_path)

            jpg_path = os.path.join(output_folder, file.replace(".heic", ".jpg"))
            heif_file.to_pillow().convert("RGB").save(jpg_path, "JPEG")
            print(f"Converted {file} -> {jpg_path}")

        except Exception as e:
            print(f"Error converting {file}: {e}")
