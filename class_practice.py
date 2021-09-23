import numpy as nm
from sklearn.model_selection import train_test_split


class hola:

    hlw = "hello"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def dekhao(self):
        print(self.name, "," , self.age)


def main():
    notun = hola("Tonmoy", "Nai")
    print( notun.hlw, notun.dekhao() )


if __name__ == "__main__":
    main()
