import setuptools



with open("tomsup/about.py") as f:
    v = f.read()
    for l in v.split("\n"):
        if l.startswith("__version__"):
            __version__ = l.split('"')[-2]

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="tomsup",
    version=__version__,
    description="An implementation of game theory of mind in a agent based \
       framework following the implementation of Devaine, et al. (2017).",
    license="Apache License 2.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kenneth C. Enevoldsen and Peter T. Waade",
    author_email="kennethcenevoldsen@gmail.com",
    url="https://github.com/KennethEnevoldsen/tomsup",
    packages=setuptools.find_packages(),
    # external packages as dependencies
    install_requires=["numpy >= 1.2.4", 
                      "pandas >= 1.2.3", 
                      "scipy >= 1.6.3", 
                      "matplotlib >= 3.4.2", 
                      "seaborn >= 0.11.1",
                      "joblib >= 1.0.1",
                      "wasabi >= 0.8.2,<0.9.0",
                      ],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="theory-of-mind tom game-theory",
)
