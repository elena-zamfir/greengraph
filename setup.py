from setuptools import setup, find_packages
setup(
name = "Greengraph",
version = "0.1",
packages = find_packages(exclude = ['*test']),
scripts = ['scripts/plot_green_between'],
install_requires = ['argparse']
)
# I should now be able to install the package and import it wherever. But I have no script
#yet to be executed as command line commands.
