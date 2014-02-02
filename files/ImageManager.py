
import pygame
import glob

levelRes = {}


def loadImage(filename):
    loadedImage = pygame.image.load(filename)
    if loadedImage is None:
        return None
    if loadedImage.get_alpha() is None:
        loadedImage = loadedImage.convert()
    else:
        loadedImage = loadedImage.convert_alpha()
    return loadedImage


def loadSet(level):
    imgList = glob.glob("img/" + level + "/*.png")
    if len(imgList) == 0:
        return
    if not level in levelRes:
        levelRes[level] = {}
    for img in imgList:
        lvlImage = loadImage(img)
        if lvlImage is not None:
            levelRes[level][img.split("/")[-1]] = lvlImage
            print "Loaded image " + img.split("/")[-1]
        else:
            print "Failed to load " + img.split("/")[-1]


def unloadSet(level):
    if level in levelRes:
        print "Unloading " + level + " img"
        del levelRes[level]


def unloadAll():
    llist = []
    for level in levelRes:
        llist.append(level)

    for level in llist:
        print "Unloading " + level + " img"
        del levelRes[level]


#### Unit Test ####


def unitTest():
    pygame.init()
    pygame.display.set_mode((300, 300))
    loadSet("debug")
    print levelRes
    unloadSet("debug")
    print levelRes
    pygame.quit()

if __name__ == "__main__":
    unitTest()
