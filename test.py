import unittest, io, csv
from csv2dictionary.csvpro import CsvBrain


class Test_Main(unittest.TestCase):
    """main test case"""

    def test_convert(self):
        case1_key = [
            {
                'first': 'cole',
                'last': 'malphrus',
                'age': '25'
            },
            {
                'first': 'kristin',
                'last': 'malphrus',
                'age': '23'
            },
            {
                'first': 'effie',
                'last': 'malphrus',
                'age': '0'
            }
        ]
        case1 = CsvBrain('test.csv')
        for index in range(len(case1_key)):
            self.assertDictEqual(case1.dict[index], case1_key[index])

    def test_search(self):
        case2_key = [
            {
                'first': 'effie',
                'last': 'malphrus',
                'age': '0'
            }
        ]
        case2 = CsvBrain('test.csv')
        self.assertEqual(case2.search('effie'), case2_key)
        

if __name__ == "__main__":
    unittest.main()