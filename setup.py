from setuptools import setup, find_packages
setup(
name = "Greengraph",
version = "0.1",
packages = find_packages(exclude = ['*test']),
scripts = ['scripts/plot_green_between'], #now command line call to plot_green_between works
install_requires = ['argparse']
)
 
