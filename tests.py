import unittest
from data_decipher import Processor


class Tests(unittest.TestCase):
    def test_data_dict(self):
        data_path = "data_decipher/names/"
        data_dict = Processor.GetFilesTextData(data_path)
        self.assertEqual(
            Processor.GetFilesTextData(data_path),
            data_dict,
        )

    def test_search_totals(self):
        # [name: string, year: int, gender: string, ppl_born: float]
        data_list = [
            ["test_name", 1994, "M", 200.0],
            ["test_name", 1990, "F", 400.0],
            ["test_name", 1980, "F", 350.0],
        ]

        totals_dict = Processor.GetSearchTotals(data_list)

        self.assertEqual(totals_dict["total"], 950)
        self.assertEqual(totals_dict["males"], 200)
        self.assertEqual(totals_dict["females"], 750)


if __name__ == "__main__":
    unittest.main()