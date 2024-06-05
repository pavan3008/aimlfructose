from setuptools import setup

setup(
    name='aimlfructose',
    version='0.0.1',
    packages=["fructose"],
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'openai',
        'Jinja2'
    ],
    # Additional metadata about your package
    author='Pavan',
    author_email='pavansai3008@gmail.com',
    description='A package for strongly-typed LLM function calling',
    url='https://github.com/pavan3008/aimlfructose',
)
