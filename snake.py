from turtle import Turtle


class Snake:

    def __init__(self):
        self.size = 3
        self.directions = [(10, 0), (0, 10), (-10, 0), (0, -10)]
        firstblock = Turtle()
        firstblock.penup()
        firstblock.color("white")
        firstblock.shape("square")
        self.snake = [self.directions[0], firstblock]
        for _ in range(2):
            self.add_block()

    def add_block(self):
        for _ in range(2):
            newblock = Turtle("square")
            # newblock.setpos(tuple(numpy.subtract(snake[-1].pos(), snake[0])))
            newblock.speed("fastest")
            newblock.setpos(self.snake[-1].pos())
            newblock.color("white")
            newblock.penup()
            for block in reversed(self.snake[2::]):
                block.setpos(self.snake[self.snake.index(block) - 1].pos())
            self.snake[1].setpos(self.snake[1].pos() + self.snake[0])
            self.snake.append(newblock)

    def move(self):
        for _ in range(2):
            for block in reversed(self.snake[2::]):
                block.setpos(self.snake[self.snake.index(block) - 1].pos())
            self.snake[1].setpos(self.snake[1].pos() + self.snake[0])

    def up(self):
        if self.snake[0] != self.directions[3]:
            self.snake[0] = self.directions[1]

    def right(self):
        if self.snake[0] != self.directions[2]:
            self.snake[0] = self.directions[0]

    def left(self):
        if self.snake[0] != self.directions[0]:
            self.snake[0] = self.directions[2]

    def down(self):
        if self.snake[0] != self.directions[1]:
            self.snake[0] = self.directions[3]

    def collided(self):
        for block in self.snake[2:]:
            if block.pos() == self.snake[1].pos():
                return True
        if abs(self.snake[1].xcor()) > 350 or abs(self.snake[1].ycor()) > 300:
            return True
        return False
