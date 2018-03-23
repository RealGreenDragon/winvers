from setuptools import setup

setup(
    name = 'winver',
    packages = ['winver'],
    version = '0.1',
    description = 'Definitive Windows version checker for Python',
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