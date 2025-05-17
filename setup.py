from setuptools import find_packages,setup
from typing import List

def get_requirment() ->List[str]:
    """
    This is a function will return list of requirments
    """
    requirment_lst:List[str] = []
    try:
        with open('requirments.txt','r') as file:
            #Read lines from the files
            lines = file.readlines()
            ## process each line
            for line in lines:
                requirment = line.strip()
                ## ignore empty line and -e .
                if requirment and requirment!='-e .':
                    requirment_lst.append(requirment)
    except FileNotFoundError:
        print('reuirment.txt file not found')

    return requirment_lst
print(get_requirment())
setup(
    name="NetworkSecurity",
    version='0.0.0.1',
    author = 'vedant choubey',
    author_email="vedantchoubey@gmail.com",
    package = find_packages(),
    install_requires = get_requirment()
)

