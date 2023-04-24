import os
from PIL import Image


class ImageUtil():
    def __init__(self,_path):
        self.img = Image.open(_path).convert("RGBA")

    def invert_image(self):
        datas = self.img.getdata()
        newData = []
        for items in datas:
            if items[3] ==255 :
                newData.append((0, 0, 0, 0))
            elif items[3] ==0 :
                newData.append((255, 255, 255, 255))
            else:
                item =255-items[3]
                newData.append((255, 255, 255, item))

        self.img.putdata(newData)
        return self
    
         
    def save_image(self,format:str,image_name:str):
        if format=='PNG':
            self.img.save(f"{image_name}.png","PNG")
        elif format=='WEBP':
            self.img.save(f"{image_name}.webp","WEBP")

