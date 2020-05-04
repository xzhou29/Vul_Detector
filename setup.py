from setuptools import setup


entry_points = {
    "console_scripts": ["vulbench=main:main"]
}


setup(
    name='vulbench',
    version='1.0',
    packages=[''],
    url='',
    license='',
    author='Xin Zhou',
    author_email='xin.zhou.pro@gmail.com',
    description='A vulnerability detection benchmarking framework',
    entry_points=entry_points
)
