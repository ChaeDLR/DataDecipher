#!/venv/bin/python
from processing.processor import Processor
from user_interface.ui import UserInterface
from graph.stat_graph import DataGraph


class DataDecipher:
    def __init__(self):
        names_path = "./names/"
        self.names_data_dict = Processor.GetFilesTextData(names_path)

    def _run_console_option(self) -> None:
        usersInput = UserInterface.GetUserInput()

        matches_list = Processor.SearchData(
            usersInput[0], self.names_data_dict, usersInput[1]
        )

        UserInterface.PrintSearchResults(matches_list)

        matches_total = Processor.GetSearchTotals(matches_list)

        UserInterface.PrintTotalBorn(matches_total)

    def _run_graph_option(self) -> None:
        name_to_search = UserInterface.GetSearchName()

        match_list = Processor.SearchData(name_to_search, self.names_data_dict)

        DataGraph.display_graph("Year", "Number born", match_list)

    def run_program(self) -> None:
        while True:
            selection: int = UserInterface.MainMenu()

            if selection == 1:
                self._run_console_option()

            elif selection == 2:
                self._run_graph_option()


if __name__ == "__main__":

    data_decipher = DataDecipher()
    data_decipher.run_program()
