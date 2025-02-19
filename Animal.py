class Animal:
    def __init__(self, name, species, color, size, weight, owner): 
        self.__name = name
        self.__species = species
        self.__color = color
        self.__size = size
        self.__weight = weight
        self.__owner = owner
        print("hello, i am", self.__name)
        print( "I am a", self.__species)
        print( "My color is", self.__color)
        print( "My size is", self.__size)
        print("My weight is", self.__weight)
        print("My owner is", self.__owner)
        
    def noise(self, noise):
        self.__noise = noise
        print("My noise goes", self.__noise)

    def jump(self, jump):
        self.__jump = jump
        print("I can jump", self.__jump)

    def playstyle(self, playstyle):
        self.__playstyle = playstyle
        print("I like to play", self.__playstyle)

    def skin(self, skin):
        self.__skin = skin
        print("My skin is", self.__skin)

    def age(self, age):
        self.__age = age
        print("I am ", self.__age, "years old")

