from setuptools import setup

setup(
    name='capitalize',
    version='0.1.0',
    author='gabriel meringolo',
    author_email='gabriel.meringolo@gmail.com',
    packages=['capitalize', 'capitalize.test', ],
    scripts=['bin/cap_script.py'],
    url='http://pypi.python.org/pypi/capitalize/',
    license='LICENSE.txt',
    description='An awesome package that does something',
    long_description=open('README.txt').read(),
    install_requires=["pytest", ],
    tests_require=["pytest", ],
    setup_requires=["pytest-runner", ],
    )


