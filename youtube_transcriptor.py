import sys
from youtube_transcript_api import YouTubeTranscriptApi

# Video ejemplo:  https://www.youtube.com/watch?v=OuuO3lgh5oo
# video_id=OuuO3lgh5oo

def transcriptor(str_video_id, str_archivo):
    try:

        transcript = YouTubeTranscriptApi.get_transcript(str_video_id, languages=['es'])

        texto = ""

        # obtengo transcripción línea a línea
        for entry in transcript:
            texto += entry['text'] + "\n"

        # envío la transcripción a un archivo con el video_id.txt
        with open(str_archivo, "w") as file:
            file.write(texto)

        print(f"Transcripción en el archivo {str_archivo}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    
    # Verifico que haya llegado el parámetro que tendría el video_id. Si no está -> exit
    if len(sys.argv) != 2:
        print("Uso desde línea de comandos: python main.py <video_id>")
        sys.exit(1)

    video_id = sys.argv[1]
    print(f"Procesando video id: {video_id}")
    archivo = sys.argv[1]+".txt"

    transcriptor(video_id, archivo)

