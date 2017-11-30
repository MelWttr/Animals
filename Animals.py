class Animal:

    name = ""
    color = ""
    is_alive = True
    speed = 0

    def __init__(self, name, color, is_alive, speed):
        self.name = name
        self.color = color
        self.is_alive = is_alive
        self.speed = speed

    def eat(self):
        print("{} is eating..".format(self.name))

    def move(self, moving_type):
        if moving_type == "walking":
            print("{} is walking".format(self.name))
        elif moving_type == "running":
            print("{} is running".format(self.name))

    def stop(self):
        self.speed = 0

    def is_moving(self):
        if self.speed == 0:
            return True
        else:
            return False

    def die(self):
        self.is_alive = False


class Cow(Animal):
    def __init__(self, name, color, is_alive, speed):
        super().__init__(name, color, is_alive, speed)

    def  moo(self):
        print("mooo")


class Goat(Animal):
    def __init__(self, name, color, is_alive, speed):
        super().__init__(name, color, is_alive, speed)

    def bleat(self):
        print("meee")


class Sheep(Animal):
    def __init__(self, name, color, is_alive, speed):
        super().__init__(name, color, is_alive, speed)

    def bleat(self):
        print("beee")


class Sheep(Animal):
    def __init__(self, name, color, is_alive, speed):
        super().__init__(name, color, is_alive, speed)

    def grunt(self):
        print("naf naf uiii")


class Bird(Animal):
    flying_speed = 0

    def __init__(self, flying_speed, name, color, is_alive, speed):
        super().__init__(name, color, is_alive, speed)
        self.flying_speed = flying_speed

    def move(self, moving_type):
        if moving_type == "walking":
            print("{} is walking".format(self.name))
        elif moving_type == "running":
            print ("{} is running".format(self.name))
        elif moving_type == "flying":
            print("{} is flying".format(self.name))


class Duck(Bird):
    swimming_speed = 0

    def __init__(self, swimming_speed, flying_speed, name, color, is_alive, speed):
        super().__init__(flying_speed, name, color, is_alive, speed)
        self.swimming_speed = swimming_speed

    def move(self, moving_type):
        if moving_type == "walking":
            print("{} is walking".format(self.name))
        elif moving_type == "running":
            print ("{} is running".format(self.name))
        elif moving_type == "flying":
            print("{} is flying".format(self.name))
        elif moving_type == "swimming":
            print("{} is swimming".format(self.name))

    def quack(self):
        print("quack")


class Han(Bird):
    def __init__(self, flying_speed, name, color, is_alive, speed):
        super().__init__(flying_speed, name, color, is_alive, speed)

    def crow(self):
        print("crow")


class Goose(Duck):
    def __init__(self, swimming_speed, flying_speed, name, color, is_alive, speed):
        super().__init__(swimming_speed, flying_speed, name, color, is_alive, speed)

    def hiss(self):
        print("shhhhh")


burenka = Cow("burenka", "black/white", True, 2)
guns = Goat("guns", "grey", True, 1)
manya = Sheep("manya", "white", True, 1)
scroodge = Duck(2, 3, "scroodge", "white", True, 1)
ryaba = Han(1, "ryaba", "gray", True, 1)
gusena = Goose(3, 2, "gusena", "pink", True, 1)

gusena.hiss()
burenka.moo()
guns.bleat()
manya.die()
scroodge.quack()
ryaba.move("running")