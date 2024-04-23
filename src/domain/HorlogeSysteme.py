from datetime import datetime
from domain.Horloge import Horloge

class HorlogeSysteme(Horloge):

    def getHour(self):
        heure = datetime.now().time().hour
        return heure
