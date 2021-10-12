from PIL import Image  # Python Image LIbrary - Image processing

import glob

sInputFolder = "image_processing\\in\\"
sFilename = ""
sOutputFolder = "image_processing\\out\\"

print(glob.glob(sInputFolder + "*.png"))

# based on SO Answer: https://stackoverflow.com/a/43258974/5086335

for file in glob.glob(sInputFolder + "*.png"):
    # Actual image convert:
    im = Image.open(file)
    rgb_im = im.convert('RGB')

    # Save the file with .jpg format:
    sFilename = file.split("\\")[-1]
    sFilename = sFilename.replace("png", "jpg")
    rgb_im.save(sOutputFolder + sFilename, quality=95)
