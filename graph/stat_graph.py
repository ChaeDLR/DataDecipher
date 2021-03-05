import matplotlib.pyplot as plt


class DataGraph:
    def _parse_names_data(self, data: list):
        name = data[0]
        years_list = []
        people_born = []

        for i in len(data):
            data_list = data[i]
            years_list.append(data_list[1])
            people_born.append(data_list[3])

        data_list = [years_list, people_born]

    @staticmethod
    def display_graph(x_axe: str, y_axe: str, data: list):
        """ display a graph with the given values """
        # TODO: Graph needs work in order to display data correctly
        name = data[0]
        years_list = []
        people_born = []
        data.sort()
        for i in range(len(data)):
            data_list = data[i]
            years_list.append(data_list[1])
            people_born.append(data_list[3])

        fig, names_plot = plt.subplots()
        names_plot.plot(years_list, people_born, linewidth=3, color="b")

        names_plot.set_title(name, fontsize=20)
        names_plot.set_xlabel(x_axe, fontsize=14)
        names_plot.set_ylabel(y_axe, fontsize=14)

        names_plot.tick_params(axis="both", labelsize=4)

        names_plot.legend()

        plt.show()