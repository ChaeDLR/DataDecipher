import unittest

from data_decipher import Processor


class DataProcessTests(unittest.TestCase):
    def setUp(self):
        self.data_path: str = "data_decipher/names/"
        self.data_dict = Processor.GetFilesTextData(self.data_path)
        return super().setUp()

    def test_data_dict(self):
        data_dict: dict = Processor.GetFilesTextData(self.data_path)
        self.assertCountEqual(
            Processor.GetFilesTextData(self.data_path),
            data_dict,
        )

    def test_search_totals(self):
        # [name: string, year: int, gender: string, ppl_born: float]
        data_list: list = [
            ["test_name", 1994, "M", 200.0],
            ["test_name", 1990, "F", 400.0],
            ["test_name", 1980, "F", 350.0],
        ]

        totals_dict: dict = Processor.GetSearchTotals(data_list)

        self.assertEqual(totals_dict["total"], 950)
        self.assertEqual(totals_dict["males"], 200)
        self.assertEqual(totals_dict["females"], 750)

    def test_search_data(self):
        matches_list: list = Processor.SearchData("Chae", self.data_dict)
        for i in range(len(matches_list)):
            self.assertEqual("Chae", matches_list[i][0])

        matches_list: list = Processor.SearchData("Acacia", self.data_dict)
        for i in range(len(matches_list)):
            self.assertEqual("Acacia", matches_list[i][0])
