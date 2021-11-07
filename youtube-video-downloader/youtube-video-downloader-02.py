from pytube import YouTube

url=input('enter URL of the YouTube video: ')
video = YouTube(url)

print('Getting Video Details...\n')
print('Title: ',video.title)
print('Thumbnail URL: ',video.thumbnail_url)
print('Length: ',video.length)
print('Description: ',video.description)
print('Views: ',video.views)

#set stream resolution
video = video.streams.get_highest_resolution()

#Download video
video.download()
print('video is downloaded.')
