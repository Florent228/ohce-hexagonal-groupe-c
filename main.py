from Traduction_En import Traduction_En
from Traduction_Fr import Traduction_Fr
from Mirror import Mirror
from Time import Time
import locale

langue_locale = locale.getlocale()[0]
code_langue = langue_locale.split('_')[0]
time = Time.getTime()
langue = Traduction_En(time) if code_langue == 'en' else Traduction_Fr(time)
mirror = Mirror(langue)
mirror.getInput()
mirror.mirror()
langue.goodbye()
