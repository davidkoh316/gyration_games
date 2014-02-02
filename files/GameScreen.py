import ImageManager
import AudioManager
import InputManager
import PauseScreen
import WinScreen
import OverScreen
import CompletedGameScreen
import SkillScreen
import Globals
import State
import World
import Entity
import CAnimation
import CPhysics
import CBasicControl
import pygame
import CCollision
import CView
import CAttach
import CLiving
import CDamage
import CHUDHealth
import CPlayer
import CDeathParticle
import CHUDMana
import CHUDHealthText
import CHUDManaText
import CHUDScoreText
import CHUDSunText
import CHUDBoss
import random


class GameScreen(State.State):
    def __init__(self):
        ImageManager.loadSet("player")
        ImageManager.loadSet("effects")
        ImageManager.loadSet(Globals.CURRENT_LEVEL)

        if len(World.groups["HUD"].sprites()) == 0:
            healthHud = Entity.Entity()
            healthHud.componentList.append(CHUDHealth.CHUDHealth())
            World.groups["HUD"].add(healthHud)

            #manaHud = Entity.Entity()
            #manaHud.componentList.append(CHUDMana.CHUDMana())
            #World.groups["HUD"].add(manaHud)

            healthText = Entity.Entity()
            healthText.componentList.append(CHUDHealthText.CHUDHealthText())
            World.groups["HUDText"].add(healthText)

            #manaText = Entity.Entity()
            #manaText.componentList.append(CHUDManaText.CHUDManaText())
            #World.groups["HUDText"].add(manaText)

            scoreText = Entity.Entity()
            scoreText.componentList.append(CHUDScoreText.CHUDScoreText())
            World.groups["HUDText"].add(scoreText)

            sunText = Entity.Entity()
            sunText.componentList.append(CHUDSunText.CHUDSunText())
            World.groups["HUDText"].add(sunText)

            if Globals.CURRENT_LEVEL == "five":
                bossHUD = Entity.Entity()
                bossHUD.componentList.append(CHUDBoss.CHUDBoss())
                World.groups["HUD"].add(bossHUD)

        if Globals.PLAYER is None:
            World.loadMap(Globals.CURRENT_LEVEL)
            World.loadBG(Globals.CURRENT_LEVEL)
            World.initialize()

            entity = Entity.Entity()
            entity.componentList.append(CAnimation.CAnimation(
                ImageManager.levelRes["player"]["Noel_SpriteSheet.png"],
                6, 6, 0, 0.17))
            entity.componentList.append(CPhysics.CPhysics())
            entity.componentList.append(CBasicControl.CBasicControl())
            entity.componentList.append(CCollision.CCollision())
            entity.componentList.append(CView.CView())
            entity.componentList.append(
                CLiving.CLiving(Globals.PLAYER_MAX_HEALTH))
            entity.componentList.append(CDamage.CDamage(Globals.PLAYER_DAMAGE))
            entity.componentList.append(CPlayer.CPlayer())
            entity.componentList.append(CDeathParticle.CDeathParticle(
                ImageManager.levelRes["player"]["Noel_Dead.png"],
                3,
                (0, -20),
                0,
                pygame.BLEND_ADD))
            World.groups["player"].add(entity)
            entity.initialize()
            entity.state = 1
            Globals.PLAYER = entity
            Globals.WIN = False
            Globals.TIME = 120

            zord = Entity.Entity()
            zord.componentList.append(CAnimation.CAnimation(
                ImageManager.levelRes["player"]["Zord_Spritesheet.png"],
                6, 6, 0, 0))
            zord.componentList.append(CPhysics.CPhysics())
            zord.accy = 0
            zord.componentList.append(CAttach.CAttach(entity, 53))
            World.groups["equipment"].add(zord)
            zord.initialize()

            if not Globals.CHECKPOINT_SET or Globals.CURRENT_LEVEL == "five":
                Globals.PLAYER.posx = World.playerPos[0]
                Globals.PLAYER.posy = World.playerPos[1]
            else:
                Globals.PLAYER.posx = float(Globals.getCheckpointPos()[0])
                Globals.PLAYER.posy = float(Globals.getCheckpointPos()[1])

        self.timer = 1.0
        self.bossWinTimer = 4.0

        if AudioManager.loadedMusic != Globals.CURRENT_LEVEL or\
                not pygame.mixer.music.get_busy():
            AudioManager.loadMusic(Globals.CURRENT_LEVEL)
            if AudioManager.loadedMusic == Globals.CURRENT_LEVEL:
                pygame.mixer.music.play(-1)
                if Globals.CURRENT_LEVEL == "five":
                    pygame.mixer.music.set_volume(0.1)

        if not Globals.CURRENT_LEVEL == "five":
            self.sunArray = []
            for sun in Globals.SUN_TRACKER[Globals.CURRENT_LEVEL]:
                self.sunArray.append(sun)

    def update(self, time):
        if Globals.WIN:
            if Globals.CURRENT_LEVEL == "five":
                if self.bossWinTimer > 0.0:
                    self.bossWinTimer -= time
                else:
                    self.exitFinal()
                    return
            else:
                if Globals.TIME > 0:
                    Globals.SCORE = Globals.SCORE + 10 * int(Globals.TIME)
                self.exitGame()
                return
        if Globals.PLAYER.isDead:
            self.timer -= time
            if self.timer <= 0:
                self.deadScreen()
                return
        if InputManager.getPressed("esc"):
            self.exitScreen()
            return
        Globals.TIME = Globals.TIME - time
        World.update(time)
        if not Globals.CHECKPOINT_SET and\
                Globals.CURRENT_LEVEL in Globals.CHECKPOINT_POS:
            if Globals.PLAYER.rect.x > Globals.getCheckpointPos()[0]:
                Globals.CHECKPOINT_SET = True

    def evaluateScores(self):
        readScores = open("highScores.txt", "r+")
        hs = {}
        findMin = False
        for line in readScores:
            name, x, score = line.partition(" ")
            score = int(score[:-1])
            hs[score] = name
            if Globals.SCORE >= int(score):
                findMin = True
        readScores.close()
        if findMin:
            writeScores = open("highScores.txt", "w")
            minScore = True
            for s in sorted(hs.iterkeys()):
                if minScore:
                    writeScores.write("name " + str(Globals.SCORE) + "\n")
                    minScore = False
                else:
                    writeScores.write(hs[s] + " " + str(s) + "\n")
            writeScores.close()

    def draw(self):
        World.draw()

    def exitScreen(self):
        ImageManager.unloadSet("debug")
        AudioManager.unloadSfxSet("debug")
        pygame.mixer.music.fadeout(1000)
        Globals.STATE = PauseScreen.PauseScreen()

    def exitGame(self):
        ImageManager.unloadSet("debug")
        AudioManager.unloadSfxSet("debug")
        World.cleanupCompletely()
        Globals.PLAYER = None
        pygame.mixer.music.fadeout(1000)
        if Globals.CURRENT_LEVEL == "one":
            Globals.CURRENT_LEVEL = "two"
            if Globals.LEVELS_BEAT < 1:
                Globals.LEVELS_BEAT = 1
        elif Globals.CURRENT_LEVEL == "two":
            Globals.CURRENT_LEVEL = "three"
            if Globals.LEVELS_BEAT < 2:
                Globals.LEVELS_BEAT = 2
        elif Globals.CURRENT_LEVEL == "three":
            Globals.CURRENT_LEVEL = "four"
            if Globals.LEVELS_BEAT < 3:
                Globals.LEVELS_BEAT = 3
        elif Globals.CURRENT_LEVEL == "four":
            Globals.CURRENT_LEVEL = "five"
            if Globals.LEVELS_BEAT < 4:
                Globals.LEVELS_BEAT = 4
        Globals.MINI_SUNS_INLVL = 0
        Globals.STATE = WinScreen.WinScreen()
        Globals.CHECKPOINT_SET = False

    def exitFinal(self):
        ImageManager.unloadSet("debug")
        AudioManager.unloadSfxSet("debug")
        World.cleanupCompletely()
        AudioManager.loadMusic("title")
        pygame.mixer.music.play(-1)
        if Globals.LEVELS_BEAT < 5:
            Globals.LEVELS_BEAT = 5
        Globals.SCORE = Globals.SCORE + 5000*Globals.MINI_SUNS
        Globals.PLAYER = None
        Globals.STATE = CompletedGameScreen.CompletedGameScreen()
        Globals.CHECKPOINT_SET = False

    def deadScreen(self):
        ImageManager.unloadSet("debug")
        AudioManager.unloadSfxSet("debug")
        World.cleanupCompletely()
        Globals.PLAYER = None
        pygame.mixer.music.stop()
        if Globals.MINI_SUNS_INLVL > 0:
            Globals.MINI_SUNS = Globals.MINI_SUNS - 1
        Globals.SCORE = Globals.SCORE - 1000*Globals.MINI_SUNS_INLVL
        if Globals.CURRENT_LEVEL != "five":
            pickCount = random.randint(1, 10)
            index = 0
            if Globals.MINI_SUNS_INLVL > 0:  # remove sun code
                while pickCount > 0:
                    index = (index + 1) % 5
                    if Globals.sunTr()[index]:
                        continue
                    pickCount -= 1
                Globals.SUN_TRACKER[Globals.CURRENT_LEVEL][index] = True
#            Globals.SUN_TRACKER[Globals.CURRENT_LEVEL] = self.sunArray
        Globals.STATE = OverScreen.OverScreen()
        Globals.MINI_SUNS_INLVL = 0
