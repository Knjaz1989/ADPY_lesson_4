from datetime import datetime
from pprint import pprint

def logger(path: str):
    def wrapper(old_func):
        def new_func(*args, **kwargs):
            time = str(datetime.now())
            cook_book = old_func(*args, **kwargs)
            name = old_func.__name__
            arguments = (args, kwargs)
            return_value = cook_book
            with open(path, 'w', encoding='utf-8') as file:
                file.write(time + '\n')
                file.write(name + '\n')
                file.write(str(arguments) + '\n')
                file.write(str(return_value))
            return cook_book
        return new_func
    return wrapper

@logger(path='info.txt')
def get_cook_book(path_to_file):
    cook_book = {}
    with open(path_to_file, "r", encoding="utf-8") as file:
        for line in file:
            name = line.strip()
            items_list = []
            total_items = int(file.readline())
            for items in range(total_items):
                ingredient_name, quantity, measure = file.readline().strip().split("|")
                items_list.append({"ingredient_name": ingredient_name.strip(), "quantity": int(quantity),
                                   "measure": measure.strip()})
            cook_book[name] = items_list
            file.readline()
    return cook_book

if __name__ == '__main__':
    pprint(get_cook_book("recipes.txt"))