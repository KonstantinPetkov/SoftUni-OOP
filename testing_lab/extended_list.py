class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)

import unittest

class ListTests(unittest.TestCase):

    def setUp(self) -> None:
        self.list = IntegerList(1, 3, 4, 5, "3", False)

    def test_if_get_data(self):
        expected_result = [1, 3, 4, 5]
        self.assertEqual(self.list.get_data(), expected_result)

    def test_if_add_invalid_input(self):
        with self.assertRaises(ValueError) as context:
            self.list.add("3")
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_if_add_valid_input(self):
        expected_result = [1, 3, 4, 5, 6]
        self.assertEqual(self.list.add(6), expected_result)

    def test_remove_if_index_is_out_of_range(self):
        with self.assertRaises(IndexError) as context:
            self.list.remove_index(4)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_remove_if_index_is_in_range(self):
        result = self.list.remove_index(2)
        self.assertEqual(result, 4)

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.list.get(4)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_get_valid_index(self):
        result = self.list.get(1)
        self.assertEqual(result, 3)

    def test_insert_invalid_index(self):
        with self.assertRaises(IndexError) as context:
            self.list.insert(7, 5)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_invalid_input(self):
        with self.assertRaises(ValueError) as context:
            self.list.insert(1, "7")
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_insert_valid_index_in_range_and_valid_input(self):
        self.list.insert(2, 9)
        self.assertEqual(self.list.get_data(), [1, 3, 9, 4, 5])

    def test_get_biggest(self):
        result = self.list.get_biggest()
        self.assertEqual(result, 5)

    def test_get_index(self):
        result = self.list.get_index(1)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()