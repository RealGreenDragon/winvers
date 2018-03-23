from setuptools import setup

setup(
    name = 'winvers',
    packages = ['winvers'],
    version = '0.1.1',
    description = 'Definitive Windows version checker for Python',
    long_description=open("README.rst").read(),
    author = 'Daniele Giudice',
    license = 'GPL v3',
    python_requires='>=2.7, <4',
    url = 'https://github.com/MagicGreenDragon/winver',
    keywords = ['windows', 'version', 'check'],
    classifiers = (
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        ),
)
