import sys


class UserInterface:
    @staticmethod
    def MainMenu() -> int:
        console_selection = ["1", "console"]
        graph_selection = ["2", "graph"]
        kill_codes = ["exit", "esc", "quit"]
        while True:
            print("Select how you want to display the data.")
            print("1) Console.")
            print("2) Graph.")
            userSelection = input().lower()
            if userSelection in console_selection:
                return 1
            elif userSelection in graph_selection:
                return 2
            elif userSelection in kill_codes:
                sys.exit()
            else:
                print("ERROR: Enter a valid option.")

    @staticmethod
    def GetUserInput() -> set:
        """Get a name and a year to search
        return set (name, year)"""

        print("Enter name to search for.")
        usersName = input()
        print("Enter year to search.")
        print("(Enter nothing or 0 to search all years.)")
        usersYear = input()
        print()

        if not usersYear:
            usersYear = 0

        return (usersName, usersYear)

    @staticmethod
    def GetSearchName() -> str:
        """ Get a name to search for """
        print("Enter a name to graph.")
        users_name = input()
        return users_name

    @staticmethod
    def PrintTotalBorn(dataList: list):
        total_born = 0
        males_born = 0
        females_born = 0
        for i in range(len(dataList)):
            matches = dataList[i]
            total_born += int(matches[3])
            if matches[2] == "M":
                males_born += int(matches[3])
            elif matches[2] == "F":
                females_born += int(matches[3])
        print(f"Total people with the name in data: {total_born}")
        print(f"Females: {females_born}")
        print(f"Males: {males_born}")

    @staticmethod
    def PrintSearchResults(matches_list: list):
        """ print the given values """
        for i in range(len(matches_list)):
            matches = matches_list[i]
            print(matches[0])
            print(f"Year: {matches[1]}")
            print(f"Gender: {matches[2]}")
            print(f"Number of people born with the name that year: {matches[3]}")