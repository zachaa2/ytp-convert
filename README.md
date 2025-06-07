# 🎵 ytp-convert

[![PyPI version](https://badge.fury.io/py/ytp-convert.svg)](https://pypi.org/project/ytp-convert/)

**ytp-convert** is a Python-based command-line tool that downloads entire YouTube playlist and combines the content into a single media file.

Enjoy listening to your favorite playlists as one contiguous file, and skip advertisements. 

---

## 🚀 Features

- Downloads entire **YouTube playlists**
- Merges all tracks into one file
- Cross-platform (Windows, macOS, Linux)
- Built with `yt-dlp`, `pydub`, and `ffmpeg`

---

## 📦 Installation

Installation of Python is required.  You can install the tool from [PyPI](https://pypi.org/project/ytp-convert/)

```bash
pip install ytp-convert
```

⚠️ ffmpeg is required — see below.

## Usage

| Option               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `url` (positional)   | The YouTube playlist URL                                                    |
| `-o`, `--output`     | Output filename **without extension** (default: `combined`)                 |
| `-f`, `--force`      | Skip failed downloads instead of aborting the process                       |
| `--format`           | Output format: `mp3` or `mp4` (default: `mp3`)                              |


```bash
ytp-convert "https://youtube.com/playlist?list=..." -o my_playlist --format .mp3
```

For more help, use
```
ytp-convert --help
```

## 🔧 System Requirement: ffmpeg

This tool requires ffmpeg to process audio streams and concatenate media files. The installation instructions are below.

### macOS
```bash
brew install ffmpeg
```

### Ubuntu / Debian
```bash
sudo apt install ffmpeg
```

### Windows
Download from ffmpeg.org

Add the bin/ folder to your system PATH

