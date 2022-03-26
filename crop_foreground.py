import os
import sys
import signal
import cv2
import random
from tqdm import tqdm

def signal_handler(signal, frame):
    print('pressed ctrl + c!!!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

class CropForeground:
  def __init__(self):
    print("crop_foreground init!")
    self.currentDirPath = os.getcwd()
    self.foregroundDirPath = self.currentDirPath + "/1foreground"
    self.foregroundCroppedDirPath = self.currentDirPath + "/2foreground_cropped"
    self.foregroundFilePath_list = os.listdir(self.foregroundDirPath)
    self.rawDataFileFullPath_list = [
        self.foregroundDirPath + '/' + file_name for file_name in self.foregroundFilePath_list]

  def run(self):
    print("run")
    for fileFullPath in tqdm(self.rawDataFileFullPath_list):
      img = cv2.imread(fileFullPath)
      height, width, channels = img.shape

      # Check if the image is valid
      assert height == 1920, "height is not 1920"
      assert width == 2880, "width is not 2880"
      assert channels == 3, "channels is not 3"

      y = random.randrange(0,int(height/3))
      x = random.randrange(0,int(width/3))

      cropped_img = img[y: y + int(height*2/3), x: x + int(width*2/3)]
      height_cropped, width_cropped, channels_cropped = cropped_img.shape

      # Check if the cropped image is valid
      assert height_cropped == 1280, "height is not 1280"
      assert width_cropped == 1920, "width is not 1920"
      assert channels_cropped == 3, "channels is not 3"

      head, tail = os.path.split(fileFullPath)
      cv2.imwrite(self.foregroundCroppedDirPath + "/" + tail, cropped_img)
    print("done!")

if __name__ == "__main__":
    cropForeground = CropForeground()
    cropForeground.run()
