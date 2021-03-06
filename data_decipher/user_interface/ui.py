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
        usersName = input().rstrip(" ")
        print("Enter year to search.")
        print("(Enter nothing or 0 to search all years.)")
        usersYear = input().rstrip(" ")
        print()

        if not usersYear:
            usersYear = 0

        usersYear = int(usersYear)

        return (usersName, usersYear)

    @staticmethod
    def GetSearchName() -> str:
        """ Get a name to search for """
        print("Enter a name to graph.")
        users_name = input()
        return users_name

    @staticmethod
    def PrintTotalBorn(dataDict: dict):
        total = dataDict["total"]
        total_females = dataDict["females"]
        total_males = dataDict["males"]
        year_range = dataDict["range"]

        print(f"Total people with the name in data: {total} ")
        print(f"Females: {total_females}")
        print(f"Males: {total_males}")
        print(f"Year range: {year_range}\n")

    @staticmethod
    def PrintSearchResults(matches_list: list):
        """ print the given values """
        for i in range(len(matches_list)):
            matches = matches_list[i]
            print(matches[0])
            print(f"Year: {matches[1]}")
            print(f"Gender: {matches[2]}")
            print(f"Number of people born with the name that year: {matches[3]}\n")