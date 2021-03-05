from processing.processor import Processor
from user_interface.ui import UserInterface
from graph.stat_graph import DataGraph

if __name__ == "__main__":

    names_path = "./names/"

    dataDict = Processor.GetFilesTextData(names_path)

    while True:
        selection = UserInterface.MainMenu()

        if selection == 1:
            usersInput = UserInterface.GetUserInput()

            matches_list = Processor.SearchData(usersInput[0], dataDict, usersInput[1])

            UserInterface.PrintSearchResults(matches_list)

            UserInterface.PrintTotalBorn(matches_list)
        elif selection == 2:
            name_to_search = UserInterface.GetSearchName()

            match_list = Processor.SearchData(name_to_search, dataDict)

            DataGraph.display_graph("Year", "Number born", match_list)