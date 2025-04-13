import yt_dlp

class Downloader():
    def __init__(self, urls, path):
        self.youtube_urls = urls
        self.path = path

    def download_audio(self):
        for url in self.youtube_urls:
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

                    'outtmpl': f'{self.path}/%(title)s.%(ext)s',  # Save file

                    #'quiet': True,  # Suppress all output
                    'no_warnings': True,  # Hide warnings
                    #'logger': None  # Disable logging
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    # Descargar
                    ydl.download([url])

            except Exception as e:
                #print(f"An error occurred: {e}")
                url = "Link no valido"
    
    # Audio is downloaded on Opus format, which sometimes not suppoer by windows media player 
    # Android works, for windows can use VLC Media Player
    def download_video(self):
        for url in self.youtube_urls:
            try:
                # Configure download options for 720p video
                ydl_opts = {
                    'format': 'bestvideo[height<=720]+bestaudio/best',  # Limit to 720p max
                    'outtmpl': f'{self.path}/%(title)s.%(ext)s',  # Save file
                    'merge_output_format': 'mp4',  # Ensure output is MP4

                    #'quiet': True,  # Suppress all output
                    'no_warnings': True,  # Hide warnings
                    #'logger': None  # Disable logging
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

            except Exception as e:
                #print(f"An error occurred: {e}")
                url = "Link no valido"