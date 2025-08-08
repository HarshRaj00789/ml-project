from setuptools import find_packages, setup

setup(
    name='ml_project',
    version='0.0.1',
    author='Harsh',
    author_email='harshraj007891@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy','pandas','scikit-learn','matplotlib','seaborn']
)