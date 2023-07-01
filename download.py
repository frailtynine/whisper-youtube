import yt_dlp


def download_audio(url):
    '''Downloads audio from Youtube'''
    yt_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with yt_dlp.YoutubeDL(yt_options) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        filename = ydl.prepare_filename(info_dict).rsplit('.', 1)[0] + '.mp3'
        ydl.download([url])
        return filename
