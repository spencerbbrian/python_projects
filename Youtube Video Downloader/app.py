from pytube import YouTube

link = input("Enter the video link here: ")
video = YouTube(link)

print("\n")
print("title: " + video.title)
print("\n")
print("Thumbnail Image:" + video.thumbnail_url)
print("\n")

#Get video with the highest resolution
stream = video.streams.get_by_itag(22)
stream.download()
print("Success!")