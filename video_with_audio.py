from pytube import YouTube
link = input("enter link : ") #user can enter the link.
yt = YouTube(link) #all the data we collect from.
print(yt.title) #for checking our video title.
print(yt.thumbnail_url) #for checking our video thumbnail.
videos=yt.streams.all() #this is for select video resolution.
vid_resolutions=list(enumerate(videos)) #all videose in multiple resolution in order to list.
for i in vid_resolutions:   #for loop is working on resolution which is given in our video.ex.144p,260p,340p as it is..
    print(i)
strm = int(input("select your resolution: ")) #we need to select our resolution in int. so i take the input in int.
videos[strm].download() #we will select the video resolution in int. (press enter).
print("𝕕𝕠𝕨𝕟𝕝𝕠𝕒𝕕 𝕤𝕦𝕔𝕔𝕖𝕤𝕤𝕗𝕦𝕝") #result are there.













