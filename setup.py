from setuptools import setup

setup(
    name='AADI-Rover-Domain',
    version='0.1',
    packages=['RoverDomain_Core'],
    url='https://github.com/AADILab/AADI-Rover-Domain',
    license='',
    author='Nicholas Zerbel',
    author_email='zerbeln@oregonstate.edu',
    description='Core AADI Rover Domain Implementation',
    install_requires=[
        'numpy>=1',
        'pygame>=2'
    ]
)
