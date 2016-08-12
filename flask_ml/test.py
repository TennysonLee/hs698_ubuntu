import unittest
from api.views import get_data, pca_var
import numpy as np
from fun_things import add
from numpy.testing import assert_array_almost_equal


class TestNumComponentsReturned(unittest.TestCase):

    def test_add(self):
        res = add(3, 4)
        self.assertEqual(res, 7)

    def test_add_fails_when_input_is_string(self):
        with self.assertRaises(TypeError):
            add(3, 'hello')

    def test_numpy_array_almost_equal(self):
        arr1 = np.array([0.0, 0.10000000, 0.15])
        arr2 = np.array([0.0, 0.10000089, 0.15])
        assert_array_almost_equal(arr1, arr2, decimal=6)

class TestSomeOtherThing(unittest.TestCase):

    def test_something_else(self):
        pass













# class TestVariancePCA(unittest.TestCase):
#
#     def setUp(self):
#         """Function to run before each test."""
#         self.df = get_data()
#
#     def test_example(self):
#         self.assertEqual(1, 1)
#
#     def test_return_types(self):
#         variance_required = 0.90
#         pcs, required_components = pca_var(self.df, var=variance_required)
#         self.assertEqual(type(required_components), int)
#         self.assertEqual(type(pcs), np.ndarray)

    # def test_number_of_components_determined(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_number_of_pcs_matches_number_of_components_determined(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     check that s.split fails when the separator is not a string
        # with self.assertRaises(TypeError):
        #     s.split(2)


if __name__ == '__main__':
    unittest.main()
