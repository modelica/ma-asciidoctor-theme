# download the webfonts

import os
from pathlib import Path
import re
from urllib.request import urlretrieve

print("Downloading webfonts...")

theme_dir = Path(__file__).parent
css_file = theme_dir / "css" / "fonts.css"

lines = []

with open(css_file) as css:
    for line in css:
        pattern = r'https\://fonts\.gstatic\.com/[^\s]+\.woff2'
        for url in re.findall(pattern, line):
            print(url)
            segments = url.split("/")
            name, version, filename = segments[-3:]
            font_dir = theme_dir / "fonts" / name / version
            os.makedirs(font_dir, exist_ok=True)
            urlretrieve(url, font_dir / filename)
        lines.append(line.replace("https://fonts.gstatic.com/s/", "../fonts/"))

with open(css_file, "w") as css:
    css.writelines(lines)
