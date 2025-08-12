from dnd_stuff.player import *
from dnd_stuff.backgrounds import *
from dnd_stuff.classes import *

eva = Player("Eva", 1)
eva.set_background(Background.ACOLYTE)
eva_class = Wizard("Wizard", 1, eva.background)
eva.set_class()


print(eva)