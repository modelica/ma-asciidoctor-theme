from pathlib import Path

lines = []
index_path = Path(__file__).parent.parent / "index.html"

urls = {
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css":
        "theme/css/font-awesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.3/styles/github.min.css":
        "theme/css/github.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js":
        "theme/js/MathJax.js",
    "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/9.18.3/highlight.min.js":
        "theme/js/highlight.min.js",
}

with open(index_path, mode="r", encoding="utf-8") as index:
    for line in index:
        for k, v in urls.items():
            line = line.replace(k, v)
        lines.append(line)

with open(index_path, "w", encoding="utf-8") as index:
    index.writelines(lines)
