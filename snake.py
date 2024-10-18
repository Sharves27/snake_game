import turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.body = [] # a list of objects
        self.initialise()
        # self.head = self.body[0]  => not declared here because, when a new snake is created, the head of the object will not be changed to the new object as the initializer runs only once, i.e., at the creation time of the object
        # self.heading = 0


    def initialise(self):
        self.create_body()
        self.head = self.body[0]
        self.heading = 0


    def create_body(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = turtle.Turtle('square')
        new_turtle.penup()
        new_turtle.color('white')
        new_turtle.goto(position)
        self.body.append(new_turtle)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def move(self):
        for i in range(len(self.body),1,-1):
            self.body[i-1].goto(self.body[i-2].pos())
        else:
            self.head.setheading(self.heading)
            self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.heading = UP

    def down(self):
        if self.head.heading() != UP:
            self.heading = DOWN

    def right(self):
        if self.head.heading() != LEFT:
            self.heading = RIGHT

    def left(self):
        if self.head.heading() != RIGHT:
            self.heading = LEFT

    def reset_snake(self):
        for i in self.body:
            i.goto(1000,1000)
        self.body.clear()
        self.initialise()


