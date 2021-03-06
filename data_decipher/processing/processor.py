import os
import copy


class Processor:
    @staticmethod
    def GetFilesTextData(path: str) -> dict:
        """ get all of the file names in a list """
        try:
            file_names: list = os.listdir(path)

            fileDataDict: dict = {}
            fileDataList: list = []

            for fileName in file_names:
                try:
                    with open(f"{path}/{fileName}", "r") as file:
                        for line in file.readlines():
                            fileDataList.append(line)
                        fileDataDict[fileName[0:7]] = copy.deepcopy(fileDataList)
                        fileDataList = []

                except IOError:
                    print(f"Failed to load the file {fileName}")

            file.close()
            return fileDataDict

        except IOError:
            print(f"Failed to get path files {path}.")

    @staticmethod
    def GetSearchTotals(dataList: list) -> dict:
        """ Takes a data list from the SearchData methods and get the totals """

        total_born = 0
        males_born = 0
        females_born = 0
        earliest_year = 0
        latest_year = 0

        for i in range(len(dataList)):
            matches = dataList[i]
            total_born += int(matches[3])
            if matches[2] == "M":
                males_born += int(matches[3])
            elif matches[2] == "F":
                females_born += int(matches[3])

            if matches[1] < earliest_year or earliest_year == 0:
                earliest_year = matches[1]
            elif matches[1] > latest_year:
                latest_year = matches[1]

        return {
            "total": total_born,
            "males": males_born,
            "females": females_born,
            "range": f"{earliest_year}-{latest_year}",
        }

    @staticmethod
    def SearchData(searchStr: str, dataDict: dict, yearFilter=0) -> list:
        """ Search a dict for the searchStr arg """

        matchesList = []
        match_finds = 0

        for dataList in dataDict:
            for dataStr in dataDict[dataList]:

                split_string = dataStr.split(",")

                if split_string[0] == searchStr:

                    year = int(dataList[3:7])
                    name = split_string[0]
                    gender = split_string[1]
                    num_ppl_born = float(split_string[2])

                    if yearFilter == 0 or year == yearFilter:
                        matchesList.append([name, year, gender, num_ppl_born])
                        match_finds += 1

        return matchesList
