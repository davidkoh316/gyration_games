# Global variables

DEBUG_MODE = False

RUNNING = True
SCREEN = None
WIDTH = None
HEIGHT = None

STATE = None
FONT = None
GAMESTARTED = False
LASTSCREENMAIN = False
LASTSCREENPAUSE = False
LASTSCREENSETTING = False
GAMECOMPLETED = False

PLAYER = None
PLAYER_MAX_HEALTH = 15
SKILL_MAX_HEALTH = 0
PLAYER_REGEN_TIME = 4
PLAYER_DAMAGE = 5
SKILL_DAMAGE = 0
PLAYER_MAX_MP = 10
PLAYER_SKILL = 0
PLAYER_JUMP = 610.0
SKILL_JUMP = 0
ARROW_VELOCITY = 700.0
ARROW_HITS = 1
ARROW_DAMAGE = 2
BOW_COOLDOWN = 0.7
MAX_SKILL = 9

MINI_SUNS = 0
MINI_SUNS_INLVL = 0

SUN_TRACKER = {}
SUN_T_POS = {}
SUN_T_INIT = False

CURRENT_LEVEL = "one"
LEVELS_BEAT = 0

BOTTOM = None

SCORE = 0

WIN = None

WIN_POS = 10000

TIME = 120

MUSIC_VOLUME = 1.0

BOSS = None

CHECKPOINT_POS = {
    "one": (3619, 1320),
    "two": (5275, 800),
    "three": (1953, 1560),
    "four": (4419, 680)
}
CHECKPOINT_SET = False


def getCheckpointPos():
    if CURRENT_LEVEL != "five":
        return CHECKPOINT_POS[CURRENT_LEVEL]
    return None


def initSunTracker(forceReset=False):
    global SUN_TRACKER
    global SUN_T_INIT

    if not SUN_T_INIT or forceReset:
        SUN_TRACKER["one"] = [True, True, True, True, True]
        SUN_TRACKER["two"] = [True, True, True, True, True]
        SUN_TRACKER["three"] = [True, True, True, True, True]
        SUN_TRACKER["four"] = [True, True, True, True, True]
        SUN_T_POS["one"] = {}
        SUN_T_POS["two"] = {}
        SUN_T_POS["three"] = {}
        SUN_T_POS["four"] = {}
        SUN_T_INIT = True


def sunTr():
    global SUN_TRACKER
    global CURRENT_LEVEL

    return SUN_TRACKER[CURRENT_LEVEL]


def sunPos():
    global SUN_T_POS
    global CURRENT_LEVEL

    return SUN_T_POS[CURRENT_LEVEL]
