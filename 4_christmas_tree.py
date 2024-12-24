from random import choice

class cristmasTree:
    def __init__(self, height: int, lights=False, balls=False) -> None:
        '''Initialize the tree with height, lights and balls'''
        self.__height = height
        self.__lights = lights
        self.__balls = balls

    def __str__(self) -> str:
        '''Return the string representation of the tree'''
        return self.star() + self.layers() + self.bottom() + self.trunk()

    def star(self) -> str:
        '''Return the star of the tree'''
        return ' ' * self.__height + '*\n'

    def layers(self) -> str:
        '''Return the layers of the tree'''
        levels = ''
        decorations = [' '] * 3 + ['.'] * self.__lights + ['o'] * self.__balls
        for i in range(1, self.__height):
            decoration = ''.join([choice(decorations) for _ in range(2 * i - 1)])
            levels += ' ' * (self.__height - i) + '/' + decoration + '\\\n'
        return levels

    def bottom(self) -> str:
        '''Return the bottom of the tree'''
        return '/' + '~' * (2 * self.__height - 1) + '\\\n'
    
    def trunk(self) -> str:
        '''Return the trunk of the tree'''
        return ' ' * (self.__height - 1) + '| |\n'


height = choice(range(3, 20))               # random height
boolean = True, False                       # tuple unpacking
lights = choice(boolean)                    # random lights
balls = choice(boolean)                     # random balls
tree = cristmasTree(height, lights, balls)  # create a tree
print(tree)