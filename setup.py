from setuptools import setup

setup(
    name="pytest-dictsdiff",
    version='0.5.4',
    py_modules=["pytest_dictsdiff"],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Lukasz Balcerzak',
    author_email='lukaszbalcerzak@gmail.com',
    entry_points={"pytest11": ["dictsdiff = pytest_dictsdiff"]},
    license='MIT',
    classifiers=["Framework :: Pytest"],
    install_requires=['dictdiffer'],
)
