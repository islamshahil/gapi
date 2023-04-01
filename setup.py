import setuptools 
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name='payall',
    version='1.0.2.3',
    description='Cross Chain Streamlined Payment Engine',
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='http://www.hashit.ml/',
    author='Hash - It',
    author_email='shahilislam@gmail.com',
    license='MIT',
    readme = "README.md",
    packages=['controller','solanaprocessor','payall'],
    zip = False,
    install_requires=[
        "requests",
        "importlib-metadata",
      ],
    package_data={
        '':[
    ]
    },
    entry_points={
        'console_scripts': [
            'payall = payall.__main__:main',
        ]
    },
    classifiers=[ 
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent', 
    ],
    project_urls = {
        'Source': 'https://github.com/islamshahil/Hash-It',
    },
    keywords="scripting, automation, python, blockchain, solana"
)