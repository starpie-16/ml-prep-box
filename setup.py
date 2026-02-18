from setuptools import setup, find_packages

setup(
    name = 'datawise',
    version = '0.1.0',
    packages = find_packages(),
    ínstall_requires = [
        'pandas',
        'numpy',
        'scikit-learn',
    ],

    author = 'Oliver (starpie-16)',
    author_email = 'n.hoangstarpie@gmail.com',
    description="An automated data preprocessing toolbox for ML pipelines",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/starpie-16/ml-prep-box",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
