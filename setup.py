import setuptools

with open("README.md", encoding="utf8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="thivabots",
    packages=setuptools.find_packages(),
    version="0.1.1",
    license="TNJ",
    description="A Project Made To Enjoy :)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="ThivankaNirmal",
    author_email="info@thivanka.lk",
    url="https://github.com/thivankaonline/thivabots",
    keywords=["sdbots", "python-pakage", "sd-api", "api", "thivankaja", "mritzme", "thivankaonline"],
    install_requires=["requests>=2.28.1"],
    project_urls={
        "Tracker": "https://github.com/thivankaonline/thivabots/issues",
        "Community": "https://t.me/ThivankaOnline",
        "Source": "https://github.com/thivankaonline/thivabots",
        "Documentation": "https://docs.thivabots.tk",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: TNJ License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)