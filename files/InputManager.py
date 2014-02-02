# check if up key was pressed by doing pygame.key.get_pressed()[pygame.K_UP]
import pygame

global keyState
global keyStatePressed
keyBindings = {
    "jump": pygame.K_SPACE,
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "up": pygame.K_UP,
    "down": pygame.K_DOWN,
    "esc": pygame.K_ESCAPE,
    "enter": pygame.K_RETURN,
    "attack1": pygame.K_a,
    "sword": pygame.K_1,
    "bow": pygame.K_2,
    "cheat1": pygame.K_h,
    "cheat2": pygame.K_j,
    "cheat3": pygame.K_o,
    "cheatboss": pygame.K_b,
    "debugMode": pygame.K_F1,
    "cheatPos": pygame.K_p}
    #"attack2": pygame.K_s,
    #"attack3": pygame.K_d,
    #"attack4": pygame.K_f,
    #"staff": pygame.K_3

cList = [
    "left",
    "right",
    "up",
    "down",
    "jump",
    "attack1",
    "sword",
    "bow",
    "enter",
    "esc"
]

keyStatePressed = []

cBindings = {}
controller = None
cConfigured = False
aCOffset = 0.2

cState = None


def update():
    """In update, set keyState to pygame.key.get_pressed()."""
    global keyState
    global keyStatePressed
    global keyBindings
    global controller
    global cState
    global cStatePressed
    global cList
    global cBindings
    try:
        oldKeyState = keyState
    except NameError:
        oldKeyState = pygame.key.get_pressed()
    keyState = list(pygame.key.get_pressed())
    if len(keyStatePressed) == 0:
        for i in keyState:
            keyStatePressed.append(0)

    for key in keyBindings:
        if keyState[keyBindings[key]] and not oldKeyState[keyBindings[key]]:
            keyStatePressed[keyBindings[key]] = 1
        else:
            keyStatePressed[keyBindings[key]] = 0

    if cConfigured:
        if cState is None:
            cState = getControllerState()
        oldCState = cState
        cState = getControllerState()

        for i in range(len(cBindings.keys())):
            if cState[i] and not oldCState[i]:
                keyStatePressed[keyBindings[cBindings.values()[i]]] = 1
            if cState[i]:
                keyState[keyBindings[cBindings.values()[i]]] = 1

#        for i in range(len(cList)):
#            if cState[i] and not oldCState[i]:
#                keyStatePressed[keyBindings[cList[i]]] = 1


def getAction(action):
    """Returns if the key corresponding to this action was pressed"""
    global keyState
    global keyBindings
    return keyState[keyBindings[action]]


def getPressed(action):
    global keyStatePressed
    global keyBindings
    return keyStatePressed[keyBindings[action]]


def initController():
    global controller
    if controller is None and pygame.joystick.get_count() > 0:
        controller = pygame.joystick.Joystick(0)
        controller.init()
        return True
    return False


def getControllerInput():
    global controller
    for b in range(controller.get_numbuttons()):
        if controller.get_button(b):
            return (1, b)  # is button, button number
    for a in range(controller.get_numaxes()):
        if controller.get_axis(a) > aCOffset:
            return (2, a)  # is axis positive, axis number
        elif controller.get_axis(a) < -aCOffset:
            return (3, a)  # is axis negative, axis number
    return (0, 0)  # nothing pressed


def getControllerState():
    global controller
    global cBindings
    state = []
    for cinput in cBindings:
        if cinput[0] == 1 and controller.get_button(cinput[1]):
            state.append(1)
        elif cinput[0] == 2 and controller.get_axis(cinput[1]) > aCOffset:
            state.append(1)
        elif cinput[0] == 3 and controller.get_axis(cinput[1]) < -aCOffset:
            state.append(1)
        else:
            state.append(0)
    return state


def axisCentered(axisVal):
    return axisVal < aCOffset or axisVal > -aCOffset
