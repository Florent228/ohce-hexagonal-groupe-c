from Mirror import Mirror
import locale

langue_systeme = locale.getlocale()[0]
print(langue_systeme)
mirror = Mirror(langue_systeme)
mirror.greeting()
mirror.getInput()
mirror.mirror()
mirror.goodbye()
