class Animal:

    NAME = ""
    COLOR = ""
    IS_ALIVE = True
    SPEED = 0

    def __init__(self, name, color, is_alive, speed):
        self.NAME = name
        self.COLOR = color
        self.IS_AlIVE = is_alive
        self.SPEED = speed

    def eat(self):
        print("{} is eating..".format(self.NAME))

    def move(self, moving_type):
        if moving_type == "walking":
            print("{} is walking".format(self.NAME))
        elif moving_type == "running":
            print("{} is running".format(self.NAME))

    def stop(self):
        self.SPEED = 0

    def is_moving(self):
        if self.SPEED == 0:
            return True
        else:
            return False

    def die(self):
        self.IS_ALIVE = False


class Cow(Animal):
    def __init__(self, name, color, speed):
        self.NAME = name
        self.COLOR = color
        self.SPEED = speed

    def  moo(self):
        print("mooo")


class Goat(Animal):
    def __init__(self, name, color, speed):
        self.NAME = name
        self.COLOR = color
        self.SPEED = speed

    def bleat(self):
        print("meee")


class Sheep(Animal):
    def __init__(self, name, color, speed):
        self.NAME = name
        self.COLOR = color
        self.SPEED = speed

    def bleat(self):
        print("beee")


class Sheep(Animal):
    def __init__(self, name, color, speed):
        self.NAME = name
        self.COLOR = color
        self.SPEED = speed

    def grunt(self):
        print("naf naf uiii")


class Bird(Animal):
    FLYING_SPEED = 0

    def __init__(self, name, color, speed, flying_speed):
        self.NAME = name
        self.COLOR = color
        self.SPEED = speed
        self.FLYING_SPEED = flying_speed

    def move(self, moving_type):
        if moving_type == "walking":
            print("{} is walking".format(self.NAME))
        elif moving_type == "running":
            print ("{} is running".format(self.NAME))
        elif moving_type == "flying":
            print("{} is flying".format(self.NAME))


class Duck(Animal, Bird):
    SWIMMING_SPEED = 0

    def __init__(self, name, color, speed, flying_speed, swimming_speed):
        self.NAME = name
        self.COLOR = color
        self.SPEED = speed
        self.FLYING_SPEED = flying_speed
        self.SWIMMING_SPEED = swimming_speed

    def move(self, moving_type):
        if moving_type == "walking":
            print("{} is walking".format(self.NAME))
        elif moving_type == "running":
            print ("{} is running".format(self.NAME))
        elif moving_type == "flying":
            print("{} is flying".format(self.NAME))
        elif moving_type == "swimming":
            print("{} is swimming".format(self.NAME))

    def quack(self):
        print("quack")


class Han(Animal, Bird):
    def __init__(self, name, color, speed, flying_speed):
        self.NAME = name
        self.COLOR = color
        self.SPEED = speed
        self.FLYING_SPEED = flying_speed

    def crow(self):
        print("crow")


class Goose(Animal, Bird, Duck):
    def __init__(self, name, color, speed, flying_speed, swimming_speed):
        self.NAME = name
        self.COLOR = color
        self.SPEED = speed
        self.FLYING_SPEED = flying_speed
        self.SWIMMING_SPEED = swimming_speed

    def hiss(self):
        print("shhhhh")




