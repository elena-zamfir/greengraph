from argparse import ArgumentParser
from Greengraph import  Map
from Greengraph import Greengraph
import matplotlib.pyplot as plt


def process():
    parser = ArgumentParser(description = "Generate graph of green spaces between tho given locations")


    parser.add_argument('--start', help="starting point" , default = 'London')
    parser.add_argument('--finish', help = 'end point', default = 'Oxford')
    parser.add_argument('--nr_steps', help = 'nr points in between', type=int, default = 10 )
    parser.add_argument('--output', help = 'file into which to save the plot')
    arguments = parser.parse_args()

    plt.close()
    figure = plt.figure()
    figure_axes = figure.add_subplot(1,1,1)
    figure_axes.plot(Greengraph(arguments.start ,arguments.finish).green_between(arguments.nr_steps))
    if arguments.output:
        figure.savefig(arguments.output)

    plt.show()




if __name__ == "__main__":
    process()
