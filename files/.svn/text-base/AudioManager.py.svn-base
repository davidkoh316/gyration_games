
import pygame
import glob

sounds = {}
loadedMusic = ""


def loadSfxSet(level):
    if pygame.mixer.get_init() is None:
        return

    sfxList = glob.glob("sfx/" + level + "/*.ogg")
    if len(sfxList) == 0:
        return
    if not level in sounds:
        sounds[level] = {}
    for sfx in sfxList:
        lvlSfx = pygame.mixer.Sound(sfx)
        if lvlSfx is not None:
            sounds[level][sfx.split("/")[-1]] = lvlSfx
            print "Loaded sound " + sfx.split("/")[-1]
        else:
            print "Failed to load " + sfx.split("/")[-1]


def unloadSfxSet(level):
    if level in sounds:
        print "Unloading " + level + " sfx"
        del sounds[level]


def loadMusic(level):
    global loadedMusic
    if pygame.mixer.get_init() is None:
        return

    dirList = glob.glob("music/" + level + "/*.ogg")
    if len(dirList) == 0:
        print "Failed to load music at " + level
    else:
        pygame.mixer.music.load(dirList[0])
        print "Loaded " + dirList[0]
        loadedMusic = level

#### Unit Test ####


def unitTest():
    pygame.init()
    pygame.display.set_mode((200, 200))
    pygame.mixer.init()
    loadSfxSet("debug")
    loadMusic("debug")
    sounds["debug"]["debugSFX.ogg"].play()
    try:
        pygame.mixer.music.play()
    except pygame.error:
        pass

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    unloadSfxSet("debug")
    pygame.mixer.quit()
    pygame.quit()

if __name__ == "__main__":
    unitTest()
