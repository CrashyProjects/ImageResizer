import os
import sys
import imghdr

from PIL import Image
import config

directory = config.directory
saveCopy = config.saveCopy
resizeRes = config.resizeRes
destination = config.destination

def is_image(filename):
    image_types = {'jpg', 'jpeg', 'png', 'bmp', 'gif'}
    file_type = imghdr.what(filename)
    if file_type in image_types:
        return True
    else:
        return False

# Set the directory path
if len(sys.argv) > 1:
    directory = sys.argv[1]
print("----------------------------------")
print("Using directory: " + directory)
print("----------------------------------")
if not os.path.isdir(directory):
    print("!Directory not found")
    sys.exit(1)

#Set destination path
if destination == "":
    print("Destination set to: " + directory)
    destination = directory
else:
    if not os.path.isdir(destination):
        print("!Destination path not found, creating it")
        os.mkdir(destination)

# Get a list of all images in the directory
files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file)) and is_image(os.path.join(directory, file))]
    
# Conversion
for file in files:
    image = Image.open(os.path.join(directory, file))
    if(saveCopy): #Do not overwrite
        file = "RESIZED_" + file
    name = os.path.join(destination, file)
    if image.size == resizeRes:
        print("!File is already ", resizeRes, " : ", name)
    else:
        resized_image = image.resize(resizeRes)
        resized_image.save(name)
        print("Resized: " + name)
