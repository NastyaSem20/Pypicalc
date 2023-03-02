import setuptools

with open('readme.md.') as file:
    read_me_desc = file.read()

setuptools.setup(
    name='calculator56',
    version="0.1",
    author='Nastya',
    author_email='nastszanzhuu@gmail.com',
    description='My calculator',
    long_description=read_me_desc,
    long_description_content_type ="text/markdown",
    packages=['calculator56'],
    install_requires=['logging'],
    python_requires='>=3.6',
    url='https://github.com/NastyaSem20/Pypicalc'
)