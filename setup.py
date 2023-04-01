import setuptools 
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name='gapi',
    version='1.0.0',
    description='GSheet Applications Programming Interface',
    long_description_content_type='text/markdown',
    long_description=long_description,
    url='http://www.shahilislam.ml/',
    author='Shahil Islam',
    author_email='shahilislam@gmail.com',
    license='MIT',
    readme = "README.md",
    packages=['gapi','gapi.readsheet'],
    zip = False,
    install_requires=[
        "importlib-metadata",
        "google-api-python-client",
        "google-auth-httplib2",
        "google-auth-oauthlib"
      ],
    package_data={
        '':[
    ]
    },
    entry_points={
        'console_scripts': [
            'gapi = gapi.__main__:main',
        ]
    },
    classifiers=[ 
        'Programming Language :: Python :: 3', 
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent', 
    ],
    project_urls = {
        'Source': 'https://github.com/islamshahil/gapi',
    },
    keywords="scripting, automation, python, gsheets"
)