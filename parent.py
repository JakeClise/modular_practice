#This file will be and will hold the parent
local_val = "Starbucks Coffees"

def square(x):
    return x * x

class User:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        return 'Hello!'

print(square(9))
user = User("Jesse")
print(user.name)
print(user.say_hello())

print(__name__)

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("the file is being executed because it is imported by another file. The file is called: ", __name__)
    
