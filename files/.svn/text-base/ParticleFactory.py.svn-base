import Entity
import CParticle
import World


def makeParticle(sprite, pos, lifetime=1, direction=(0, 0), style=0, flags=0):
    entity = Entity.Entity()
    entity.componentList.append(
        CParticle.CParticle(sprite, pos, lifetime, direction, style, flags))
    World.groups["particles"].add(entity)
    entity.initialize()
