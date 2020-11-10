import os
import torch
from torch.utils.data import Dataset
from PIL import Image
import torchvision.transforms.functional as TF

class DataReader(Dataset):

    def __init__(self,dirName, tranform=None):
        self.listOfFile = self.getListOfFiles(dirName)
        print(self.listOfFile)
    def __len__(self):
        return len(self.listOfFiles) / 3

    def __getitem__(self, index):
        x = Image.open(self.listOfFile[index * 3])
        y = Image.open(self.listOfFile[(index * 3)+1])
        x2 = Image.open(self.listOfFile[(index * 3)+2])
        x = TF.to_tensor(x)
        y = TF.to_tensor(y)
        x2 = TF.to_tensor(x2)
        return [torch.cat((x, x2)), y]

    def getListOfFiles(self, dirName):
        listOfFile = os.listdir(dirName)
        allFiles = []
        for entry in listOfFile:
            fullPath = os.path.join(dirName, entry)
            if os.path.isdir(fullPath):
                allFiles = allFiles + self.getListOfFiles(fullPath)
            else:
                allFiles.append(fullPath)
        return allFiles

dirName = r"C:\Users\user\Desktop\vimeo_triplet\sequences"

test = DataReader(dirName)

for x,y in test:
    print(x.shape)
    break

