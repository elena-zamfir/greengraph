from argparse import ArgumentParser
from Greengraph import  Map
from Greengraph import Greengraph
import matplotlib.pyplot as plt


def process():
    parser = ArgumentParser(description = "Generate graph of green spaces between tho given locations")


    parser.add_argument('start', help="starting point",
                    type=str )
    parser.add_argument('finish', help = 'end point', type = str)
    parser.add_argument('nr_steps', help = 'nr points in between', type=int )
    arguments = parser.parse_args()

    plt.plot(Greengraph(arguments.start ,arguments.finish).green_between(arguments.nr_steps))
    plt.show()

if __name__ == "__main__":
    process()
