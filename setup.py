from typing import List
from setuptools import setup, find_packages

def get_requirements() -> List[str]:
    """
    This function will return list of Requirements
    """
    requirement_list: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found")

    return requirement_list


setup(
    name = "NetworkSecurity",
    version = "0.0.1",
    author = "Aryan jani",
    author_email = "janiaryan993@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)


if __name__ == "__main__":
    print(get_requirements())