from youtube_transcript_api import YouTubeTranscriptApi
video_id="OuuO3lgh5oo"

# Replace with your proxy server details
proxy_server = "http://127.0.0.1:9090"

proxies = {
    "http": proxy_server,
    "https": proxy_server,
}


def transcriptor(video_id):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {video_id}')  # Press Ctrl+F8 to toggle the breakpoint.
    try:

        # Get the transcript using the proxy server
        transcript = YouTubeTranscriptApi.get_transcript(video_id, proxies=proxies)

        # Print the transcript
        for entry in transcript:
            print(entry['text'])

    except Exception as e:
        print(f"Error: {e}")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    transcriptor(video_id)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
