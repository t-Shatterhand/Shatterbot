from os import path
from urllib.parse import urlparse

import youtube_dl
import os


def get_video_id(url):
    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    o = urlparse(url)
    if o.netloc == 'youtu.be':
        return o.path[1:]
    elif o.netloc in ('www.youtube.com', 'youtube.com'):
        if o.path == '/watch':
            id_index = o.query.index('v=')
            return o.query[id_index + 2:id_index + 13]
        elif o.path[:7] == '/embed/':
            return o.path.split('/')[2]
        elif o.path[:3] == '/v/':
            return o.path.split('/')[2]
    return None  # not a link


def getMusic(update, context):
    if len(update.message.text.split(' ', 1)) == 1:
        update.message.reply_text("Please, enter the video URL after /getMusic (/getMusic <URL>)")
    else:
        video_query = update.message.text.split(' ', 1)[1]
        # update.message.reply_text("Your query was: " + video_query)
        video_id = get_video_id(video_query)
        if video_id is None:
            update.message.reply_text("Video not found - Enter valid youtube video URL")
        else:
            update.message.reply_text("Now wait a minute - the longer your video was, the longer it will take. "
                                      "Video conversion issues :)")
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_id])
                info_dict = ydl.extract_info(video_id, download=False)
                video_title = info_dict.get('title', None)
            normal_filename = str(video_title + ".mp3").replace("/", "-")
            for i in os.listdir():
                if i.endswith(".mp3"):
                    src = path.realpath(i)
                    dest = path.realpath(normal_filename)
                    os.rename(src, dest)
            context.bot.send_audio(chat_id=update.message.chat.id, audio=open(normal_filename, 'rb', ), timeout=200)
            os.remove(normal_filename)


# def youTubeSearch(query):
#    command=['youtube-dl', 'ytsearch:"' + query +'"', '-g']
#    result=subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split()
#    return result
