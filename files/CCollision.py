import pygame
import Component
import World


def updatePosition(entity):
    entity.rect.x = int(entity.posx)
    collided = False
    h = []
    h.append(World.hashpos(entity.rect.x, entity.rect.y))
    h.append(World.hashpos(entity.rect.x + entity.rect.width, entity.rect.y))
    h.append(World.hashpos(entity.rect.x, entity.rect.y + entity.rect.height))
    h.append(World.hashpos(
        entity.rect.x + entity.rect.width, entity.rect.y + entity.rect.height))
    for hashVal in h:
        try:
            for tile in World.tileBuckets[hashVal].objects():
                if pygame.sprite.collide_rect(entity, tile):
                    if entity.rect.x < tile.rect.x:
                        entity.rect.x = tile.rect.x - entity.rect.width - 1
                    elif entity.rect.x > tile.rect.x:
                        entity.rect.x = tile.rect.x +\
                            tile.rect.width + 1
                    entity.velx = 0
                    entity.posx = entity.rect.x
                    collided = True
                    break
            if collided:
                break
        except IndexError:
            pass
    if entity.isGrounded:
        entity.rect.y += 1
    else:
        entity.rect.y = int(entity.posy)
    collided = False
    h = []
    h.append(World.hashpos(entity.rect.x, entity.rect.y))
    h.append(World.hashpos(entity.rect.x + entity.rect.width, entity.rect.y))
    h.append(World.hashpos(entity.rect.x, entity.rect.y + entity.rect.height))
    h.append(World.hashpos(
        entity.rect.x + entity.rect.width, entity.rect.y + entity.rect.height))
    for hashVal in h:
        try:
            for tile in World.tileBuckets[hashVal].objects():
                if pygame.sprite.collide_rect(entity, tile):
                    #entity.vely = 0
                    if entity.rect.y < tile.rect.y:
                        entity.rect.y = tile.rect.y - entity.rect.height
                        entity.isGrounded = True
                        entity.vely = 0
                    elif entity.rect.y > tile.rect.y:
                        entity.rect.y = tile.rect.y +\
                            tile.rect.height + 1
                        entity.vely = entity.vely + 100
                    entity.posy = entity.rect.y
                    collided = True
                    break
            if collided:
                break
        except IndexError:
            pass
    if not collided:
        entity.isGrounded = False


class CCollision(Component.Component):

    def initialize(self, entity):
        entity.update_pos = updatePosition
