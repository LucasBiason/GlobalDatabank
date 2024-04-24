from setuptools import setup

setup(
    name='django-toolbox',
    version='1.0.2',
    descriptions='Toolbox library for django projects',
    author='Lucas Biason',
    packages=[
        'toolbox',
    ],
    install_requires=[
        'pycpfcnpj==1.5.1',
        'validators==0.18.1',
    ]
)
