#help you to install any folder as a local package and impport functions from different modules
from setuptools import setup, find_packages 
setup(
    name='medical-chatbot',
    version='0.1.0',
    author='Piyush Kaushik ',
    author_email='piyushkaushik14@gmail.com',
    packages=find_packages(),
    install_requires=[] # see requirements.txt for the list of dependencies
)