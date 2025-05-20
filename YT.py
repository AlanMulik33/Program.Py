import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mkv',
        'outtmpl': '%(title)s.%(ext)s',
        'quiet': True,  # Suppress yt_dlp output for cleaner display
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download successful!")
    except Exception as e:
        print(f"an error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter YouTube video URL: ")
    download_video(url)