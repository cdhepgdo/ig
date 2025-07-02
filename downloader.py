import subprocess, os, re, requests, json

def es_carrusel(html):
    return "edge_sidecar_to_children" in html

def descargar_con_yt_dlp(url, carpeta="descargas"):
    os.makedirs(carpeta, exist_ok=True)
    comando = [
        "yt-dlp",
        "-o", f"{carpeta}/%(title)s.%(ext)s",
        url
    ]
    subprocess.run(comando, check=True)

def descargar_carrusel(url, carpeta="descargas"):
    os.makedirs(carpeta, exist_ok=True)
    headers = {"User-Agent": "Mozilla/5.0"}
    html = requests.get(url, headers=headers).text
    json_data = re.search(r"window\._sharedData\s*=\s*(\{.*?\});</script>", html)
    data = json.loads(json_data.group(1))
    media = data["entry_data"]["PostPage"][0]["graphql"]["shortcode_media"]
    for i, edge in enumerate(media["edge_sidecar_to_children"]["edges"], 1):
        node = edge["node"]
        url_media = node["video_url"] if node["is_video"] else node["display_url"]
        ext = "mp4" if node["is_video"] else "jpg"
        nombre = f"{carpeta}/item_{i}.{ext}"
        with open(nombre, "wb") as f:
            f.write(requests.get(url_media).content)
