import json
import os
from googleapiclient.discovery import build
from helper.youtube_api_manual import channel_id


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.response = None
        self.channel_id = channel_id

        # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('API_KEY')

        # Эта строка создает объект youtube, который будет использоваться для взаимодействия с YouTube API.
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""

        self.response = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        channel_info = json.dumps(self.response, indent=2, ensure_ascii=False)
        return channel_info
