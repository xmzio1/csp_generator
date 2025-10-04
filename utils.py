import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import hashlib
import json
import os

# إنشاء مجلد reports إذا لم يكن موجودًا
os.makedirs("reports", exist_ok=True)

def get_hash(content):
    """توليد hash SHA256 من نص"""
    h = hashlib.sha256()
    h.update(content.encode('utf-8'))
    return f"'sha256-{h.digest().hex()}'"

def extract_resources(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    resources = {
        "script-src": set(),
        "style-src": set(),
        "img-src": set(),
        "font-src": set(),
        "frame-src": set(),
        "connect-src": set(),
        "inline-scripts": set(),
        "inline-styles": set()
    }

    # سكربتات خارجية وداخلية
    for script in soup.find_all("script"):
        if script.get('src'):
            domain = urlparse(script['src']).netloc
            if domain: resources["script-src"].add(f"https://{domain}")
        elif script.string:
            resources["inline-scripts"].add(get_hash(script.string.strip()))

    # ستايلات خارجية وداخلية
    for style in soup.find_all("style"):
        if style.string:
            resources["inline-styles"].add(get_hash(style.string.strip()))
    for link in soup.find_all("link", rel="stylesheet", href=True):
        domain = urlparse(link['href']).netloc
        if domain: resources["style-src"].add(f"https://{domain}")

    # صور
    for img in soup.find_all("img", src=True):
        domain = urlparse(img['src']).netloc
        if domain: resources["img-src"].add(f"https://{domain}")

    # iframes
    for frame in soup.find_all("iframe", src=True):
        domain = urlparse(frame['src']).netloc
        if domain: resources["frame-src"].add(f"https://{domain}")

    return resources

def generate_csp(resources):
    csp_parts = []
    for key, values in resources.items():
        if values:
            csp_parts.append(f"{key} " + " ".join(values))
    return "; ".join(csp_parts)

def save_report(url, resources, csp):
    domain = urlparse(url).netloc
    data = {
        "url": url,
        "resources": {k: list(v) for k,v in resources.items()},
        "csp": csp
    }
    with open(f"reports/{domain}.json", "w") as f:
        json.dump(data, f, indent=4)
    print(f"[+] CSP report saved: reports/{domain}.json")
