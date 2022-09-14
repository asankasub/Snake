from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        

    def create_snake(self):

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
          
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.snake.append(snake_segment)

    
    def extend(self):
        self.add_segment(self.snake[-1].position())
    
    def reset(self):
        
        for part in self.snake:
            part.goto(-500,0)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        

    def move(self):
        for seg_num in range(len(self.snake)-1, 0, -1):
            x= self.snake[seg_num-1].xcor()
            y= self.snake[seg_num-1].ycor()
            self.snake[seg_num].goto(x,y)
            
        self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 