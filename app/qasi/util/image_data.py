import matplotlib.image as mpimg
import os 

class ImageData():
    def __init__(self, image):
        if isinstance(image, str):
            self.img = mpimg.imread(image)
            self.height = self.img.shape[0]
            self.width = self.img.shape[1]
        else:
            self.img = image
            self.height = self.img.shape[0]
            self.width = self.img.shape[1]

    def get_subimage(self, x, y, w, h):
        coord_x = int(self.width*x)
        coord_y = int(self.height*y)
        coord_w = int(self.width*w)
        coord_h = int(self.height*h)

        return ImageData(self.img[coord_y:coord_y+coord_h,coord_x:coord_x+coord_w])

    def save(self, directory, filename):
        if not os.path.isdir(directory):
            os.mkdir(directory)
        mpimg.imsave(directory+"/"+str(filename), self.img)

