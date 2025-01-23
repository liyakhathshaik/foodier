from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
from utils.health import HealthUtils

# Load environment variables
load_dotenv()

class YouTubeRecommenderAgent:
    def __init__(self):
        """Initialize the YouTube API with the API key from the environment."""
        api_key = os.getenv("YOUTUBE_API_KEY")
        if not api_key:
            raise ValueError("Please set the YOUTUBE_API_KEY in the .env file.")
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def recommend_videos(self, user_data):
        """Fetch exercise videos based on user data."""
        goal = user_data.get("goal", "Healthy").lower()
        query = f"{goal} tips and tricks"

        # Customize query based on user's goal
        if goal == "gym bulking":
            query = "gym bulking tips and motivation"
        elif goal == "gym cutting":
            query = "gym cutting tips and motivation"
        elif goal == "pregnancy":
            query = "safe pregnancy exercises and tips"
        elif goal == "weight gain":
            query = "weight gain tips and motivation"
        elif goal == "weight loss":
            query = "weight loss tips and motivation"
        elif goal == "sports":
            query = "sports fitness and training tips"
        else:
            query = "healthy lifestyle tips and exercises"

        search_response = self.youtube.search().list(
            q=query,
            type='video',
            part='id,snippet',
            maxResults=5  # Limit to 5 results to stay within quota
        ).execute()
        videos = []
        for search_result in search_response.get('items', []):
            video_id = search_result['id']['videoId']
            video_title = search_result['snippet']['title']
            videos.append({
                "id": video_id,
                "title": video_title,
                "url": f"https://www.youtube.com/watch?v={video_id}"
            })
        return videos