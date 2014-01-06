try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


setup(
    name='datahubup',
    version="0.1",
    author='Ross Jones',
    author_email='ross@servercode.co.uk',
    url='http://datahub.io/',
    description="A simple command line tool for uploading files to datahub.io",
    long_description = "A simple command line tool for uploading files to datahub.io",
    install_requires=[
        "ckanclient==0.10"
    ],
    extras_require = {
    },
    zip_safe=False,
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['datahubup'],
    include_package_data=True,
    package_data={},
    entry_points="""
    [console_scripts]
    datahubup = datahubup.client:main
    """,
)
