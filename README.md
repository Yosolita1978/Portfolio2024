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

images/  docs/  ascii/  podfic/     unchanged, not generated
```

## Editing pages

The nav bar and footer are repeated in all eight HTML files, because plain
HTML has no way to share them. So they are generated from one source:

```
python3 tools/build.py
```

Edit page **content** in `tools/build.py`, then re-run it. Edit **styles** in
`css/` directly — the generator never touches those.

`tools/build.py` overwrites the eight `index.html` files plus `404.html`,
`sitemap.xml` and `robots.txt`. It does not touch `css/`, `js/`, `images/`,
`docs/`, `ascii/` or `podfic/`.

The site does not need Python to run or deploy. The generator is only there
so the shared nav and footer stay in sync.

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
