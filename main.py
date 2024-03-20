from Langue import Langue
from Mirror import Mirror
from Time import Time


# Haut niveau
time = Time.getTime()
langue = Langue(time).getLanguage()
mirror = Mirror(langue)
mirror.mirror()
