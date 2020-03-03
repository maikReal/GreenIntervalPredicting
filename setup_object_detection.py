import os

os.environ['PYTHONPATH'] += ":/content/models/research/slim"


def run_setup():

    os.chdir('models/research/object_detection')

    os.system('python setup.py build')
    os.system('python setup.py install')

    os.chdir('../slim')

    os.system('python setup.py build')
    os.system('python setup.py install')

    os.chdir('../../../')
