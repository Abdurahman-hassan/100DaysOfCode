from turtle import Turtle


LIST_OF_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
# up = 90 , down = 270 , left = 180 , right = 0
LIST_OF_DIRECTIONS = [90, 0, 270, 180]
MOVE_DISTANCE = 20


class Snake():

    def __init__(self):
        super().__init__()
        self.list_of_objects = []
        self.create_snake()
        self.head = self.list_of_objects[0]

    def create_snake(self):
        for position in LIST_OF_POSITIONS:
            self.add_a_segment(position)

    def add_a_segment(self, position):
        turtle = Turtle("circle")
        turtle.color("red")
        turtle.penup()
        turtle.goto(position)
        self.list_of_objects.append(turtle)

    def extend_a_snake_body(self):
        # we will add a new segment to the last object position of the snake body
        self.add_a_segment(self.list_of_objects[-1].position())

    # def isTailCollisioned(self):
    #     for the_parts_of_snake_body in self.list_of_objects:
    #         if the_parts_of_snake_body == self.head:
    #             pass
    #         elif self.head.distance(the_parts_of_snake_body) < 10:
    #             return True

    # another way to skip the head we will start from 1 to the end of list
    def isTailCollisioned(self):
        for the_parts_of_snake_body in self.list_of_objects[1:]:
            if self.head.distance(the_parts_of_snake_body) < 10:
                return True

    def move(self):

        for object_of_snake in range(len(self.list_of_objects) - 1, 0, -1):
            # the positions of objects 3, 2, 1
            new_x_position = self.list_of_objects[object_of_snake - 1].xcor()
            new_y_position = self.list_of_objects[object_of_snake - 1].ycor()
            # the object in position 3 will go to the object in position 2 will go to the object in position 1
            self.list_of_objects[object_of_snake].goto(new_x_position, new_y_position)

        self.head.forward(MOVE_DISTANCE)

    def up_position(self):
        if self.head.heading() != LIST_OF_DIRECTIONS[2]:
            self.head.setheading(LIST_OF_DIRECTIONS[0])

    def right_position(self):
        if self.head.heading() != LIST_OF_DIRECTIONS[3]:
            self.head.setheading(LIST_OF_DIRECTIONS[1])

    def down_position(self):
        if self.head.heading() != LIST_OF_DIRECTIONS[0]:
            self.head.setheading(LIST_OF_DIRECTIONS[2])

    def left_position(self):
        if self.head.heading() != LIST_OF_DIRECTIONS[1]:
            self.head.setheading(LIST_OF_DIRECTIONS[3])
