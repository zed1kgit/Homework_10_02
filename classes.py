import json
import pickle


class Car:
    def __init__(self, brand, model, mileage):
        self.brand = brand
        self.model = model
        self.mileage = mileage

    def get_mileage(self):
        return self.mileage

    def get_full_name(self):
        return f"Машина {self.model}, марки {self.brand}"

    def save_pkl(self):
        with open(r'saved_data\car_data.pkl', 'wb') as file:
            pickle.dump(self.__dict__, file)
        return "Файл car_data.pkl создан"

    def load_pkl(self):
        with open(r'saved_data\car_data.pkl', 'rb') as file:
            loaded_data = pickle.load(file)
            self.__dict__ = loaded_data
        return f"Данные из файла записаны: {loaded_data}"

    def save_json(self):
        with open(r'saved_data\car_data.json', 'w', encoding='utf-8') as fh:
            json.dump(self, fh, cls=CarEncoder, ensure_ascii=False, indent=2)
        return "Файл создан"

    def load_json(self):
        with open(r'saved_data\car_data.json', 'r', encoding='utf-8') as fh:
            loaded_data = json.load(fh)
            self.brand = loaded_data["Brand"]
            self.model = loaded_data["Model"]
            self.mileage = loaded_data["Mileage"]
        return f"Данные из файла записаны: {loaded_data}"


class CarEncoder(json.JSONEncoder):
    def default(self, o):
        return {
            "Brand": o.brand,
            "Model": o.model,
            "Mileage": o.mileage,
            "Methods": {
                "Get_full_name": o.get_full_name(),
                "Get_mileage": o.get_mileage()
            },
            "ClassName": o.__class__.__name__
        }


class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author

    def __str__(self):
        return f'{self.title} {self.year} г.'

    def get_author(self):
        return self.author

    def save_pkl(self):
        with open(r'saved_data\book_data.pkl', 'wb') as file:
            pickle.dump(self.__dict__, file)
        return "Файл book_data.pkl создан"

    def load_pkl(self):
        with open(r'saved_data\book_data.pkl', 'rb') as file:
            loaded_data = pickle.load(file)
            self.__dict__ = loaded_data
        return f"Данные из файла записаны: {loaded_data}"

    def save_json(self):
        with open(r'saved_data\book_data.json', 'w', encoding='utf-8') as fh:
            json.dump(self, fh, cls=BookEncoder, ensure_ascii=False, indent=2)
        return "Файл создан"

    def load_json(self):
        with open(r'saved_data\book_data.json', 'r', encoding='utf-8') as fh:
            loaded_data = json.load(fh)
            self.title = loaded_data["Title"]
            self.year = loaded_data["Year"]
            self.author = loaded_data["Author"]
        return f"Данные из файла записаны: {loaded_data}"


class BookEncoder(json.JSONEncoder):
    def default(self, o):
        return {
            "Title": o.title,
            "Year": o.year,
            "Author": o.author,
            "Methods": {
                "__str__": o.__str__(),
                "Get_author": o.get_author()
            },
            "ClassName": o.__class__.__name__
        }


class Stadium:
    def __init__(self, people, area, name):
        self.people = people
        self.area = area
        self.name = name

    def get_name(self):
        return self.name

    def get_info(self):
        return f"Стадион площадью {self.area}, вмещает {self.people} людей"

    def save_pkl(self):
        with open(r'saved_data\stadium_data.pkl', 'wb') as file:
            pickle.dump(self.__dict__, file)
        return "Файл stadium_data.pkl создан"

    def load_pkl(self):
        with open(r'saved_data\stadium_data.pkl', 'rb') as file:
            loaded_data = pickle.load(file)
            self.__dict__ = loaded_data
        return f"Данные из файла записаны: {loaded_data}"

    def save_json(self):
        with open(r'saved_data\stadium_data.json', 'w', encoding='utf-8') as fh:
            fh.write(JSONDataAdapter.to_json(self))
        return "Файл создан"

    def load_json(self):
        with open(r'saved_data\stadium_data.json', 'r', encoding='utf-8') as fh:
            loaded_data = JSONDataAdapter.from_json(fh.read()).__dict__
            self.__dict__ = loaded_data
        return f"Данные из файла записаны: {loaded_data}"


class JSONDataAdapter:
    @staticmethod
    def to_json(obj):
        if isinstance(obj, Stadium):
            return json.dumps({
                "people": obj.people,
                "area": obj.area,
                "name": obj.name
            }, ensure_ascii=False, indent=2)

    @staticmethod
    def from_json(obj_json_str):
        obj_python_dict = json.loads(obj_json_str)
        try:
            stadium = Stadium(obj_python_dict['people'], obj_python_dict['area'], obj_python_dict['name'])
            return stadium
        except AttributeError:
            print("Неверная структура!")
