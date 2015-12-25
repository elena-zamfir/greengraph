from argparse import ArgumentParser
from Greengraph import  Map
from Greengraph import Greengraph
import matplotlib.pyplot as plt


def process():
    parser = ArgumentParser(description = "Generate graph of green spaces between tho given locations")


    parser.add_argument('--start', help="starting point" )
    parser.add_argument('--finish', help = 'end point')
    parser.add_argument('--nr_steps', help = 'nr points in between', type=int )
    arguments = parser.parse_args()
    if arguments.start:
        start = arguments.start;
    else:
        start = 'London';
    if arguments.finish:
        finish = arguments.finish;
    else:
        finish  = 'Oxford';
    if arguments.nr_steps:
        nr_steps = arguments.nr_steps;
    else:
        nr_steps = 10;
    plt.close()
    plt.plot(Greengraph(start ,finish).green_between(nr_steps))
    plt.show()

if __name__ == "__main__":
    process()
