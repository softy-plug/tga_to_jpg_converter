import os
from PIL import Image

# Prompt user for folders
tga_folder = input('Enter the folder with tga images: ')
jpg_folder = input('Enter folder to save converted jpg images: ')

# Check if folders exists, else create them
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# Loop through all files in the tga folder
for file_name in os.listdir(tga_folder):
    if file_name.endswith('.tga'):
        # Open tga image and convert to RGB
        tga_image = Image.open(os.path.join(tga_folder, file_name))
        tga_image = tga_image.convert('RGB')

        # Create new jpg file name
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(jpg_folder, jpg_file_name)

        # Save jpg image with maximum quality
        jpg_image = tga_image.save(jpg_file_path, 'JPEG', quality=100)

print('All tga images in {} converted to jpg and saved in {}.'.format(tga_folder, jpg_folder))

#softy_plug
