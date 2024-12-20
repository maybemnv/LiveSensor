from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    return requirement_list

setup(
    name="aps",
    version="0.1", 
    author="Manav",
    author_email="manavkauahal99@gmail.com",
    description="A predictive maintenance system for monitoring air pressure systems.",
    url="https://github.com/maybemnv/LiveSensor",
    packages=find_packages(),
)