from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    # Function to read requirements from a file
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = [req.strip() for req in file_obj.readlines() if req.strip() != HYPHEN_E_DOT]
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='jesuisaditya10',
    author_email='jesuisaditya10@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
