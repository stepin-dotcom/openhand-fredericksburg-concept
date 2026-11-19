"""Assemble the site: wraps each file in src/pages/ with the shared header and footer.

Usage:  python3 build.py
Edit page content in src/pages/*.html, shared parts in src/partials/, then re-run.
Each page file starts with two comment lines:
  <!-- title: Page title -->
  <!-- description: One-sentence summary for search/social -->
"""
import pathlib, re

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src"
HEAD = (SRC / "partials" / "head.html").read_text()
HEADER = (SRC / "partials" / "header.html").read_text()
FOOTER = (SRC / "partials" / "footer.html").read_text()

NAV = [("index.html", "Home"), ("about.html", "About"), ("programs.html", "Programs"),
       ("get-involved.html", "Get Involved"), ("contact.html", "Contact")]

def nav_html(current):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    items.append('<li><a class="btn btn-gold" href="donate.html">Donate</a></li>')
    return "\n          ".join(items)

for page in sorted((SRC / "pages").glob("*.html")):
    raw = page.read_text()
    title = re.search(r"<!-- title: (.*?) -->", raw).group(1)
    desc = re.search(r"<!-- description: (.*?) -->", raw).group(1)
    body = re.sub(r"<!-- (title|description): .*? -->\n?", "", raw)
    full_title = "Open Hand of Fredericksburg" if page.name == "index.html" else f"{title} | Open Hand of Fredericksburg"
    html = (HEAD.replace("{{title}}", full_title).replace("{{description}}", desc)
            + HEADER.replace("{{nav}}", nav_html(page.name))
            + body
            + FOOTER)
    (ROOT / page.name).write_text(html)
    print("built", page.name)
