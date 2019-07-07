import setuptools

print(setuptools.find_packages())

long_description="""
EasePy: A simple system which provides some basic utilities.

EasyPy was made out of my desire to learn how to use Python more.

EasyPy offers several features: Numb Operations, Fractions, List Features,
String Features, Instrance Generation (Not All Work Yet), and most importantly...
An advanced chat bot system (based on nltk but expanded upon)
"""

setuptools.setup(
     name='easePy',  
     version='1.0',
     author="Corman Online",
     author_email="mrccay@12gmail.com",
     description="A simple package which adds a chat bot system, and several utilities.",
     long_description=long_description,
     license='Apache 2.0 License',
     long_description_content_type="text/markdown",
     url="link",
     package_data={'': ['__init__.py']},
     include_package_data=True,
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
 )
