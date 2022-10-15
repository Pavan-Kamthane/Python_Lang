import instaloader
insta = instaloader.Instaloader()

# Ask Username
user = input("Enter the username: ")
# Downloader Profile Pic
insta.download_profile(user, profile_pic_only=True)
# Download Photos
insta.download_profile(user, profile_pic_only=False)
