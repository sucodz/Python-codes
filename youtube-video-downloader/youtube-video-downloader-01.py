from pytube import YouTube

url=input('enter URL of the YouTube video: ')
video = YouTube(url)

print('Getting Video Details...\n')
print('Title: ',video.title)
print('Thumbnail URL: ',video.thumbnail_url)
print('Length: ',video.length)
print('Description: ',video.description)
print('Views: ',video.views)

print('*************  available resolutions:  ************* \n')
for stream in video.streams.filter(progressive=True):
    print(' ************* ', stream.resolution)
res = input('\n*************  choose a resolution:  ')

video.streams.filter(res=res, file_extension='mp4').first().download("Videos/")
print('video is downloaded.')
