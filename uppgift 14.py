FRUITS = ['banana', 'apple', 'orange']
CARS = ['volvo', 'ford', 'tesla']
ANIMALS = ['whale', 'cat', 'dog', 'cow']


def run():
    basket = [
        'volvo', 'is', 'an', 'orange', 'apple', 'cat'
    ]
    cars = []
    fruits = []
    animals = []
    rest = []
    for item in basket:
        if item in CARS:
            cars.append(item)
        elif item in FRUITS:
            fruits.append(item)
        elif item in ANIMALS:
            animals.append(item)
        else:
            rest.append(item)

    write_things(cars, 'Cars')
    write_things(fruits, 'Fruits')
    write_things(rest, 'Misc')
    write_things(animals, "Animals")


def write_things(items, kind):
    print(f"{kind.upper()}  ({len(items)}st)")
    for item in items:
        print(f" {item}")


if __name__ == '__main__':
    run()

