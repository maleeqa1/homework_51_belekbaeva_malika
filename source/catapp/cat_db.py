import random
class Cat:
    name = ""
    age = 1
    avatar = "images/neutral_cat.jpg"
    satiety = 40
    happiness = 40
    is_sleeping = False

    @classmethod
    def feed(cls):
        if not cls.is_sleeping:
            new_satiety = cls.satiety + 15
            if new_satiety > 100:
                cls.happiness = max(0, cls.happiness - 30)
            else:
                cls.happiness = min(100, cls.happiness + 5)
            cls.satiety = min(100, new_satiety)
            cls.get_avatar()
    @classmethod
    def sleep(cls):
        cls.is_sleeping = True

    @classmethod
    def play(cls):
        if cls.is_sleeping:
            cls.is_sleeping = False
            cls.happiness = max(0, cls.happiness - 5)
            cls.get_avatar()
        else:
            cls.satiety = max(0, cls.satiety - 10)
            if random.randint(1, 3) == 1:
                cls.happiness = 0
                cls.get_avatar()
            else:
                cls.happiness = min(100, cls.happiness + 15)
                cls.get_avatar()
    @classmethod
    def get_avatar(cls):
        if cls.happiness > 70:
            cls.avatar = "images/happy_cat.jpg"
        elif cls.happiness > 30:
            cls.avatar = "images/neutral_cat.jpg"
        else:
            cls.avatar = "images/sad_cat.jpg"




