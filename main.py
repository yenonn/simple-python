from math import add, substraction, multiplication, division
from hello import print_hello
from my_list import give_me_a_list
from my_dict import give_me_a_string_dict, give_me_a_int_dict

def print_dict(dict: dict) -> None:
    for k, v in dict.items():
        print(k, v)

def print_list(list: list) -> None:
    for number in list:
        print(number)

if __name__ == "__main__":
    dict1 = give_me_a_string_dict()
    dict_int = give_me_a_int_dict()
    list1 = give_me_a_list()

    print_dict(dict1)
    print_dict(dict_int)
    print_list(list1)

    # print("Hello, World!")
    # list_numbers = [(1, 2), (3, 4), (5, 6),(7, 8)] # []list, ()tuple, {"k": "v"}dict {1,2,3}set
    # for index in range(len(list_numbers)):
    #     if index % 2 != 0:
    #         number1, number2 = list_numbers[index]
    #         print_hello(f"{number1} + {number2} = {add(number1, number2)}")
    #         print_hello(f"{number1} - {number2} = {substraction(number1, number2)}")
    #         print_hello(f"{number1} * {number2} = {multiplication(number1, number2)}")
    #         print_hello(f"{number1} / {number2} = {division(number1, number2)}")

    # for number1, number2 in list_numbers:
    #     print_hello(f"{number1} + {number2} = {add(number1, number2)}")
    #     print_hello(f"{number1} - {number2} = {substraction(number1, number2)}")
    #     print_hello(f"{number1} * {number2} = {multiplication(number1, number2)}")
    #     print_hello(f"{number1} / {number2} = {division(number1, number2)}")
