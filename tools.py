# tools.py

import os
from crewai_tools import YoutubeChannelSearchTool

def get_yt_tool():

    channel = os.getenv("YOUTUBE_CHANNEL")

    if not channel:
        raise ValueError("YOUTUBE_CHANNEL not set")

    return YoutubeChannelSearchTool(
        youtube_channel_handle=channel
    )