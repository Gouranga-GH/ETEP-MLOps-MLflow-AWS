import setuptools  # Importing the setuptools library, which provides tools for packaging Python projects

# Opening the README.md file to use its content as the long description for the package
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()  # Reading the contents of README.md into a variable

__version__ = "0.0.0"  # Defining the version of the package

# Defining metadata variables for the package
REPO_NAME = "ETEP-MLOps-MLflow-AWS"  # Name of the GitHub repository
AUTHOR_USER_NAME = "Gouranga-GH"  # GitHub username of the author
SRC_REPO = "ETEP_MLOps_MLflow_AWS"  # Name of the source repository (directory containing the package code)
AUTHOR_EMAIL = "post.gourang@gmail.com"  # Email of the author

# The setup function from setuptools is used to configure the package details
setuptools.setup(
    name=SRC_REPO,  # Name of the package
    version=__version__,  # Version of the package
    author=AUTHOR_USER_NAME,  # Name of the package author
    author_email=AUTHOR_EMAIL,  # Author's email address
    description="A python package setup",  # Short description of the package
    long_description=long_description,  # Detailed description of the package, usually the README.md content
    long_description_content="text/markdown",  # Format of the long description (Markdown in this case)
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL to the project repository on GitHub
    project_urls={  # Additional URLs related to the project
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # URL for reporting bugs
    },
    package_dir={"": "src"},  # Specifies that the package code is located in the "src" directory
    packages=setuptools.find_packages(where="src")  # Automatically finds all packages in the "src" directory
)
