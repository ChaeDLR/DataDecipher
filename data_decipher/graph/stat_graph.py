import matplotlib.pyplot as plt


class DataGraph:
    @staticmethod
    def display_graph(x_axe: str, y_axe: str, data: list):
        """ display a graph with the given values """
        # TODO: Graph needs work in order to display data correctly
        name = data[0][0]
        years_list = []
        people_born = []
        y_ticks = []
        data.sort()
        for i in range(len(data)):
            data_list = data[i]
            years_list.append(data_list[1])
            people_born.append(data_list[3])
            y_ticks.append(data_list[3])
        y_ticks.sort()

        fig, names_plot = plt.subplots()
        # names_plot.plot(years_list, people_born, linewidth=3, color="b")

        plt.bar(years_list, people_born)
        names_plot.set_title(name, fontsize=20)
        names_plot.set_xlabel(x_axe, fontsize=14)
        names_plot.set_ylabel(y_axe, fontsize=14)
        names_plot.set_ylim(bottom=0, top=max(people_born))

        names_plot.tick_params(axis="both", labelsize=4)

        names_plot.legend()

        plt.show()