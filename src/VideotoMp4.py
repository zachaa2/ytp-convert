from pytube import YouTube
from pytube import Playlist
import glob
from moviepy.editor import VideoFileClip, concatenate_videoclips

class PlaylistMerger:
    def __init__(self, playlist_url):
        self.playlist_link = playlist_url
        self.fileCtr = 0

    def getFilenamesFromBin(self):
        lis = glob.glob("bin\\*.mp4")
        return lis    

    def download(self, link):

        youtubeObj = YouTube(link)
        youtubeObj = youtubeObj.streams.get_highest_resolution()
        try:
            youtubeObj.download(output_path="bin", filename_prefix=str(self.fileCtr) + "_")
            self.fileCtr += 1
        except:
            print("AN ERROR OCCURED")
    
    def getLinksFromPlaylist(self, playlist_link):
        playlist = Playlist(playlist_link)
        links = []
        ctr = 1
        for link in playlist:
            if link not in playlist:
                links.append(link)
            else:
                links.append(link + str(ctr))
                ctr += 1
        print(links)
        return links
    
    def downloadVideoList(self, url):
        urls = self.getLinksFromPlaylist(url)
        for i in range(len(urls)):
            self.download(urls[i])
    
    
if __name__ == "__main__":
    playlist = "https://www.youtube.com/playlist?list=PLERI1_ESTKAwVhUliNnKieLrsK8M75ynb"
    link = "https://www.youtube.com/watch?v=5ZKdReHSARQ"

    pg = PlaylistMerger(playlist_url=playlist)
    pg.downloadVideoList(playlist)
    print(pg.getFilenamesFromBin())
