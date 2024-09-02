import sys
from youtube_transcript_api import YouTubeTranscriptApi
import requests

# video_id="OuuO3lgh5oo"

if len(sys.argv) != 2:
    print("Usage: python script.py <video_id>")
    sys.exit(1)

video_id = sys.argv[1]
print(f"Procesando video id: {video_id}")


# Set the SOCKS4 proxy server details
proxy_server = "127.0.0.1"
proxy_port = "9090"

# Configure the proxies
proxies = {
    "http": f"http://{proxy_server}:{proxy_port}",
    "https": f"http://{proxy_server}:{proxy_port}",
}

requests.proxies = proxies


def transcriptor(str_video_id, str_proxies):
    try:

        # Get the transcript using the proxy server
        transcript = YouTubeTranscriptApi.get_transcript(str_video_id, str_proxies)
        # transcript = YouTubeTranscriptApi.get_transcript(str_video_id, proxies=proxies)

        # Print the transcript
        for entry in transcript:
            print(entry['text'])

    except Exception as e:
        print(f"Error: {e}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    transcriptor(video_id, requests.proxies)

