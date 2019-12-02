from setuptools import setup, find_packages


setup(name='myproject',
    version = "1.00",
    packages = find_packages(),  
    package_data = {
        # If any package contains *.py, include them:
        '': ['*.py'],
    })
