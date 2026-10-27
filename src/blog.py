"""Loads blog posts written in Decap CMS (content/posts/*.md).

Each post is a Markdown file with front matter:
    title, date (YYYY-MM-DD), category, cover (/assets/img/blog/...), summary (optional)
The file name is the post's web address: content/posts/my-post.md -> /post/my-post
Cover photos uploaded through the CMS are resized to web-friendly .webp files at build time.
"""
from datetime import date, datetime
from pathlib import Path
import html
import re

import markdown
import yaml

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT / "content" / "posts"
SITE_DIR = ROOT / "site"
OPT_DIR = SITE_DIR / "assets" / "img" / "blog" / "web"


def _optimise(cover: str) -> str:
    """Return a web-sized .webp version of an uploaded cover photo (falls back to the original)."""
    if not cover:
        return ""
    src = SITE_DIR / cover.lstrip("/")
    if not src.exists() or "/web/" in cover:
        return cover
    try:
        from PIL import Image, ImageOps
    except ImportError:
        return cover
    OPT_DIR.mkdir(parents=True, exist_ok=True)
    out = OPT_DIR / (src.stem + ".webp")
    if not out.exists() or out.stat().st_mtime < src.stat().st_mtime:
        im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
        im.thumbnail((1600, 1600))
        im.save(out, "WEBP", quality=80)
    return "/" + str(out.relative_to(SITE_DIR)).replace("\\", "/")


def _as_date(v):
    if isinstance(v, datetime):
        return v.date()
    if isinstance(v, date):
        return v
    try:
        return datetime.fromisoformat(str(v)[:10]).date()
    except ValueError:
        return date.today()


def load_posts():
    posts = []
    for f in sorted(POSTS_DIR.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.S)
        meta, body = (yaml.safe_load(m.group(1)) or {}, m.group(2)) if m else ({}, text)
        if meta.get("draft"):
            continue
        d = _as_date(meta.get("date"))
        body_html = markdown.markdown(body, extensions=["extra", "sane_lists"])
        body_html = body_html.replace("<ol>", '<ol class="post-list">').replace("<ul>", '<ul class="post-list">')
        plain = re.sub(r"<[^>]+>", "", body_html).strip()
        summary = (meta.get("summary") or "").strip() or (plain[:155].rsplit(" ", 1)[0] + "...")
        posts.append({
            "slug": f.stem,
            "title": str(meta.get("title") or f.stem),
            "cat": str(meta.get("category") or "Ideas"),
            "date_obj": d,
            "date": f"{d:%B} {d.day}, {d.year}",
            "img": _optimise(str(meta.get("cover") or "")),
            "summary": html.escape(summary, quote=True),
            "body_html": body_html,
        })
    posts.sort(key=lambda p: p["date_obj"], reverse=True)
    return posts
