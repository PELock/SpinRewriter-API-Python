import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='spin-rewriter-api',

    version='1.0.0',

    description='Spin Rewriter is a revolutionary article spinner that uses ENL Semantic Spinning to understand the meaning of text. It produces high quality, unique and readable spun articles with a click.',
    long_description=long_description,
    long_description_content_type="text/markdown",

    keywords="spinner spinrewriter seo article enl semantic language english writing text",

    url='https://www.spinrewriter.com',

    author='Spin Rewriter',
    author_email='info@spinrewriter.com',

    license='Apache-2.0',

    packages=setuptools.find_packages(),

    include_package_data=False,
    zip_safe=False,

    install_requires=[
        'requests'
    ],

    classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Natural Language :: English",
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
      ],

    python_requires='>=3.5',
)