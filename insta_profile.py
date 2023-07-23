import instaloader
bot=instaloader.Instaloader()
profile = input("enter profile Name: ")
#password = input("Endter password:");
#bot.login(profile,password)
bot.download_profile(profile,profile_pic_only=True)
print("Download Successfully")