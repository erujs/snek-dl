# snek-dl

Python program for downloading videos using `redvid` and `yt-dlp`.

## Dependencies/Libraries

- [Python 3.x](https://www.python.org/downloads/)
- `ffmpeg` (install via system package manager):
  - On Ubuntu/Debian: `sudo apt-get install ffmpeg`
  - On MacOS: `brew install ffmpeg`
  - On Windows: Download from the [FFmpeg website](https://ffmpeg.org/download.html) and add it to your system PATH.

## Setup Instructions

1. Clone the repository:
	```
	git clone <repository-url>
	cd <repository-directory>
	```

2. Install Python dependencies:
	```
	pip install -r requirements.txt
	```

3. Add video URLs in data.py.

4. Run the script:
	```
	python3 main.py
	```

## Scope

- **Supported Platforms**:
  - YouTube
  - TikTok
  - Reddit

## Future Plans

We are actively working on adding support for additional platforms in future updates.