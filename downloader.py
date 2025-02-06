import yt_dlp

def download_audio(youtube_url, output_path="downloads"):
    try:
        # Configure download options
        ydl_opts = {
            'format': 'bestaudio/best',  # Download best audio quality
            'postprocessors': [{
                # Converts audio from webm to mp3
                'key': 'FFmpegExtractAudio', # needs to be installed on computer and the bin folder on enviroment variables.
                'preferredcodec': 'mp3', 
                'preferredquality': '192',
            }],

            'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Save file
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
            print("Download completed!")
        
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
video_urls = []
adding_more = True

while adding_more:
    url = input("Add a youtube video URL to download audio from, q to start downloading: ")
    if url == "q":
        adding_more = False
    else:
        video_urls.append(url)

for url in video_urls:
    download_audio(url)

print("All downloads completed!")