# Data Lab website

Static website for the Data Lab (Dr. Faezeh Ensan, Toronto Metropolitan University),
with a browser-based content manager powered by [Sveltia CMS](https://sveltiacms.app).

- **Live site:** https://towheedb.github.io/DataLab/
- **Content manager:** https://towheedb.github.io/DataLab/admin/

## How it works

```
content/          ← everything editable (YAML + Markdown); this is what the CMS edits
  settings.yml       site name, director, contact details, links
  pages/             home.yml, about.md, join.md
  areas/             one file per research theme
  publications/      one file per paper (abstract in the body)
  people/            one file per student / alumnus
assets/           ← stylesheet, logos, uploads
admin/            ← Sveltia CMS (index.html + config.yml)
build.py          ← turns content/ into the static site in site/
.github/workflows/deploy.yml  ← rebuilds and publishes to GitHub Pages on every push
```

Every time someone saves in the content manager, Sveltia commits the change to the
`main` branch, GitHub Actions runs `build.py`, and the new site is live within a minute or two.

## One-time setup

1. **Push this repository** to `TowheedB/DataLab` on GitHub (branch `main`).
2. **Enable GitHub Pages:** repository *Settings → Pages → Build and deployment → Source: GitHub Actions*.
3. Wait for the *Build and deploy site* workflow to finish (Actions tab). The site is now live.

If the repository ever moves, update `repo:` (and the two URLs) in `admin/config.yml`.

## Signing in to the content manager (GitHub access token)

Sveltia CMS talks to GitHub directly from the browser; no server or OAuth app is needed.

1. Make sure your GitHub account has **write access** to the repository.
2. Create a token at https://github.com/settings/personal-access-tokens/new
   - *Fine-grained token* (recommended): Repository access → *Only select repositories* → `DataLab`;
     Permissions → Repository → **Contents: Read and write**. Set an expiry you're comfortable with.
   - Or a *classic* token with the `repo` scope.
3. Open **/admin/** on the site, click **Sign In with Token**, and paste the token.

The token is stored only in your browser. Sign out (top-right menu) to forget it, and revoke
it on GitHub if it is ever exposed. Each person editing the site should use their own token.

## Editing content

| What you want to do | Where |
|---|---|
| Add or edit a paper, its abstract or DOI | **Publications** |
| Add a student, mark someone as alumni | **Students & Alumni** (untick *Current member*) |
| Change a research theme's text or icon | **Research themes** |
| Change the home tagline, About text, history timeline, Join Us text | **Pages** |
| Change contact details, director info, footer links | **Site settings** |

Publications are grouped by year automatically; the *Research theme* field drives the theme
filter and the "Selected papers" lists on the Research page.

## Building locally

```bash
pip install -r requirements.txt
python3 build.py        # writes ./site
python3 -m http.server -d site 8000   # then open http://localhost:8000
```

To try the CMS against your local files, Sveltia supports "Work with Local Repository"
on the sign-in screen (Chrome/Edge) when served over http://localhost.
