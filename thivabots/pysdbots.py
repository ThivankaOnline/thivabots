import requests


headers={'Content-Type': 'application/json'}


def anime_logo(name):
    API = f"https://api.thivabots.tk/anime-logo?name={name}"
    req = requests.get(API).url
    return(req)

def tiktok(url):
    API = f"https://api.thivabots.tk/tiktok?url={url}"
    req = requests.get(API).json()
    return(req)

def apod():
    API = "https://api.thivabots.tk/apod"
    req = requests.get(API).json()
    return(req)

def detect_lang(text):
    req = requests.get(f"https://api.thivabots.tk/detect?text={text}").json()
    return(req)

def write(text):
    body = {
        "text": f"{text}"
    }
    url = "https://api.thivabots.tk/write"
    req = requests.post(url=url, headers=headers, json=body).url
    return(req)

def chk(cc):
    API = f"https://api.thivabots.tk/chk?cc={cc}"
    req = requests.get(API).json()
    return(req)

def sk_checker(key):
    req = requests.get(f"https://api.thivabots.tk/sk?key={key}").json()
    return(req)

def lyrics(song):
    req = requests.get(f"https://api.thivabots.tk/lyrics?song={song}").json()
    return(req)

def ipinfo(ip):
    req = requests.get(f"https://api.thivabots.tk/ipinfo?ip={ip}").json()
    return(req)

def hirunews():
    req = requests.get("https://api.thivabots.tk/hirunews").json()
    return(req)

def logohq(text):
    req = requests.get(f"https://api.thivabots.tk/logohq?text={text}").url
    return(req)

def fakeinfo():
    req = requests.get("https://api.thivabots.tk/fakeinfo").json()
    return(req)


a = anime_logo("ThivankaJa")
print(a)