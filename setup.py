from distutils.core import setup

setup(
    name='Kaggle Nlp Refresher',
    version='0.1.0',
    author='Özer Baday',
    author_email='',
    packages=['pandas'],
    scripts=[],
    url='',
    license='LICENSE.txt',
    description='',
    long_description=open('README.txt').read(),
    install_requires=[
        "pandas >= 0.23.4",
        "beautifulsoup4 >= 4.6.3",
    ],
)