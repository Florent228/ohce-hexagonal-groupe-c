from datetime import datetime


class Time:
    def getTime(self):
        time = datetime.now().time().hour
        return time
