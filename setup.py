from setuptools import find_packages, setup

Dash_E_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this funtion is to list all requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace('\n','') for req in requirements]

        if Dash_E_dot in requirements:
            requirements.remove(Dash_E_dot)
    return requirements
    
    
setup(
name='mlproject',
version='0.0.1',
author='Saxam',
author_email='chaturvedi.saksham2607@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)