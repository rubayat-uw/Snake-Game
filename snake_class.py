"""
This module contains a structure class for the Snake module.
"""


class Snake:
    """
        This is the main class for the snake.

    Attributes:
    -----------
        head_position : tuple(int, int)
            The x- and y-coordinates for the head position of snake
        block_size : tuple(int, int)
            The width and height of the snake.
        color_block : tuple(int, int, int)
            A tuple of values between 0 and 255 indicating the r, g, b value of the block color

    Methods:
    --------

        Movement function:
            Snake moves in one of the four different directions such as up, down, left and right.
            The rest of the body must follow the head position but not in same way.

        inside_bounds:
            Returns true if the Snake is inside bounds that means right side of snake coincides with right side of bounds
            otherwise return false.

        check_collision:
            It is used to check if any of Snake Object collides with shape at the given coordinates and of given size.

        check_collision_with_fruit():
            It is used to check if any of Snake Object collides with Fruit at the given coordinates and of given size.

        check_collision_with_self():
            It is used to check if the head Block in the Snake Object collides with any other Block in the Snake Object.

        grow():
            It is used to increases the size of the Snake by appending new Block object.

    """

    def __init__(self, head_position, block_size, block_colour):
        """Initialize the snake object. The parameters are passed on to the init function of Snake

        Attributes:
        -----------
        head_position : tuple(int, int)
            The x- and y-coordinates for the head position of snake
        block_size : tuple(int, int)
            The width and height of the snake.
        color_block : tuple(int, int, int)
            A tuple of values between 0 and 255 indicating the r, g, b value of the block color
        """
        self.head_position = head_position
        self.block_size = block_size
        self.block_colour = block_colour
        
        self.index = 0
        newbody_block = body_buildup(self.head_position, self.block_size, self.block_colour)
        self.body_list = [newbody_block]

    
    def move_left(self):
        '''This function moves the head position of the snake in the left direction'''       
        return self.move(-30,0)
    def move_right(self):
        '''This function moves the head position of the snake in the right direction'''
        return self.move(+30,0)
    def move_up(self):
        '''This function moves the head position of the snake in the up direction'''
        return self.move(0,-30)
    def move_down(self):
        '''This function moves the head position of the snake in the down direction'''
        return self.move(0,+30)
    
    def move(self,x,y):
        '''This function moves the head position of snake in different direction based on input'''
        temp = self.head_position
        starting_pos = (
            self.head_position[0]+x, self.head_position[1]+y)
        self.head_position = starting_pos
        self.body_list[0].head_position = starting_pos
        initial_head_pos = True
        for i in self:
            if initial_head_pos:
                initial_head_pos = False
                continue
            starting_pos = temp
            temp = i.head_position
            i.head_position = starting_pos


    def inside_bounds(self, cord_upperleft, cord_lowerright):
        '''This function is used to check if the Snake Object is inside bounds
        Parameters:
        ------------------------------------------
        cord_upperleft : tuple(int, int)
            The x- and y-coordinates for the top left corner of the bounds
        cord_lowerright : tuple(int, int)
            The x- and y-coordinates for the bottom right corner of the bounds
        Return :
            True: if snake is inside the provided bounds
            False: if not inside the provided bounds
        '''
        
        if ((cord_lowerright[0] - cord_upperleft[0] <= self.block_size[0]) or
            (cord_upperleft[0] >= self.head_position[0] + self.block_size[0])or
            (cord_upperleft[1] >= self.head_position[1] + self.block_size[1])or
            (cord_lowerright[0] <= self.head_position[0]) or
            (cord_lowerright[1] <= self.head_position[1])):
            return False
        return True


    def check_collision(self, cord_upperleft, shape_block):
        '''Function to check if any Block in the Snake Object collides with shape at the given coordinates and of given size
        Parameters:
        ------------------------------------------
        cord_upperleft : tuple(int, int)
            The x- and y-coordinates for the top left corner of the bound
        shape_block : tuple(int, int)
            The width and height of the shape

        Return :
            True: if any collision
            False: if no collision
        '''
        if ((self.head_position[0] <= cord_upperleft[0] <= self.head_position[0] + self.block_size[0]) and
                (self.head_position[0] <= cord_upperleft[0] + shape_block[0] <= self.head_position[0] + self.block_size[0]) and
                (self.head_position[1] <= cord_upperleft[1] <= self.head_position[1] + self.block_size[1]) and
                (self.head_position[1] <= cord_upperleft[1] + shape_block[1] <= self.head_position[1] + self.block_size[1])):
            return True
        return False

    def check_collision_with_fruit(self, cord_upperleft_fruits, shape_block_fruits):
        '''Function to check if any Block in the Snake Object collides with Fruit at the given coordinates and of given size
        Parameters:
        ------------------------------------------
        cord_upperleft_fruits : tuple(int, int)
            The x- and y-coordinates for the top left corner of the bound
        shape_block_fruits : tuple(int, int)
            The width and height of the object

        Return : 
            True: if any collision
            False: if no collision
        '''
        
        return self.check_collision(cord_upperleft_fruits, shape_block_fruits)

    def check_collision_with_self(self):
        '''Function to check if the head Block in the Snake Object collides with any other Block in the Snake Object
        Return :
            True: if any collision
            False: if no collision
        '''
        initial_head_pos = True
        for i in self:
            if initial_head_pos:
                initial_head_pos = False
                continue
            if self.check_collision(i.head_position, i.block_size):
                return True
            elif self.check_collision(i.head_position, i.block_size) == False:
                continue
        return False

    def grow(self):
        '''It will increases the size of the Snake by one Block object'''
        snake_growpart = body_buildup(
            self.head_position, self.block_size, self.block_colour)
        self.body_list.append(snake_growpart)

    def __len__(self):
        return len(self.body_list)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self) == self.index:
            self.index = 0
            raise StopIteration
        self.index += 1
        return self.body_list[self.index - 1]


class body_buildup:
    """
    A simple structure for a building block for a snake.

    Attributes:
    -----------
        snake_headpos_new : tuple(int, int)
            x and y coordinates for the top left corner of the block

        snake_size_new : tuple(int, int)
            The width and height of the block.

        new_snake_color : tuple(int, int, int)
            A tuple of values between 0 and 255 indicating the r, g, b value of the block color

    Methods:
    -----------------
        Getter function is used for getting coordinates, size and colour.
        """
    def __init__(self, snake_headpos_new, snake_size_new, snake_colour_new):
        """Initialize the block object. The parameters are passed on to the init function of Block

        Attributes:
    -----------
        snake_headpos_new : tuple(int, int)
            x and y coordinates for the top left corner of the block

        snake_size_new : tuple(int, int)
            The width and height of the block.

        snake_color_new : tuple(int, int, int)
            A tuple of values between 0 and 255 indicating the r, g, b value of the block color
        """
        self.head_position = snake_headpos_new
        self.block_size = snake_size_new
        self.block_colour = snake_colour_new

    def get_coordinates(self):

        """Get the coordinates value for snake.

        Return: tuple(int, int)
            x and y coordinates for the top left corner of the block
        """
        return self.head_position

    def get_size(self):
        """Get the size of the block.

        Return: tuple(int, int)
            The width and height of the block
        """
        return self.block_size

    def get_colour(self):
        """Get the color of the block.

        Return: tuple(int, int, int)
            A tuple of values between 0 and 255 indicating the r, g, b value of the block color
        """
        return self.block_colour
