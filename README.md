# Cristina Rodriguez portfolio


![Alt Text](https://github.com/Yosolita1978/Portfolio2024/blob/main/video/Screen%20Recording%202024-01-19%20at%209.49.37%20PM.gif?raw=true)

## Author
Hello! I'm a project-driven software engineer with a strong focus on developing technical curricula and fostering interactive learning. My expertise lies in full-stack development, where I proficiently use technologies such as JavaScript, Python, Java, and React Native. I'm currently seeking a Curriculum developer role in the Greater Seattle Area. If you have a position that I should hear about, feel free to email yosola at Gmail.


---

## Project structure

Plain HTML, CSS and JavaScript. No framework, no build step, no dependencies
to install. Amplify serves these files directly.

```
index.html              /                 home
about/index.html        /about/
ventures/index.html     /ventures/
projects/index.html     /projects/
teaching/index.html     /teaching/
certifications/index.html
chat/index.html         /chat/
404.html                custom not-found page

css/tokens.css          colors, fonts, spacing  (change a value here, it updates everywhere)
css/base.css            reset, nav, hero, buttons, footer
css/pages.css           cards, project rows, certifications, chat

js/nav.js               mobile menu
js/hero.js              the typing effect + scroll reveal (shared by every page)
js/chat.js              click-to-load for the Hugging Face embed

cristina.md             /cristina.md      profile for AI agents (Markdown)

images/  docs/  ascii/  podfic/
```

## Editing pages

The HTML files are the source of truth. Edit them directly, then commit and
push; Amplify serves whatever is in the repo. Edit **styles** in `css/`.

The nav bar, footer and most of `<head>` are repeated in all eight HTML files
(the seven `index.html` pages plus `404.html`), because plain HTML has no way
to share them. A change to any of those means updating every file.

These are also edited by hand:

- `cristina.md`: profile for AI agents, linked from every page's `<head>` and
  from `llms.txt`. When you change it, update the "Last updated" date between
  the `last-modified` markers.
- `llms.txt` and `llms-full.txt`: summaries for AI crawlers.
- `sitemap.xml` and `robots.txt`: update `sitemap.xml` when a page is added
  or removed.

There used to be a generator, `tools/build.py`. It was removed because it got
out of sync with the HTML; it is still in the git history.

## Hosting

AWS Amplify, app ID `d1uudvswe15a0`, custom domain `www.yosola.co`.

URLs use a trailing slash (`/about/`, not `/about`). Every internal link,
the sitemap and all canonical tags follow that, so keep new links consistent.

Amplify redirect rules live in the console, not in this repo. The static-site
rules are:

```json
[
  {"source":"https://yosola.co","target":"https://www.yosola.co","status":"302"},
  {"source":"/<*>","target":"/404.html","status":"404"}
]
```

The second rule makes missing URLs return a real 404. The previous setting,
`{"source":"/<*>","target":"/index.html","status":"404-200"}`, was a
single-page-app catch-all that served the home page with a 200 for every dead
URL — that is the value to restore if the 404 rule ever needs rolling back.
