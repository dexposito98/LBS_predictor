from setuptools import setup
from setuptools import find_packages

setup(
    name='BS_predictor',
    version='1.0',
    description = "Binding site prediction of a pdb query protein based on interactions and properties of the residues using supervised learning.",
    
    author="Denis Expósito Navarro, Marta Alonso Caubilla, Yolanda Andrés López",
    author_email="denis.exposito01@estudiant.upf.edu, marta.alonso07@estudiant.upf.edu, yolanda.andres01@estudiant.upf.edu",
    packages=['BS_predictor'],
    
    package_data = {
        "BS_predictor": [".csv", ".py", "data/classes"],
    },
    include_package_data=True,
    
    entry_points={
        'console_scripts': [
            'BS_predictor=BS_predictor:main'
        ]
    },
    install_requires=[
        'pandas >= 2.0',
        'biopython >= 1.81', 
        'scikit-learn>= 1.2.2', 
        'numpy >= 1.23.4', 
        'networkx >= 3.1', 
        'scipy >= 1.10.1'],
    script_name = 'BS_predictor.py')

