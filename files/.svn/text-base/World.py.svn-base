import pygame
import View
import Globals
import ImageManager
import Entity
import CBackground
import Bucket
import ParticleFactory
import random
import CSpawnMushroom
import CSpawnBird
import CParticle
import CSpawnSlime
import CSpawnStalactite
import CSun
import CSpawnBat
import CSpawnOwl
import CSpawnIcicle
import CSpawnSnowboss
import CSpawnVulture
import CSpawnRabbit
import CSpawnPenguin

# player group holds the player entity
# enemies group holds monster entities
# attack group holds player attack entities (sword, arrow)
# particles group holds particle type entities (death animations)
groups = {
    "particles": pygame.sprite.Group(),
    "enemies": pygame.sprite.Group(),
    "boss": pygame.sprite.Group(),
    "player": pygame.sprite.Group(),
    "equipment": pygame.sprite.Group(),
    "pProjectile": pygame.sprite.Group(),
    "tilesObs": pygame.sprite.Group(),
    "tiles": pygame.sprite.Group(),
    "HUD": pygame.sprite.Group(),
    "HUDText": pygame.sprite.Group(),
    "spawners": pygame.sprite.Group()
}

bg = pygame.sprite.Group()

key = []
tiles = {}
tileSize = 0
playerPos = (0, 0)


#entityBuckets = []
tileBuckets = []
cell_size = 200
world_width = 0


def hashpos(x, y):
    h = int(x) / cell_size +\
        ((int(y) / cell_size) * (world_width / cell_size))
    return h


def findKeyPos(symbol):
    for y in range(len(key)):
        for x in range(len(key[y])):
            if key[y][x] == symbol:
                return (x, y)


def loadMap(cLevel):
    Globals.initSunTracker()

    global key
    global tiles
    global tileSize
    global playerPos
    global tileBuckets
    global world_width

    mapFile = "img/" + cLevel + "/map"
    keyFile = "img/" + cLevel + "/key"

    groups["tiles"].empty()
    groups["tilesObs"].empty()
    groups["spawners"].empty()

    lresources = []
    for resource in ImageManager.levelRes:
        lresources.append(resource)
    for resource in lresources:
        if resource == "one" or resource == "two" or\
                resource == "three" or resource == "four":
            ImageManager.unloadSet(resource)

    ImageManager.loadSet(cLevel)

    key = []
    tiles = {}
    tileSize = 0
    k = open(keyFile)
    y = 0
    x = 0
    for line in k:
        if y == 0:
            iString = ""
            for c in line:
                if c != '\n':
                    iString = iString + c
            tileSize = int(iString)
        else:
            key.append(line)
            temp = 0
            for c in line:
                temp += 1
            if temp > x:
                x = temp
        y += 1
    k.close()

    tileSheet = ImageManager.levelRes[cLevel]["tiles.png"]
    for j in range(y - 1):
        for i in range(x - 1):
            tiles[(i, j)] = tileSheet.subsurface(
                pygame.Rect(i * tileSize, j * tileSize, tileSize, tileSize))

    f = open(mapFile)

    y = 0
    sunID = 0
    for line in f:
        x = 0
        for c in line:
            if c == 'p':
                playerPos = (x * tileSize, y * tileSize)
            elif c == '*':
                Globals.WIN_POS = x * tileSize
            elif c == '-':  # monster 0
                makeMonsterSpawner(x * tileSize, y * tileSize, 0, cLevel)
            elif c == '_':  # monster 1
                makeMonsterSpawner(x * tileSize, y * tileSize, 1, cLevel)
            elif c == '=':  # monster 2
                makeMonsterSpawner(x * tileSize, y * tileSize, 2, cLevel)
            elif c == '+':  # monster 3
                makeMonsterSpawner(x * tileSize, y * tileSize, 3, cLevel)
            elif c == '~':  # sun
                if Globals.SUN_TRACKER[Globals.CURRENT_LEVEL][sunID]:
                    sun = Entity.Entity()
                    sun.componentList.append(CSun.CSun())
                    sun.image = ImageManager.levelRes["effects"]["sun.png"]
                    sun.rect = sun.image.get_rect()
                    sun.rect.x = x * tileSize
                    sun.rect.y = y * tileSize
                    sun.posx = sun.rect.x
                    sun.posy = sun.rect.y
                    groups["enemies"].add(sun)
                    Globals.sunPos()[(sun.rect.x, sun.rect.y)] = sunID
                sunID += 1
            elif c != '\n' and c != ' ':
                block = Entity.Entity()
                block.image = tiles[findKeyPos(c)]
                block.rect = block.image.get_rect()
                block.rect.left = x * tileSize
                block.rect.top = y * tileSize
                if (c >= 'A' and c <= 'Z') or\
                        (c >= '0' and c <= '9'):
                    groups["tilesObs"].add(block)
                else:
                    groups["tiles"].add(block)
            x += 1
        y += 1
    Globals.BOTTOM = y * tileSize
