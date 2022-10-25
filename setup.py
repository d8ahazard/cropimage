import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cropimage_dh",
    version="0.0.6",
    author="D8ahazard",
    author_email="donate.to.digtalhigh@gmail.com",
    description="A simple toolkit for detecting and cropping main body from pictures.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/haofanwang/cropimage",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
