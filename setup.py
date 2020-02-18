'''
Setup script for json_visualizer
This file is a part of json_visualizer
'''


from setuptools import setup

if __name__ == '__main__':
    
    # Long description
    with open('./README.md') as f:
        readme = f.read()
    
    setup(
        name='json_visualizer',
        version='0.0.1',
        description='Posting message to slack for Python',
        long_description=readme,
        author='Ryotaro A. Abe',
        author_email='ryoutar.abe@gmail.com',
        url='https://github.com/users/RyotaroAbe/projects/',
        license='MIT',
        install_requires=['json'])
