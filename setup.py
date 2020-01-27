import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='lazy-aidan',
    version='0.0.1',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    license='MIT License',
    description='An easy sms/email notifier that lets you send yourself updates on how your code is doing.',
    long_description=README,
    url='https://github.com/Adawg4/lazy-aidan/',
    author='Adawg4',
    author_email='aidan@upakka.com',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
	install_requires = [
		
    ],
)
