# delall_package/setup.py

from setuptools import setup, find_packages

setup(
    name="delall_package",
    version="0.1.0",
    packages=find_packages(),
    description="A simple package to delete all variables in the current namespace",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Sampson Palmisano",
    author_email="spalmisano21@hotmail.com",
    url="https://github.com/realsonnyp/delall_package",  # Update with your GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
