from setuptools import find_packages, setup

def get_requirements(file_path):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()
    return requirements

setup(
    name='Classification_project',
    version='0.0.1',
    author='Abhishek Jadhav',
    author_email='abhishekjadhav3470@gmail.com',
    description='Cat_dog_Object_classification',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
