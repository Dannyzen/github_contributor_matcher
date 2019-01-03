import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Github_Contributor_Matcher",
    version="0.1.1",
    author="Dannyzen",
    author_email="danny.rosen@gmail.com",
    description="Identify contributors of a repo, given their organization",
    keywords='github contributor organization matcher repo',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dannyzen/github_contributor_matcher",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent"],
    install_requires=[
        "github3.py==1.2.0",
        "pyyaml==3.13"],
    entry_points={
        "console_scripts":[
            "github_contributor_matcher=github_contributor_matcher.contributor_matcher:main"]
    }
)
