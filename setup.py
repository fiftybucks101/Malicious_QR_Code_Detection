import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = 'Mlops/tree/main/Malicious_QR_Code_Detection'
AUTHOR_USER_NAME = 'fiftybucks101'
SRC_REPO = 'MaliciousQRCOdeDetection'
AUTHOR_EMAIL = 'fiftybucks001@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version = __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='Python package for Malicious URL Detection in QR Code',
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"": "src"},
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    packages=setuptools.find_packages(where='src')
)