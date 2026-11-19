# Open Hand of Fredericksburg — concept website

A free website concept prepared for [Open Hand of Fredericksburg](https://www.instagram.com/openhandfredericksburg/), a faith-based nonprofit offering paid summer internships, mentoring and life-skills training to Fredericksburg-area youth.

> **This is a proposal, not Open Hand's official website.** Search engines are blocked (`robots.txt` and `noindex`), and online giving and forms are intentionally switched off until Open Hand approves the site.

## Content and brand sources

- Text: Open Hand's previous website (2022–2023, via the Internet Archive), its IRS Form 990 filings, and its Idealist profile.
- Logo: Open Hand's own logo, from its public Idealist profile (500×500 PNG). Replace with original artwork from Open Hand if available.
- Colors: taken from the logo's turquoise (`#00ADB9`).

## How it's built

Plain HTML and CSS served by GitHub Pages. No frameworks, no build service.

```
src/pages/      page content (one file per page)
src/partials/   shared header, footer, <head> and logo
assets/         stylesheet, script, images
build.py        combines partials + pages into the root .html files
```

### Editing

1. Edit a page in `src/pages/` (or the shared parts in `src/partials/`).
2. Run `python3 build.py` to regenerate the `.html` files in the root folder.
3. Commit and push. GitHub Pages publishes automatically.

## Going live (after Open Hand approves)

- [ ] Re-register `openhand-fred.org` in Open Hand's name, add a `CNAME` file, and point DNS to GitHub Pages
- [ ] Remove the concept banner (`src/partials/header.html`) and the footer note
- [ ] Remove `noindex` from `src/partials/head.html` and replace `robots.txt` to allow indexing
- [ ] Add a donation form (e.g. Zeffy) on `donate.html`
- [ ] Add GRAD application and volunteer interest forms (e.g. Google Forms)
- [ ] Confirm leadership names and bios, and add real photos (with photo releases)
- [ ] Move the repository to a GitHub organization owned by Open Hand
