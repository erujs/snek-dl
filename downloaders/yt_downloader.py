import yt_dlp


def download_yt_video(url, output_path, cookies_path=None):
    try:
        ydl_opts = {
            "format": "best",
            "outtmpl": f"{output_path}/%(title)s~%(id)s.%(ext)s",
            "postprocessors": [
                {
                    "key": "FFmpegVideoConvertor",
                    "preferedformat": "mp4",  # Convert to mp4
                }
            ],
            "cookiefile": cookies_path
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    except yt_dlp.DownloadError as e:
        print(f"Download error: {e}")
    except Exception as e:
        print(f"Failed to download video from {url}. Error: {e}")
