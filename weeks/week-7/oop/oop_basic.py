# 1. Define a class. Write a class Dog with an __init__ that stores a name , and a method bark()
# that returns "<name> says woof" 

class Dog:
    """
    class for dogs 
    
    """
    def __init__(self, name:str):
        self.name =  name

    def bark(self):
        return f'{self.name} says woof'
    

# 2. Two attributes. Write a class Rectangle whose __init__ takes width and height , and a
# method area() that returns their product.

class Rectangle:
    def __init__(self,width, hight):
        self.width = width 
        self.hight = hight
    
    def area(self):
        return self.width * self.hight
    

# 3. Default value. Write a class Counter that starts at 0 (or at a given start value), with
# increment() and a value() method.


class Counter:
    def __init__(self, value = 0):
        self.value = value

    def increment(self):
        self.value += 1



# 4. String representation. Add a __str__ method to a Point class so that print(Point(1, 2))
# shows (1, 2)

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'
    

# 5. Bank account. Write a class BankAccount with a balance (default 0 ), and methods
# deposit(amount) and withdraw(amount) . Withdrawing more than the balance should leave
# the balance unchanged.

class BankAccount:
    """
    class to  mannge bank accounts 
    
    """
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self,amount):
        if amount > self.balance:
            return
        else:
            self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount

    
# 6. Update state. Write a class Temperature that stores a value in Celsius and has a method
# to_fahrenheit() returning the converted value.

class Temperature:
    def __init__(self , temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 9/5) + 32
    

# 7. Class attribute. Write a class Student where every instance shares a class attribute
# school = "Kodcode" , and each has its own name . Show that changing one student's name
# does not affect another's.

class Student:
    school = 'Kodcode'
    
    def __init__(self, name:str):
        self.name = name


# 8. Count instances. Write a class Player that uses a class attribute to count how many Player
# objects have been created so far.


class Player:
    counter_players = 0

    def __init__(self):
        Player.counter_players += 1


#9. Compare objects. Write a class Money with an amount , and a method is_more_than(other)
# that returns whether this object's amount is larger than another Money object's

class Money:
    def __init__(self, amount):
        self.amount = amount

    def __gt__(self,other):
        return other.amount < self.amount
    
    
# 10. A small model. Write a class Playlist that stores a list of song titles. Provide add(title) ,
# remove(title) , and count() methods, and a __str__ that lists the songs.

class Playlist:
    def __init__(self):
        self.playlist = []

    def __add__(self, item):
        self.playlist.append(item)
        return self

    def __str__(self):
        return str(self.playlist)

    def __len__(self):
        return len(self.playlist)
    

p1 = Playlist()
p1 = p1 + 'pink moon'
p1 += 'hellp'
print(type(p1))
print(p1)

