#!/usr/bin/python3
""" Base Class Module """


import json
import turtle
import csv


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init Function """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @staticmethod
    def draw(list_rectangles, list_squares):
        screen = turtle.Screen()
        screen.title("Shapes Drawing")

        pen = turtle.Turtle()

        for rectangle in list_rectangles:
            pen.penup()
            pen.goto(rectangle.x, rectangle.y)
            pen.pendown()
            for _ in range(2):
                pen.forward(rectangle.width)
                pen.left(90)
                pen.forward(rectangle.height)
                pen.left(90)
        
        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        turtle.done()

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square instance
        else:
            return None

        dummy_instance.update(**dictionary)  # Update with provided dictionary
        return dummy_instance

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_list = cls.to_json_string(dict_list)
        with open(cls.__name__ + ".json", mode='w', encoding='utf-8') as file:
            file.write(json_list)

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                data = file.read()
                if not data:
                    return []
                dict_list = cls.from_json_string(data)
                return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        instance_list = []
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(
                            int(row[1]), int(row[2]), int(row[3]),
                            int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(
                            int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                    instance_list.append(instance)
        except FileNotFoundError:
            pass
        return instance_list
