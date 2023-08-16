import random
import dictionary_creatures

def Nickname():
    pass

def Generator():
    n = dictionary_creatures.name
    a = dictionary_creatures.alligment
    l = dictionary_creatures.sizeAndhitpoints
    e = dictionary_creatures.elements
    key, value = random.choice(list(l.items()))
    print(f"Name: {random.choice(n)}")
    print(f"Size: {key}")
    print(f"Hitpoints: {value}")
    print(f"Element: {random.choice(e)}")
    print(f"Alligment: {random.choice(a)}")

def Opt():
    return str(input("Would You like to Generate RPG Sttufs?(y/n): "))

opt = Opt()
while(True):
    if (opt == 'y'):
        count = int(input("How Many creatures would you like to generate: "))
        for i in range(count):
            Generator()
            print("//////////////////////////////////////////")
        opt = Opt()
    else:
        exit()