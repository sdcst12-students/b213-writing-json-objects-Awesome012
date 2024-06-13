class game:
    guess = 0

    def checkInteger(self,x):
        # if x is an integer return true
        # else return false
        return True

    def askInput(self):
        x = ""
        while self.checkInteger(x):
            x = input("enter a number")
            try:
                x = int(x)
            except:
                print("that is not number")
        return x

    def checkVale(self):
        # check to see if guess is too high or low
        if self.guess > self.secretNumber:
            return 1
        elif self.guess < self.secretNumber:
            return -1
        else:
            return 0

    def intstructions(self):
        pass

    def main(self):
        self.instructions()
        self.guess = self.askInput()
        self.checkVale()

    def __init__(self):
        self.secretNumber = 20


myGame = game()
print(myGame.secretNumber)