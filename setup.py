from setuptools import setup

setup(
    name='snapshotalyzer',
    version=0.1,
    author="ekimr72",
    author_email="ekimr72@email.com",
    description="Snapshotalyzer is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/ekimr72/snapshotalyzer",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
