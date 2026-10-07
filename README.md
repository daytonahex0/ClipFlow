# ClipFlow

Marketing site and working production planner for ClipFlow, an AI-powered short-form content production system.

Single static file, no build tools or dependencies required to run.

## Run

Open `dist/index.html` in a browser, or serve the folder with any static host.

## What works

- Responsive site with light and dark themes (follows the system, with a manual toggle)
- Production board: add a clip, get a script outline and timed shot list, move it through Ideas, Scripting, Producing, Review and Ready
- Quality scorer: rate eight criteria, get a verdict and the fixes to make first
- Board and theme are saved in the browser's localStorage only. Nothing is sent anywhere.

## What it does not include

No video generation, accounts, analytics collection or pricing. The page states this where relevant and shows no invented figures.

## Layout

- `src/clipflow.html` source fragment (title, fonts, styles, markup, script)
- `build.py` wraps it into a full page: `python3 build.py` writes `dist/index.html`
- `dist/index.html` the deployable page

Fonts load from Google Fonts. If blocked, system fonts are used.
