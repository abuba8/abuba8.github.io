# John Doe — Portfolio

Minimalist developer portfolio built with Flask. Inspired by clean personal-site layouts.

## Run

```bash
pip install flask
python app.py
```

Visit http://localhost:5000

## Structure

- `app.py` — Flask app + sample data (notes, videos, courses, projects)
- `templates/index.html` — single-page layout
- `static/css/styles.css` — styles with light/dark mode (auto via prefers-color-scheme)
- `static/js/main.js` — newsletter form handler

## Customize

Edit the `NOTES`, `VIDEOS`, `COURSES`, `PROJECTS` lists in `app.py` to swap in your own content. Update the hero text and avatar initials in `templates/index.html`.
