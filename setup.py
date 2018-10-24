from setuptools import setup, find_packages

setup(
    name="thumbs",
    version="1.0",
    license="MIT Licence",

    author="YeHarold",
    packages=find_packages(),
    include_package_data=True,
    platforms="linux",
    install_requires=['pillow',"adb"],

)