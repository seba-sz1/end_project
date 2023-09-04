"""Napisz funkcję flatten_list która będzie przyjmować listę, elementem listy może być kolejna lista, lub integer i
chodzi o to, żeby zwrócić listę która będzie zawierać jedynie integery, przykładowo
jak funkcja przyjmie taką listę [1, 2, [3, 4, [5], [6]], 7, 8, 9] to ma zwrócić [1, 2, 3, 4, 5, 6, 7, 8, 9]"""


def flatten_list(lst):
    end_list = []
    for i in lst:
        if type(i) is int:
            end_list.append(i)
        elif type(i) is list:
            end_list += flatten_list(i)
    return end_list

# list1 = [1, 2, [3, 4, [5], [6]], 7, 8, 9]
# list2 = flatten_list(list1)
# print(list2)