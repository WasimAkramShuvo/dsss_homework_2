from setuptools import setup, find_packages

setup(
    name="math-quiz",
    version="1.0",
    packages=find_packages(),
    install_requires=[],  # Add dependencies here if needed
    author="WasimAkramShuvo",
    author_email="wasimakaramshuvo.net@gmail.com",
    description="A simple math quiz game with random questions.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/WasimAkramShuvo/dsss_homework_2",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)