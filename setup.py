import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

dependencies = [
    'aiohttp', 
    'aiosqlite',
    'nanoevent',
    'nanoinject',
    'yoyo-migrations',
]

test_deps = [
    'pytest'
]

setuptools.setup(
    name="nanobrew.core",
    version="0.0.1",
    author="Berry Langerak",
    author_email="berry.langerak@gmail.com",
    description="Nanobrew is brewing automation software",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nanobrew/nanobrew-core",
    packages=['nanobrew'],
    install_requires=dependencies,
    tests_require=test_deps,
    extras_require={
        'test': test_deps,
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 2 - Pre-Alpha',
    ],
    python_requires='>=3.6',
)