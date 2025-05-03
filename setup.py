from setuptools import setup, find_packages

setup(
    name="ytp2mp3",
    version="0.1",
    packages=find_packages(),
    install_requires=[ # dep
        "yt-dlp",
        "pydub"
    ],
    entry_points={
        "console_scripts": [
            "ytp2mp3 = ytp2mp3.cli:main",  # module:function
        ],
    },
    python_requires=">=3.7",
)
