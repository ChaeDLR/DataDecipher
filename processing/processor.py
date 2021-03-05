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

                except:
                    print(f"Failed to load the file {fileName}")

            file.close()
            return fileDataDict

        except:
            print(f"Failed to get path files {path}.")

    @staticmethod
    def SearchData(searchStr: str, dataDict: dict, yearFilter=0) -> list:
        """ Search a dict for the searchStr arg """

        matchesList = []
        match_finds = 0

        for dataList in dataDict:
            for dataStr in dataDict[dataList]:

                split_string = dataStr.split(",")

                if split_string[0] == searchStr:

                    year = dataList[3:7]
                    name = split_string[0]
                    gender = split_string[1]
                    num_ppl_born = split_string[2]

                    if yearFilter == 0 or year == str(yearFilter):
                        matchesList.append([name, year, gender, num_ppl_born])
                        match_finds += 1

        return matchesList
