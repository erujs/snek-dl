import os
from data import data
from downloaders.yt_downloader import download_yt_video
from downloaders.rd_downloader import download_redvid_video


def create_or_get_folder(folder_path):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        # If it doesn't exist, create the folder
        os.makedirs(folder_path)
        print(f"Folder created: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")

    # Get the absolute path of the folder
    folder_path = os.path.abspath(folder_path)
    return folder_path


def get_platform(url):
    if "reddit.com" in url:
        return "reddit"
    elif "youtube.com" in url:
        return "youtube"
    elif "tiktok.com" in url:
        return "tiktok"
    else:
        return None


def download_video(url, output_folder, cookies_path=None):
    platform = get_platform(url)

    if platform == "reddit":
        download_redvid_video(url, output_folder)
    elif platform == "youtube" or "tiktok":
        download_yt_video(url, output_folder, cookies_path)
    else:
        print(f"No downloader available for URL: {url}")


def main():
    urls = data()
    output_folder = create_or_get_folder("downloads")

    for url in urls:
        download_video(url, output_folder)


if __name__ == "__main__":
    main()
