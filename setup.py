from setuptools import setup, find_packages
setup(
name = "Greengraph",
version = "0.1",
packages = find_packages(exclude = ['*test']),
scripts = ['scripts/greengraph'], #now command line call to plot_green_between works
install_requires = ['argparse']
)