#    block = Entity.Entity()
#    block.image = pygame.Surface((30, 600))
#    block.rect = pygame.Rect((-30, 600, 30, 600))
#    groups["tilesObs"].add(block)

#    entityBuckets = []
    tileBuckets = []
    xmax = (x) * tileSize + cell_size
    ymax = (y) * tileSize + cell_size
    world_width = xmax
    for y in range(ymax / cell_size):
        for x in range(xmax / cell_size):
            tileBuckets.append(Bucket.Bucket(x * cell_size, y * cell_size))
#            entityBuckets.append(Bucket.Bucket(x * cell_size, y * cell_size))

    for tE in groups["tilesObs"]:
        tileBuckets[hashpos(tE.rect.x, tE.rect.y)].add(tE)
        tileBuckets[hashpos(tE.rect.x + tE.rect.width, tE.rect.y)].add(tE)
        tileBuckets[hashpos(tE.rect.x, tE.rect.y + tE.rect.height)].add(tE)
        tileBuckets[hashpos(
            tE.rect.x + tE.rect.width, tE.rect.y + tE.rect.height)].add(tE)


def makeMonsterSpawner(x, y, mType, level):
    spawner = Entity.Entity()
    spawner.posx = x
    spawner.posy = y
    spawner.rect = pygame.Rect(x, y, 1, 1)
    if level == "one":
        if mType == 0:
            spawner.componentList.append(CSpawnMushroom.CSpawnMushroom(1))
        elif mType == 1:
            spawner.componentList.append(CSpawnBird.CSpawnBird(1))
    elif level == "two":
        if mType == 0:
            spawner.componentList.append(CSpawnVulture.CSpawnVulture(1))
        elif mType == 1:
            spawner.componentList.append(CSpawnRabbit.CSpawnRabbit(1))
    elif level == "three":
        if mType == 0:
            spawner.componentList.append(CSpawnBat.CSpawnBat(1))
        elif mType == 1:
            spawner.componentList.append(CSpawnStalactite.CSpawnStalactite(1))
        elif mType == 2:
            spawner.componentList.append(CSpawnSlime.CSpawnSlime(1))
    elif level == "four":
        if mType == 0:
            spawner.componentList.append(CSpawnOwl.CSpawnOwl(1))
        elif mType == 1:
            spawner.componentList.append(CSpawnIcicle.CSpawnIcicle(1))
        elif mType == 2:
            spawner.componentList.append(CSpawnPenguin.CSpawnPenguin(1))
    elif level == "five":
        if mType == 0:
            ImageManager.loadSet("boss")
            spawner.componentList.append(CSpawnSnowboss.CSpawnSnowboss())
            spawner.initialize()
    if len(spawner.componentList) > 0:
        groups["spawners"].add(spawner)


def loadBG(level):
    bg.empty()
    bgEntity = Entity.Entity()
    bgEntity.componentList.append(CBackground.CBackground(level))
    bg.add(bgEntity)


def collide(name1, name2, doKill1=0, doKill2=0):
    return pygame.sprite.groupcollide(
        groups[name1], groups[name2], doKill1, doKill2)


def initialize():
    for name in groups:
        for entity in groups[name].sprites():
            entity.initialize()
    for entity in bg.sprites():
        entity.initialize()


def update(interval):
    groups["particles"].update(interval)
    groups["enemies"].update(interval)
    groups["boss"].update(interval)
    groups["player"].update(interval)
    groups["equipment"].update(interval)
    groups["pProjectile"].update(interval)
    groups["tilesObs"].update(interval)
    groups["tiles"].update(interval)
    groups["HUD"].update(interval)
    groups["HUDText"].update(interval)
    groups["spawners"].update(interval)

    damageCheck()
    fallCheck()

    bg.update(interval)

    vol = pygame.mixer.music.get_volume()
    if vol < Globals.MUSIC_VOLUME:
        pygame.mixer.music.set_volume(vol + 0.01)


