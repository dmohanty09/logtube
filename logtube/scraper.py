import sys
import os

from youtube_transcript_api import YouTubeTranscriptApi
# import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

# Get credentials and create an API client
# flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
# credentials = flow.run_console()
api_service_name = "youtube"
api_version = "v3"


def transcribe_video(video_id):
    print(f'Transcribing Video ID: {video_id}')
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e:
        transcript = []
        print(e, file=sys.stderr)
    return transcript


def transcribe_videos(video_ids):
    for num, video_id in enumerate(video_ids, start=1):
        print(f'Playlist Video {num} of {len(video_ids)}')
        transcript = transcribe_video(video_id)
        print(f'Transcript: {transcript}')


class YoutubeScraper:

    GOOGLE_APPLICATION_CREDENTIALS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

    def __init__(self):
        self.youtube = googleapiclient.discovery.build(api_service_name,
                                                       api_version,
                                                       developerKey=YoutubeScraper.GOOGLE_APPLICATION_CREDENTIALS)

    def get_most_popular(self, page_token=None):
        print('Getting first 50 popular videos..')
        request = self.youtube.videos().list(
            part="statistics",
            chart="mostPopular",
            maxResults=50,
            pageToken=page_token,
            regionCode="US"
        )
        response = request.execute()
        return response

