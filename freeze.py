import os, shutil
import app as flaskapp

OUT = "build"
if os.path.exists(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)

client = flaskapp.app.test_client()

def save(url, path):
    resp = client.get(url)
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(resp.get_data(as_text=True))
    print(f"{url} -> {path} ({resp.status_code})")

# Home + CV
save("/", "index.html")
save("/cv", "cv/index.html")

# Every publication and project, driven by the data in app.py
for p in flaskapp.PUBLICATIONS:
    save(f"/publications/{p['slug']}", f"publications/{p['slug']}/index.html")
for p in flaskapp.PROJECTS:
    save(f"/projects/{p['slug']}", f"projects/{p['slug']}/index.html")

# Copy static assets and disable Jekyll processing
shutil.copytree("static", os.path.join(OUT, "static"))
open(os.path.join(OUT, ".nojekyll"), "w").close()

print("DONE — output in ./build")