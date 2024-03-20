from datetime import datetime


class Time:
    @staticmethod
    def getTime(self):
        time = datetime.now().time().hour
        return time
