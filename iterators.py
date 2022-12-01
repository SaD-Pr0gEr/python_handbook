"""
An iterable is an object that has an __iter__ method which returns an iterator, or which defines a __getitem__
method that can take sequential indexes starting from zero (and raises an IndexError when the indexes are no
longer valid). So an iterable is an object that you can get an iterator from.
An iterator is an object with a next (Python 2) or __next__ (Python 3) method.
Iterator:
    Class is used to implement an iterator
    Iterators are used mostly to iterate or convert other objects to an iterator using iter() function.
    Iterator uses iter() and next() functions(or __iter__/__next__ method)
    Every iterator IS NOT a generator
    Once calculated and used elements are not saved anywhere.
    __iter__ is just for "for"-loop, u can use only __next__ to iterate in iterable object
    (but u always use for-loop, because it's comfortable ;))
"""


# import time

# import requests
# from bs4 import BeautifulSoup


class MyUselessIterableDataStructure:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        self.counter = 0

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter > 1:
            raise StopIteration
        value = self.value1 if self.counter == 0 else self.value2
        self.counter += 1
        return value


# for i in MyUselessIterableDataStructure(1, 2):
#     print(i)


class MyArray:

    def __init__(self, *values: int):
        self.check_data_type(*values)
        self.data = values
        self.index = 0

    @staticmethod
    def check_data_type(*values):
        for data in values:
            if not isinstance(data, int):
                raise ValueError(f"Expected 'int': Got '{type(data).__name__}'")

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


# for i in MyArray(1, 2, 3, 4, 5, True):
#     print(i)


# print(MyArray(1, 2).__next__())  # U can define and __next__()/next() without defining
# __iter__ on class, cause __iter__ is just for "for" loop


class MyRange:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.counter = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.end:
            raise StopIteration
        value = self.counter
        self.counter += 1
        return value

    def __str__(self):
        return f"MyRange({self.start}, {self.end})"

    def __repr__(self):
        return f"MyRange({self.start}, {self.end})"


# print(MyRange(20, 30))
# for i in MyRange(10, 20):
#     print(i)


# for i in requests.get("https://habr.com").iter_lines():
#     print(i.decode("utf-8"))

# requests.Response.iter_lines() returns an iterator that iterates through the rows of content


# print(requests.get("https://habr.com").text.__sizeof__())
# counter = 0
# for i in requests.get("https://habr.com", stream=True).iter_lines(chunk_size=300):
#     print(i.decode("utf-8"), "end!!!")
# counter += i.decode("utf-8").__sizeof__()
# print(counter)


# class NoEffectiveGithubParserIterator:
#     """Yes, it's iterator, but code logic is no effect"""
#     target_url = "https://github.com/SaD-Pr0gEr?tab=repositories"
#
#     def __init__(self):
#         self.iter_content = requests.get(self.target_url, stream=True).iter_lines()
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         content = BeautifulSoup(
#             next(self.iter_content).decode("utf-8"),
#             "html.parser"
#         )
#         repo_obj = content.find("a", attrs={"itemprop": "name codeRepository"})
#         return f'https://github.com{repo_obj["href"]}' if repo_obj else None
#
#
# for data in NoEffectiveGithubParserIterator():
#     if data: print(data)

# def for_loop(iterable, loop_body_func):
#     iterator = iter(iterable)
#     next_element_exist = True
#     while next_element_exist:
#         try:
#             element_from_iterator = next(iterator)
#         except StopIteration:
#             next_element_exist = False
#         else:
#             loop_body_func(element_from_iterator)


# something = iter([1, 2, 3])
#
# for i in something:  # it works
#     print(i)
#
#
# for i in something:  # it'll not work, cause iter() returns 1 iterator, we used it before,
#     # for every iterating we should generate new iterator with iter()
#     print(i)
