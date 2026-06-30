import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
from typing import List

hy='-e .'

def get_requriments(file_path:str)->List[str]:
    
  with open(file_path)as file_obj:
   requirements=file_obj.readlines()
   
   requirements=[req.replace('\n','') for req in requirements]

   
   if hy in requirements:
     requirements.remove(hy)
   return requirements

__version__ = "0.0.0"

REPO_NAME = "Deep-Learning-Project"
AUTHOR_USER_NAME = "Babaralikhan098"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "babaralikhanaiexpert098@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=get_requriments('requirements.txt')
)