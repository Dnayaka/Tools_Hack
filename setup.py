import os

os.system("pkg install git")
os.system("git clone https://github.com/cutipu/HASOKI.git")
os.system("git clone https://github.com/HunxByts/GhostTrack.git")
os.system("git clone https://github.com/KasRoudra/MaxPhisher.git")
os.system("git clone https://github.com/Dnayaka/CRACK_FB.git")
os.system("pip3 install beautifulsoup4")
os.system("pip3 install phonenumbers")
os.system("pip3 install rich")
os.system("pip3 install requests")
os.system("pip3 install cloudscraper")
os.system("pip3 install socks")
os.system("pip3 install pysocks")
os.system("pip3 install colorama")
os.system("pip3 install undetected_chromedriver")
os.system("pip3 install httpx")

if os.name == "nt":
    pass
else:
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")

print("Done.")
