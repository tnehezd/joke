from setuptools import setup, find_packages

setup(
    name="Not A Joke",
    description="Lack of inspiration",
    license="MIT License",
    author="T.J. Dijkema",
    author_email="t.j.dijkema@gmail.com",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['tell_joke=joke.joke:tell_joke']
    }, install_requires=[]
)
