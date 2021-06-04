class Game:
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 0
        self._score = 100

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("You dont have your sole")
            self._lives = 0

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if level > 0:
            del_level = level - self._level
            self._score += 5000 * del_level
            self._level = level

    def __str__(self):
        return "name: {}, Lives: {}, level: {}, score: {}".format(self.name, self._lives, self._level, self._score)


div = Game('Divakar')
print(div)

div.lives -= 2
print(div)

div.lives -= 2
print(div)

div.level += 5
print(div)
# getter and setter function