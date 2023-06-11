import random


class Array:

    def __init__(self, capacity, fill_value=None):
        self.capacity = capacity
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __randomfill__(self):
        for i in range(self.__len__()):
            self.__setitem__(i, random.randint(0,100))
        return self.items
            
    
    def __sum__(self):
        return sum(self.items)


if __name__ == "__main__":
    menu = Array(5)
    print(menu)
    for i in range(menu.__len__()):
        menu.__setitem__(i, i+1)

    print(menu)

    for i in range(len(menu)):
        menu[i] = i+2

    print(menu)

    print(menu.__sum__())

    print(menu.__randomfill__())
