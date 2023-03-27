# This is a sample Python script.
import csv

import youtube_dl
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from youtube_search import YoutubeSearch
from youtube_dl import YoutubeDL

links = []
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'verbose': True,
    'ignoreerrors': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


def search(name):
    # Use a breakpoint in the code line below to debug your script.
    results = YoutubeSearch(name, max_results=10).to_dict()
    return results[0]['url_suffix']


def extract_meta(video_url):
    meta = ydl.extract_info(
        video_url, download=False)

    return meta


if __name__ == '__main__':

    with open('songs.csv', 'r') as csv_file:
        # create a CSV reader object
        csv_reader = csv.reader(csv_file)

        # skip the header row if there is one
        next(csv_reader)

        # iterate over the rows and pass data to next method
        for row in csv_reader:
            artist = row[0]
            song = row[1]
            # pass the artist and song to the next method
            search_res = search(artist + ' ' + song)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                try:
                    url = 'https://www.youtube.com/' + search_res
                    meta = extract_meta(url)
                    download = ydl.download([url])
                except Exception as e:
                    print('Error at ' + url, e)
            links.append('url')
