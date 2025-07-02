from flask import Flask, render_template, request, send_file
from downloader import descargar_con_yt_dlp, descargar_carrusel
import os, shutil, uuid

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        carpeta = f"descargas/{uuid.uuid4()}"
        try:
            if "/p/" in url:
                descargar_carrusel(url, carpeta)
            else:
                descargar_con_yt_dlp(url, carpeta)
            shutil.make_archive(carpeta, 'zip', carpeta)
            return send_file(f"{carpeta}.zip", as_attachment=True)
        except Exception as e:
            return f"Error: {e}"
    return render_template("index.html")
