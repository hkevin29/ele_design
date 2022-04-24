import os
import random
import blue
import purple

def main():
    a= random.choice([1,2])
    print(a)
    if a == 1:
        blue.main()
    else:
        purple.main()


main()


