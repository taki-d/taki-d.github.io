from PIL import Image
import PIL.ExifTags as ExifTags
import os
import datetime

if __name__=='__main__':
    list = os.scandir(".")

    images = {}

    for f in list:
        extentions = ["png", "jpg", "JPG"]
        if f.name.split(".")[-1] in extentions:
            img = Image.open(f.name)
            exif = img.getexif().items()
            
            tags = {}
            for k, v in exif:
                if k in ExifTags.TAGS:
                    tags[ExifTags.TAGS[k]] = v

            if 'DateTime' in tags:
                time = datetime.datetime.strptime(tags["DateTime"], "%Y:%m:%d %H:%M:%S")
                images[time] = f.name

    sorted_images = sorted(images.items(), key=lambda x:x[0])

    for k, v in sorted_images:
        print("{{< resizeimage src=\"", end="")
        print(v, end="")
        print("\" alt=\"\" >}}")

        print(k)