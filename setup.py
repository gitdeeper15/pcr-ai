#!/usr/bin/env python3
"""Setup script for PCR_AI — Research II."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip()
        for line in fh
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="pcr-ai",
    version="0.1.0",
    author="Samir Baladi",
    author_email="gitdeeper@gmail.com",
    description="The Production and Control of Representations in Artificial Intelligence — Research II: A Conceptual Architecture, Authority Structure, Representation Lifecycle, and Research Protocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests", "tests.*", "docs", "docs.*", "PUBLICATION", "PUBLICATION.*", "ANALYSIS", "ANALYSIS.*", "REPORTS", "REPORTS.*"]),
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.11",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Sociology",
        "Topic :: Documentation",
    ],
    keywords="AI, representations, structural analysis, platform studies, human-AI interaction, research protocol, authority structure, lifecycle, pcr-ai",
    project_urls={
        "Homepage": "https://pcr-ai.netlify.app",
        "GitHub": "https://github.com/gitdeeper15/pcr-ai",
        "GitLab": "https://gitlab.com/gitdeeper/pcr-ai",
        "Codeberg": "https://codeberg.org/gitdeeper/pcr-ai",
        "Bitbucket": "https://bitbucket.org/gitdeeper/pcr-ai",
        "Zenodo": "https://doi.org/10.5281/zenodo.23940837",
        "PyPI": "https://pypi.org/project/pcr-ai/",
        "OSF": "https://osf.io/vmx2u",
    },
)
