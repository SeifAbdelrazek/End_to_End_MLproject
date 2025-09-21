from setuptools import setup, find_packages
from typing import List
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements if req.strip() != ""]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements        


setup(
    name='ml_project',
    version='0.0.1',
    author='seif_ahmed',
    author_email='eldinsafe@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

    
)