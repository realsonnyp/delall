# delall/setup.py

from setuptools import setup

setup(
    name="delall_package",
    version="0.1.0",
    py_modules=["delall"],  # Explicitly declare the module (delall.py)
    description="A simple package to delete all variables in the current namespace",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Sampson Palmisano",
    author_email="spalmisano21@hotmail.com",
    url="https://github.com/realsonnyp/delall",  # Update with your GitHub URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
