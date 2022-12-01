"""
Generator:
    Function is used to implement a generator.
    All the local variables before the yield function are stored.
    Generators are mostly used in loops to generate an iterator by returning all the values in the loop without
        affecting the iteration of the loop
    Generator uses yield keyword
    Every generator is an iterator
    Once calculated and used elements are not saved anywhere.
    Generator returns iterator, but the essence of the generator is that it can freeze work using yield and
    continues its work at the next call, saving the values of all local attributes
"""

from typing import Generator, Union, Iterator


# def countdown(n):
#     print("countdown")
#     while n > 0:
#         yield n  # returns n and "freezes" function
#         n -= 1   # When we call next()/__next__() we start from here(next line after yield)


# generator = countdown(10)
# print(generator.__next__())
# print(generator.__next__())
# print(next(generator))
# generator.close()  # Exits from generator(if u call it next time you'll get StopIteration error
# generator.throw(SomeException("error"))  # Raises Exception

# for i in countdown(10):
#     print(i)


def file_reader_generator(file_path: str) -> Generator:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if not line:
                continue
            yield line


def grep(source: Union[Generator, Iterator], search_text: str) -> Generator:
    counter = 1
    for inner_text in source:
        if search_text in inner_text:
            yield f"\033[92m{search_text} Found in line {counter}"
            counter += 1
            continue
        yield f"\033[91m{search_text} not found in line {counter}"
        counter += 1


text_generator = file_reader_generator("test_data/source.txt")
searcher = grep(text_generator, "Date")
