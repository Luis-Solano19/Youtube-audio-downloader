from ytdownloader import Downloader

option = int(input("Elige una opcion a descargar. \n1.-Video(s)\n2.-Audio(s): "))

video_urls = []
adding_more = True

while adding_more:
    url = input("Link/URL de youtube, [q] para comenzar con la(s) descarga(s): ")
    
    if url == "q":
        adding_more = False
    else:
        video_urls.append(url)

if option == 1:
    ytdown = Downloader(urls=video_urls, path="videos")
    ytdown.download_video()

if option == 2:
    ytdown = Downloader(urls=video_urls, path="audios")
    ytdown.download_audio()


print("DESCARGAS FINALIZADAS")