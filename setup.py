from setuptools import setup

setup(
    name="pytest-dictsdiff",
    packages=["pytest_dictsdiff"],
    author='Lukasz Balcerzak',
    author_email='lukaszbalcerzak@gmail.com',
    entry_points={"pytest11": ["dictsdiff = pytest_dictsdiff"]},
    license='MIT',
    classifiers=["Framework :: Pytest"],
    install_requires=['dictdiffer'],
)
