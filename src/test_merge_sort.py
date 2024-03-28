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
        reverse_large_list = list(range(100000, 0, -1))
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

    def test_unsorted_multiple_indeces(self):
         array = [29, 72, 98, 13, 87, 66, 52, 51, 36, 21, 75, 4, 88, 58, 46, 31, 55, 74, 19, 8]
         sorted = [4, 8, 13, 19, 21, 29, 31, 36, 46, 51, 52, 55, 58, 66, 72, 74, 75, 87, 88, 98]
         self.assertListEqual(
             sorted,
             merge_sort(array)
         )
