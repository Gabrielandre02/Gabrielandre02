"""Rewrite the CREDLY block of README.md with the user's active Credly certifications."""
import datetime
import html
import json
import re
import sys
import urllib.request

USER = "gabriel.andre"
README = "README.md"
START, END = "<!-- CREDLY:START -->", "<!-- CREDLY:END -->"
INCLUDE = re.compile(r"Kubestronaut|^(CK|KC)|Certified|Certification")
EXCLUDE = re.compile(r"Skill Badge|Seller|Executive|Ver\.")


def fetch_badges():
    req = urllib.request.Request(
        f"https://www.credly.com/users/{USER}/badges.json",
        headers={"Accept": "application/json", "User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)["data"]


def is_wanted(badge, today):
    name = badge["badge_template"]["name"]
    expires = badge.get("expires_at_date")
    if expires and expires < today:
        return False
    return bool(INCLUDE.search(name)) and not EXCLUDE.search(name)


def render(badges):
    items = []
    for b in badges:
        tpl = b["badge_template"]
        name = html.escape(tpl["name"], quote=True)
        items.append(
            f'<a href="{tpl["url"]}"><img src="{b["image_url"]}" width="90" '
            f'alt="{name}" title="{name}" /></a>'
        )
    return '<p align="center">\n  ' + "\n  ".join(items) + "\n</p>"


def main():
    today = datetime.date.today().isoformat()
    badges = [b for b in fetch_badges() if is_wanted(b, today)]
    if not badges:
        sys.exit("no badges matched; refusing to blank the README block")
    badges.sort(key=lambda b: b["issued_at_date"], reverse=True)

    text = open(README, encoding="utf-8").read()
    block = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not block.search(text):
        sys.exit("CREDLY markers not found in README.md")
    new = block.sub(lambda _: f"{START}\n{render(badges)}\n{END}", text)
    open(README, "w", encoding="utf-8").write(new)
    print(f"{len(badges)} badges written")


if __name__ == "__main__":
    main()
