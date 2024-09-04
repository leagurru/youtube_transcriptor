import sys
from youtube_transcript_api import YouTubeTranscriptApi

# Video ejemplo:  https://www.youtube.com/watch?v=OuuO3lgh5oo
# video_id=OuuO3lgh5oo

def transcriptor(str_video_id, str_language_transcripcion, str_language_traduccion):
    try:

        # retrieve the available transcripts
        transcript_list = YouTubeTranscriptApi.list_transcripts(str_video_id)
        transcript = transcript_list.find_transcript([str_language_transcripcion])

        # transcripcion en el lenguaje original
        transcription = YouTubeTranscriptApi.get_transcript(str_video_id, languages=[str_language_transcripcion])

        texto = ""

        # obtengo transcripción línea a línea
        for entry in transcription:
            texto += entry['text'] + "\n"

        str_archivo_transcripcion = str_language_transcripcion + "-" + str_video_id + ".txt"
        # envío la transcripción a un archivo con el lenguaje-video_id.txt
        with open(str_archivo_transcripcion, "w") as file:
            file.write(texto)

        print(f"Transcripción en el archivo {str_archivo_transcripcion}")


        if language_traduccion:
            # Traducción de la transcripción
            # fetch the actual transcript data
            transcript.fetch()

            # translating the transcript will return another transcript object
            traduccion = transcript.translate(str_language_traduccion).fetch()
            # print(transcript.translate(str_language_traduccion).fetch())

            # obtengo la traducción línea a línea
            texto_traducido = ""
            for entry in traduccion:
                texto_traducido += entry['text'] + "\n"

            # envío la traducción a un archivo con el lenguaje-video_id.txt
            str_archivo_traduccion = str_language_traduccion + "-" + str_video_id + ".txt"
            with open(str_archivo_traduccion, "w") as file:
                file.write(texto_traducido)

            print(f"Traducción en el archivo {str_archivo_traduccion}")


    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    
    # Verifico que haya llegado el parámetro que tendría el video_id y el language. Si no está -> exit
    if len(sys.argv) < 3:
        print("Uso desde línea de comandos: python main.py <video_id> <language>")
        sys.exit(1)

    video_id = sys.argv[1]
    language_transcripcion = sys.argv[2]

    if len(sys.argv) == 4:
        language_traduccion = sys.argv[3]
    else:
        language_traduccion = False

    print(language_traduccion)

    print(f"Procesando video id: {video_id} para el lenguaje '{language_transcripcion}'")

    if language_traduccion:
        print(f"Se intentará traducir al lenguaje '{language_traduccion}'")

    transcriptor(video_id, language_transcripcion, language_traduccion)



