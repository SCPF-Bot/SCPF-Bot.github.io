Be thorough with your work.

---

SCPF-Bot.github.io — Private Website
======================================

A personal Jekyll site built with the Chulapa theme (gitdev-dark skin).
Hosted on GitHub Pages at: https://scpf-bot.github.io

Structure
---------
  _config.yml               — Jekyll site configuration (theme, nav, collections, SEO)
  _includes/series.html     — Reusable prev/next pagination for multi-page series
  index.html                — Landing page with navigation tiles
  404.md                    — Custom 404 error page
  pages/
    _collections/           — Jekyll collection source files (diary entries, e-tech)
    index.pages/            — Index/listing pages for each collection
    zero.to.stable/         — Financial survival guide (4 pages)
    archive/                — Personal archive of files and credentials
    misc/                   — To-do list, special thanks

Collections
-----------
  diary.index.2019 – diary.index.2025   — Daily diary entries addressed to Babii
  e.tech                                — Educational pages on Web 1.0 / 2.0 / 3.0

Theme
-----
  Remote theme : dieghernan/chulapa
  Skin         : gitdev-dark
  Font         : Ubuntu Mono (Google Fonts)

Plugins
-------
  jekyll-github-metadata, jekyll-paginate,
  jekyll-include-cache, jekyll-sitemap

Notes
-----
  - All front matter uses single YAML block (no duplicate --- separators).
  - Absolute URLs replaced with root-relative paths for portability.
  - Email links use mailto: protocol.
  - series.html supports accessible prev/next navigation with aria-labels.
