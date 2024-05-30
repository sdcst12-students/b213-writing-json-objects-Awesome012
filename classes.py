class car:

    make = ""
    year = 0
    model = ""
    body = {
        'style': "",
        'color' : ""
    }

    def startcar(self):
        pass
        pass

    def throttle(self):
        pass
        pass

    def __init__(self,a,b,c):
        self.make = a
        self.year = b
        self.model = c
        pass
        self.throttle()

myCar = car('Honda',2020,'CRX')
print(myCar.make)