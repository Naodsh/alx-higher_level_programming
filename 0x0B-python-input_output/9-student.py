#!/usr/bin/python3
"""Module for student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """init function """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
