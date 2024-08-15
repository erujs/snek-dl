from redvid import Downloader


def download_redvid_video(url, output_path):
    try:
        # Initialize the Downloader
        reddit = Downloader(max_q=True)

        # Set the URL and output path
        reddit.url = url
        reddit.path = output_path

        # Download the video
        reddit.download()

    except Exception as e:
        print(f"Failed to download video from {url}. Error: {e}")
