#define name keyword->class name->Cat
class Cat:
# variable ->species 
    species = 'mammal'

    # Constructor!
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # name and age are being passed as parameters. 
        # self always has to be in the contructor
        # self is pointing back to itself. 
    def describe(self):
        return "%s is %d years old." %(self.name, self.age)

guster = Cat("Guster", 11)
bandit = Cat("Bandit", 11)
# ******************************************************************************************
#print("%s is %d years old." % (guster.name, guster.age))
#print("%s is a %s" % (guster.name, guster.species))    
#print("%s is %s's sister, they are both %s(s)" % (bandit.name, guster.name, bandit.species))
# print statements commented out to show examples of methods
#********************************************************************************************

print(guster.describe())
print(bandit.describe())