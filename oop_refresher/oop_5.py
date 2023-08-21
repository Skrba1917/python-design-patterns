from abc import ABC, abstractmethod
from typing import Type


class MyInterface(ABC):
    @abstractmethod
    def my_method(self):
        pass


class MyClass(MyInterface):
    def my_method(self):
        print("my_method implementation in MyClass")


class AnotherClass(MyInterface):
    def my_method(self):
        print("my_method implementation in AnotherClass")


class NotImplementingInterface:
    def some_method(self):
        print("I am not implementing an interface")


def process_my_interface(obj: MyInterface):
    obj.my_method()
    print("The object has correctly implemented MyInterface")


my_obj = MyClass()
process_my_interface(my_obj)

another_obj = AnotherClass()
process_my_interface(another_obj)

not_implementing_interface = NotImplementingInterface()
process_my_interface(not_implementing_interface)
