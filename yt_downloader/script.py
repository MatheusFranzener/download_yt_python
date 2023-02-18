import os
import shutil
from pytube import YouTube
from moviepy.editor import *

sairSistema = False

while sairSistema == False:
    link = input("Informe o link do vídeo a ser baixado: ")
    opcaoDownload = input("Escolha a opção para baixar \n1 - MP3 \n2 - MP4 \n>: ")

    video = YouTube(link)

    if (opcaoDownload == "1"):
        audio_stream = video.streams.filter(only_audio=True).order_by('abr').desc().first()
        audio_path = audio_stream.download()
        mp3_path = os.path.splitext(audio_path)[0] + '.mp3'
        audio = AudioFileClip(audio_path)
        audio.write_audiofile(mp3_path)
        audio.close()
        os.remove(audio_path)
        downloads_folder = os.path.expanduser('~/Downloads')
        shutil.move(mp3_path, downloads_folder)
        print("Download concluído com sucesso, salvo em: " + mp3_path)
    else:
        stream = video.streams.get_highest_resolution()
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        stream.download(download_path)
        print("Download concluído com sucesso, salvo em: " + download_path)

    opcao = int(input("Deseja baixar outro vídeo? \n1 - Sim \n2 - Não \n>: "))

    if (opcao == 2):
        print("Saindo do sistema...")
        sairSistema = True
