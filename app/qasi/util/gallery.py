import os
import math
import glob

class Gallery():
    def __init__(self, root_directory, width, height):
        self.root_directory = root_directory
        self.width = width
        self.height = height
        self.imageList = [os.path.basename(x) for x in glob.glob(root_directory+"/*.jpg")]
        self.num_pages = math.ceil(len(self.imageList)/(width*height))

    def get_page(self, page_number):
        page_images = self.imageList[self.width*self.height*(page_number-1):self.width*self.height*page_number]

        imageMatrix = []
        for i in range(self.height):
            imageMatrix.append(page_images[self.width*i:self.width*(i+1)])
        return imageMatrix

