from distutils.core import setup

setup(
    name='docxstache',
    version='0.0.1',
    author='V. David Zvenyach',
    author_email='dave@esq.io',
    packages=['docxstache'],
    scripts=[],
    url='http://pypi.python.org/pypi/docxstache/',
    download_url="https://github.com/vzvenyach/docxstache2/tarball/0.0.1",
    license='LICENSE.txt',
    description='Mustache for docx',
    long_description=open('readme.md').read(),
    install_requires=[
        "pystache>=0.5.4",
    ],
)