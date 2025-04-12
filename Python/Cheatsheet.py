# threading enables us to run codes simultaneously
# we don't need to wait for one line to finish before implement next lines
# don't use threading when unnecessary
import threading

class Messenger(threading.Thread):

    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = Messenger(name = 'Send out messages')
y = Messenger(name = 'Receive messages')
x.start()
y.start()


# unpacking lists
product = ['Dec 25,2014', 'gloves', 'Macy''s', 8.51]
date, item, location, price = ['Dec 25,2014', 'gloves', 'Macy''s', 8.51]

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    return avg
    
    
# Unpacking Arguments
def health_index(age, apple_eaten, cigar_smoken):
    answer = age + 0.3 * apple_eaten - 4 * cigar_smoken
    return answer

my_info = [21, 5, 1]
print(health_index(*my_info))


# zip function
first = ['Nicholas', 'aa', 'bb']
second = ['Han', 'AA', 'BB']
name = zip(first, second) # name is like [('Nicholas','Han'),('aa','AA'),('bb','BB')]
for a, b in name:
    print(a, b)


# lambda function
answer = lambda x: x*4
print(answer(1))


# functions on dictionaries
stock = {
    'GOOG': 520.45,
    'FB': 76.54,
    'YHOO': 38.29,
    'EDU': 123.32
}


# zip is sorted by the first value passed in
print(min(zip(stock.values(), stock.keys())))
sorted(zip(stock.values(), stock.keys()))


# Class
class Enemy:
    life = 3 # class variables are those whose values are the same across objects
    
    # like a constructor, or initializer list
    # any time we create an object, init is automatically called
    def __init__(self, dummy):
        self.dummy = dummy # instance variables are those whose values are different across objects
        
    def attack(self):  # keyword "self" is automatically filled
        print("ouch!")
        self.life -= 1  # keyword "self" is necessary

    def check_life(self):
        if self.life <= 0:
            print("I'm dead.")
        else:
            print(str(self.life) + "life left.")

enemy1 = Enemy(1)
enemy1.attack()
enemy1.check_life()


# class inheritance
class Parent:

    def print_last_name(self):
        print("Han")

class Child(Parent):

    def print_first_name(self):
        print("Zhenxiong")

    # overriding is okay
    def print_last_name(self):
        print("Nicholas")

me = Child()
me.print_first_name()
me.print_last_name()


# multiple inheritance
class Mom:
    def my_intelligence(self):
        print("I have intelligence.")

class Dad:
    def my_strength(self):
        print("I have strength.")

class Child(Mom, Dad):
    pass  # use this keyword if you just want to do nothing (like semicolon in C++)


# Download image
import random
import urllib.request

def download_image(url):
    name = random.randrange(1, 10000)
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url, fullname)


# Download files
from urllib import request
xdf_url = 'http://real-chart.finance.yahoo.com/table.csv?s=EDU&d=7&e=10&f=2015&g=d&a=8&b=15&c=2006&ignore=.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    fx = open(r'xdf.csv', 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()

download_stock_data(xdf_url)
