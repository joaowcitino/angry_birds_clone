from setuptools import setup, find_packages

setup(
    name="angry_birds_clone",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pygame>=2.0.0",
        "numpy",
        "math",
        "os",
        "sys",
        "random",
    ],
    entry_points={
        'console_scripts': [
            'angry_birds_clone=angry_birds_clone.main:main',
        ],
    },
    package_data={
        'angry_birds_clone': ['assets/*.png'],
    },
    author="Seu Nome",
    author_email="seuemail@exemplo.com",
    description="Um clone de Angry Birds em Python usando Pygame e física.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/feijonts/angry_birds_clone",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
