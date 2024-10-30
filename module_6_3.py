class Horse:
    def __init__(self, x_distance = 0, sound = 'Frrr'):
        self.x_distance = x_distance
        self.sound = sound

    def run(self, dx):
        self.dx = self.x_distance + dx
class Eagle:
    def __init__(self, y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance
        self.sound = sound
    def fly(self, dy):
        self.dy = self.y_distance + dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__(x_distance)
        super().__init__(y_distance)
        super().__init__(sound)

    def move(self):
        super().run()
        super().fly()
    def get_pos(self):
        print(self.x_distance, self.y_distance)
    def voice(self):
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
