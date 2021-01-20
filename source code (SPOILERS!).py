#made by TetrisLitHub, Enjoy ;)
#btw this contains spoilers, continue at your own risk!!


import getpass, os, time, urllib.request
username = getpass.getuser()
input("Welcome to True or False! type 'T' for true, 'F' for false, and enter for unsure/don't know in response to each question of the survey.")
input("True or False: I like surveys in general.")
input("True or False: What is your gender? (T for male, F for female, press enter for other)")
input("True or false: You are on the internet at least one hour per day.")
input("True or false: __SAMPLE__TEXT__")
input("True or false: __SAMPLE__TEXT__")
input("True or false: You like to meet new people!")
input("True or false: You are home alone")
input("True or false: Someone would hear you if you screamed as loud as possible")
input("True or false: the nearest police station is within 5 miles of your current location.")
input("True or false: you know at least one martial art, and/or are in possesion of a self defense weapon.")
input("True or false: The person behind you is friendly.")
input(f"True or False: {username}")
page = urllib.request.urlopen('http://api.ipify.org/')
print("True or False:", page.read())
time.sleep(1.5)
try: f = open(f"C:/Users/{username}/Desktop/ISEEYOU.vbs", "x")
except: f = open(f"C:/Users/{username}/Desktop/ISEEYOU.vbs", "w")
f.write("x=msgbox('CRITICAL ERROR', 0+16, 'Windows Defender has detected 21 viruses on your computer.)")
f.close()
for x in range(0,5):
    os.startfile(f"C:/Users/{username}/Desktop/ISEEYOU.vbs")
input("True or false: thHereEisnoeLsPcapethHereEisnoeLsPcapethHereEisnoeLsPcapethHereEisnoeLsPcape")
input(f'True or False: {username} liked True or False and would recommend it to other people')
input(f'True or False: goodbye for now, {username} ;)')
for x in range(0,10):
    os.startfile(f"C:/Users/{username}/Desktop/ISEEYOU.vbs")
input('press enter to close')
