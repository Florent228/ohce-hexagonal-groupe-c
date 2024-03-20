from dataclasses import dataclass
from datetime import datetime

@dataclass
class Mirror:
    mot: str
    def is_morning(self) -> bool:
        return datetime.now().hour <= 12

    def is_evening(self) -> bool:
        return datetime.now().hour >= 18

    def welcome(self):
        if self.is_evening():
            print("Bonjour ")
        elif self.is_evening():
            print("Bonsoir ")

    def goodbye(self):
        print("Au revoir")

    def prompt_message(self):
        print(">")
        print("Entrer un mot : ")
        self.mot = input()

    def is_palindrome(self):
        reversed = self.mot[::-1]
        return self.mot == reversed

    def mirroring(self):
        if self.is_palindrome():
            print("Bien dit !")
