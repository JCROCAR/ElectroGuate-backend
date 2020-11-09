import base64
import pyrebase
import json
import os

from django.utils import timezone
from ElectroGuate import settings



def image(folder, name):
    config = ""
    with open(settings.BASE_DIR+'/config.json') as json_file:
            config = json.load(json_file)
    if config != "":
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = folder+"/"+name
        path_local = settings.BASE_DIR+"/"+name
        img=storage.child(path_on_cloud).put(path_local)
        os.remove(path_local)
        return storage.child(path_on_cloud).get_url(token=img["downloadTokens"]).split("&")[0]
    else:
        return "Error"

def decode_image(data):
    format, imgstr = data.split(";base64,")
    ext = format.split("/")[-1]
    now = timezone.now()
    image_data = base64.b64decode(imgstr)
    image_path = f"{now:%Y%m%d%H%M%S}{now.microsecond}.{ext}"
    image_file = open(image_path,"wb")
    image_file.write(image_data)
    image_file.close()
    return image_path


