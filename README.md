## Lambda-blog-test


It will automate the web application project, specifically for Lambda Web project.
This is developed on python selenium and Robot framework(for reports).
Python version: Python 3.7.5

## Note:
I used Pycharm, you can also add the dependecy through Pycharm-> Preferences ->Project Interpreter-> "+" button
## Best to have a virtualenv to run this project
'''
 python3 -m venv /path/to/new/virtual/environment
'''

## You can install this framework through the command line,
'''pip install robotframework'''
'''pip install selenium'''
'''pip install setuptools'''


<b>To know more about robotframework :</b>
- [robotframework](http://robotframework.org)

## Simple command which tells, how to run this project with test suite,
Go to directory
'''
cd Lambda-blog-test
'''
'''
python setup.py install
'''

## And run below command,
'''
 robot --outputdir "Logs/${date}"  --variable  BROWSER:chrome  --variable URL:https://lambda.grofers.com/ TestSuites/test_links.robot
'''

## In the above command BROWSER can be one of the below:
chrome
firefox
safari
