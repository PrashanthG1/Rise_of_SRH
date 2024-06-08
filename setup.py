from setuptools import find_packages, setup

k= '-e .'

def get_requirements(file_path:str)-> list[str]:
    '''
    This function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace('\n', '') for req in requirements]

        if k in requirements:
            requirements.remove(k)

    return requirements





setup(
name='SRH 2024',
version= '0.0.1',
author='prashanth',
author_email='prashanth.shastha@gmail.com',
packages= find_packages(),
install_requires= get_requirements('requirements.txt')


)

