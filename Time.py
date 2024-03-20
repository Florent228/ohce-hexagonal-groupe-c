from datetime import datetime


class Time:
    @staticmethod
    def getTime():
        # Bas niveau
        time = datetime.now().time().hour
        return time
