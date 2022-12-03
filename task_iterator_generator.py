from types import GeneratorType


class FlatIterator:
    """Доработать класс FlatIterator. Должен получиться итератор, который принимает список списков и
    возвращает их плоское представление, т.е последовательность состоящую из вложенных элементов. Функция test в коде
    ниже также должна отработать без ошибок.
    """

    def __init__(self, list_of_list: list):
        self.source_list = list_of_list
        self.list_index = 0
        self.list_item_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.list_item_index == len(self.source_list[self.list_index]):
            self.list_index += 1
            self.list_item_index = 0
        if self.list_index == len(self.source_list):
            raise StopIteration
        value = self.source_list[self.list_index][self.list_item_index]
        self.list_item_index += 1
        return value


def flat_generator(matrix: list):
    """Доработать функцию flat_generator.
    Должен получиться генератор, который принимает список списков и возвращает их
    плоское представление. Функция test в коде ниже также должна отработать без ошибок.
    """
    for parent_list in matrix:
        for inner_list in parent_list:
            yield inner_list


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), GeneratorType)


# if __name__ == '__main__':
#     test_1()
#     test_2()
