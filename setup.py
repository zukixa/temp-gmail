import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name='temp-gmail',
    version='1.0.1',
    author="zukixa",
    author_email="56563509+zukixa@users.noreply.github.com",
    description="temp gmail api.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zukixa/temp-gmail",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['curl_cffi'],
)
