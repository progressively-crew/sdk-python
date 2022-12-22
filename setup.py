from setuptools import find_packages, setup

setup(
    name='progressively/sdk',
    packages=find_packages(include=['sdk']),
    version='0.0.1',
    description='Python SDK for Progressively',
    author='Marvin Frachet <marvin.frachet@gmail.com>',
    license='MIT',
    install_requires=[
        "requests>=2.28"],
    setup_requires=[],
    tests_require=[]
)