class Traduction_En:

    def __init__(self, time):
        self.time = time

    def greeting(self):
        if self.time < 12:
            print("Good morning!")
        elif self.time > 12 and self.time < 20:
            print("Good afternoon!")
        else:
            print("Good evenning!")
        print("Enter a word to reverse")

    def goodbye(self):
        print("Goodbye!")

    def isPalindrome(self):
        print("Well said!")
