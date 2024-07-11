from classes import Car, Book, Stadium

test_car = Car("BMW", "M5", 1000)
test_book = Book("Горе от ума", 1825, "А. С. Грибоедов")
test_stadium = Stadium(81000, 221000, "Лужники")
choice = input("save или pkl или json\n")

if choice == "save":
    test_car.save_pkl()
    test_car.save_json()
    test_book.save_pkl()
    test_book.save_json()
    test_stadium.save_pkl()
    test_stadium.save_json()
elif choice == "pkl":
    test_car.load_pkl()
    print(test_car.__dict__)
    input()
    test_book.load_pkl()
    print(test_book.__dict__)
    input()
    test_stadium.load_pkl()
    print(test_stadium.__dict__)
elif choice == "json":
    test_car.load_json()
    print(test_car.__dict__)
    input()
    test_book.load_json()
    print(test_book.__dict__)
    input()
    test_stadium.load_json()
    print(test_stadium.__dict__)
