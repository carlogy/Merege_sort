import unittest
import random

from merge_sort import(
    merge_sort,
    merge
)

class TestMergeSort(unittest.TestCase):
    def test_sorted_list(self):
        array = array = [1,2,3,4,5,6,7,8,9]
        self.assertListEqual(
            array,
            merge_sort(array)
        )

    def test_sorting_first_digit(self):
        unsorted_array = [9,2,3,4,5,6,7,8,1]
        sorted_array = [1,2,3,4,5,6,7,8,9]
        self.assertListEqual(
            sorted_array,
            merge_sort(unsorted_array)
        )

    def test_empty_array(self):
        array = []
        self.assertListEqual(
            array,
            merge_sort(array)
        )

    def test_reverse_order(self):
        reverse_large_list = list(range(1000000, 0, -1))
        self.assertListEqual(
            sorted(reverse_large_list),
            merge_sort(reverse_large_list)
        )

    def test_empty_list(self):
        array = []
        self.assertListEqual(
            array,
            merge_sort(array)
        )


    def test_large_unsorted_list(self):
        array = list(range(0, 1000000))
        random.shuffle(array)

        self.assertListEqual(
            sorted(array),
            merge_sort(array)
        )
if __name__ == '__main__':
    unittest.main()