def fallCheck():
    for player in groups["player"]:
        if player.posy > Globals.BOTTOM:
            player.kill()
            player.isDead = True
    for enemy in groups["enemies"]:
        if enemy.posy > Globals.BOTTOM:
            enemy.kill()


def damageCheck():
    colList = collide("equipment", "enemies")
    colList = dict(colList.items() + collide("equipment", "boss").items())
    for equipment in colList:
        if equipment.isAttacking and not equipment.hasHit:
            for enemy in colList[equipment]:
                v = vars(enemy)
                if 'hurtFunc' in v:
                    equipment.hasHit = True
                    enemy.hurtFunc(equipment, enemy, equipment.damage)
                    spos = (
                        equipment.posx + (enemy.posx - equipment.posx) / 2.0,
                        equipment.posy + (enemy.posy - equipment.posy) / 2.0)
                    ParticleFactory.makeParticle(
                        ImageManager.levelRes["effects"]["sparkParticle.png"],
                        spos,
                        0.4,
                        ((random.random() - 0.5) * 4.0, (
                            random.random() - 0.5) * 4.0),
                        CParticle.SPIN_CLOCKWISE | CParticle.EXPLODE,
                        pygame.BLEND_ADD)
                    break
        else:
            break
    colList = collide("pProjectile", "enemies")
    colList = dict(colList.items() + collide("pProjectile", "boss").items())
    for proj in colList:
        if not proj.hasHit:
            for enemy in colList[proj]:
                v = vars(enemy)
                if 'hurtFunc' in v:
                    proj.hasHit = True
                    enemy.hurtFunc(proj, enemy, proj.damage)
                    break
        else:
            break
    colList = collide("enemies", "player")
    colList = dict(colList.items() + collide("boss", "player").items())
    for enemy in colList:
        for player in colList[enemy]:
            v = vars(player)
            ve = vars(enemy)
#            if 'regen_time' in v:
#                player.regen_time = 0.0
            if 'hurtFunc' in v and 'damage' in ve:
                player.hurtFunc(enemy, player, enemy.damage)
                break


def draw():
    bg.draw(Globals.SCREEN)

    moveToCam()
    groups["tilesObs"].draw(Globals.SCREEN)
    groups["tiles"].draw(Globals.SCREEN)
    groups["enemies"].draw(Globals.SCREEN)
    for bossEntity in groups["boss"]:
        bossEntity.draw(bossEntity, Globals.SCREEN)
    groups["player"].draw(Globals.SCREEN)
    groups["pProjectile"].draw(Globals.SCREEN)
    groups["equipment"].draw(Globals.SCREEN)
#    groups["particles"].draw(Globals.SCREEN)
    for particle in groups["particles"]:
        particle.pdraw(particle, Globals.SCREEN)
    moveToDefault()

    groups["HUD"].draw(Globals.SCREEN)
    groups["HUDText"].draw(Globals.SCREEN)


def moveToCam():
    for key in groups:
        if key != "spawners" and key != "HUD":
            for entity in groups[key].sprites():
                v = vars(entity)
                if "posx" in v and "posy" in v:
                    entity.rect.x = int(entity.posx - View.getx())
                    entity.rect.y = int(entity.posy - View.gety())
                else:
                    entity.posx = entity.rect.x
                    entity.posy = entity.rect.y
                    entity.rect.x = int(entity.posx - View.getx())
                    entity.rect.y = int(entity.posy - View.gety())


def moveToDefault():
    for key in groups:
        if key != "spawners" and key != "HUD":
            for entity in groups[key].sprites():
                v = vars(entity)
                if "posx" in v and "posy" in v:
                    entity.rect.x = int(entity.posx)
                    entity.rect.y = int(entity.posy)
                else:
                    entity.posx = entity.rect.x
                    entity.posy = entity.rect.y
                    entity.rect.x = int(entity.posx)
                    entity.rect.y = int(entity.posy)


def cleanup():
    for name in groups:
        if name != "player":
            groups[name].empty()


def cleanupCompletely():
    for name in groups:
        groups[name].empty()
