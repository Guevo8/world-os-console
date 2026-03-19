from setuptools import setup, find_packages

setup(
    name="world-os-console",
    version="0.1.0",
    description="6-Tier Worldbuilding Framework (FastAPI + CLI)",
    author="Tobi Peters",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.100.0",
        "uvicorn>=0.20.0",
        "pydantic<2.0",
        "requests>=2.31.0",
    ],
    entry_points={
        'console_scripts': [
            'world-os=cli.main:main',
        ],
    },
    python_requires='>=3.10',
)
