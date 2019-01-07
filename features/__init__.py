from aloe import before, step, world
from sodam import SodaMachine

@before.each_example
def clear(*args):
    world.sodam = SodaMachine()
    world.returned = SodaMachine()

@step('(\d+) coins are added')
def addCoins(self, amount):
    amount = int(amount)
    for i in range(0, amount):
        world.sodam.add50c()

@step('I withdraw a soda')
def drawSoda(self):
    world.sodam.draw()

@step('I receive a soda')
def receiveSoda(self):
    assert world.sodam.canWithDraw() == False, \
      "Soda received"

@step('I receive coins')
def receiveCoins(self):
    world.sodam.return50cs() 

@step('I withdraw (\d+) soda; (\d+) fruits')
def withdraw1(self, soda, fruits):
    soda = int(soda)
    fruits = int(fruits)
    world.sodam.draw(True, False, False, True)

@step('I withdraw (\d+) fruits; (\d+) muesli')
def withdraw2(self, fruits, muesli):
    fruits = int(fruits)
    muesli = int(muesli)
    world.sodam.draw(False, True, False, True)

@step(r'I receive (\d+) soda; (\d+) fruit')
def receive2(self, soda, fruit):
    sodas = int(soda)
    fruits = int(fruit)
    assert sodas == world.sodam.getSodas() and fruits == world.sodam.getFruits(), \
      "received uneven2"

@step('I receive (\d+) fruit; (\d+) muesli')
def receive1(self, fruit, muesli):
    fruit = int(fruit)
    muesli = int(muesli)
    assert fruit == world.sodam.getFruits() and not muesli != world.sodam.getMueslis(), \
      "received uneven1"

@step('I can withdraw (\d+) soda; (\d+) muesli; (\d+) nuts; (\d+) fruits')
def canWithdraw(self, soda, muesli, nuts, fruits):
    soda = int(soda) and True or False
    muesli = int(muesli) and True or False
    nuts = int(nuts) and True or False
    fruits = int(fruits) and True or False

    assert world.sodam.canWithDraw(soda, muesli, nuts, fruits) == True

@step('I return coins')
def returnCoins(self):
    world.returned = world.sodam.return50cs()

@step('I receive coins')
def receiveCoins(self):
    assert world.sodam.canWithDraw() == False and not world.returned == 0
