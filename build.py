#!/usr/bin/env python3
"""
Data Lab website builder.

Reads everything under ./content (edited through Sveltia CMS at /admin/),
renders the static site into ./site.  Run:  python3 build.py
"""
import os, re, glob, html, shutil
import yaml, markdown

ROOT = os.path.dirname(os.path.abspath(__file__))
CONTENT = os.path.join(ROOT, "content")
OUT = os.path.join(ROOT, "site")

# --------------------------------------------------------------- loading ---
def read_md(path):
    """Return (frontmatter dict, body markdown) for a file with optional --- frontmatter."""
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if m:
        return (yaml.safe_load(m.group(1)) or {}), m.group(2)
    return {}, text

def read_yml(path):
    return yaml.safe_load(open(path, encoding="utf-8")) or {}

def load_folder(name):
    items = []
    for p in sorted(glob.glob(os.path.join(CONTENT, name, "*.md"))):
        fm, body = read_md(p)
        fm["_body"] = body.strip()
        fm["_slug"] = os.path.splitext(os.path.basename(p))[0]
        items.append(fm)
    return items

SETTINGS = read_yml(os.path.join(CONTENT, "settings.yml"))
HOME     = read_yml(os.path.join(CONTENT, "pages", "home.yml"))
ABOUT_FM, ABOUT_BODY = read_md(os.path.join(CONTENT, "pages", "about.md"))
JOIN_FM,  JOIN_BODY  = read_md(os.path.join(CONTENT, "pages", "join.md"))

AREAS  = sorted(load_folder("areas"), key=lambda a: a.get("order", 99))
PUBS   = sorted(load_folder("publications"), key=lambda p: (-int(p.get("year", 0)), p.get("order", 999)))
PEOPLE = sorted(load_folder("people"), key=lambda p: (not p.get("current", False), p.get("name", "").split()[-1]))
GROUPS = SETTINGS.get("groups", [])
DIR    = SETTINGS.get("director", {})
PI     = DIR.get("name", "").replace("Dr. ", "")

# --------------------------------------------------------------- helpers ---
def e(s): return html.escape(str(s), quote=True)
def md(s): return markdown.markdown(s or "", extensions=[])
def md_inline(s): return re.sub(r"^<p>|</p>$", "", md(s).strip())
def bold_pi(authors):
    return e(authors).replace(e(PI), f"<strong>{e(PI)}</strong>") if PI else e(authors)

NAV = [("index.html","Home"),("about.html","About"),("research.html","Research"),("publications.html","Publications"),
       ("students.html","Students"),("join.html","Join Us"),("contact.html","Contact")]

ICONS = {
 "graph":    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="5" cy="6" r="2.5"/><circle cx="19" cy="6" r="2.5"/><circle cx="12" cy="18" r="2.5"/><path d="M7 7.5l3.5 8M17 7.5l-3.5 8M7.5 6h9"/></svg>',
 "search":   '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L21 21M7.5 10.5h6M10.5 7.5v6"/></svg>',
 "document": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4M9 12h6M9 16h6M9 8h2"/></svg>',
 "shield":   '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 3v6c0 4.5-3.4 8-8 9-4.6-1-8-4.5-8-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
 "brain":    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 4a3 3 0 0 0-3 3v1a3 3 0 0 0-2 3 3 3 0 0 0 2 3v1a3 3 0 0 0 3 3h1V4zM15 4a3 3 0 0 1 3 3v1a3 3 0 0 1 2 3 3 3 0 0 1-2 3v1a3 3 0 0 1-3 3h-1V4z"/></svg>',
 "chat":     '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/></svg>',
}
def icon(a): return ICONS.get(a.get("icon", "graph"), ICONS["graph"])

LOGO_LIGHT = '<svg class="brand-mark" viewBox="0 0 100 100" aria-hidden="true"><path fill="#4C1D95" fill-rule="evenodd" d="M20 10 H50 A40 40 0 0 1 50 90 H20 Z M34 24 V76 H50 A26 26 0 0 0 50 24 Z"/><path fill="#10B981" stroke="#fff" stroke-width="5" stroke-linejoin="round" paint-order="stroke" d="M20 10 H34 V76 H64 V90 H20 Z"/></svg>'
LOGO_DARK  = '<svg class="brand-mark" viewBox="0 0 100 100" aria-hidden="true"><path fill="#fff" fill-rule="evenodd" d="M20 10 H50 A40 40 0 0 1 50 90 H20 Z M34 24 V76 H50 A26 26 0 0 0 50 24 Z"/><path fill="#34D399" stroke="#2E1065" stroke-width="5" stroke-linejoin="round" paint-order="stroke" d="M20 10 H34 V76 H64 V90 H20 Z"/></svg>'

def layout(page, title, body):
    S = SETTINGS
    links = "".join(f'<a href="{href}"{" class=active aria-current=page" if href==page else ""}>{label}</a>' for href,label in NAV)
    ext = "".join(f'<a href="{e(l["url"])}" target="_blank" rel="noopener">{e(l["label"])}</a>' for l in S.get("links", [])[:4])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} · {e(S["site_name"])}</title>
<meta name="description" content="{e(S["site_name"])} — {e(DIR.get("name",""))}'s research group at {e(S["university"])}.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap nav-row">
    <a class="brand" href="index.html">{LOGO_LIGHT}{e(S["site_name"])}</a>
    <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false" onclick="document.body.classList.toggle('nav-open');this.setAttribute('aria-expanded',document.body.classList.contains('nav-open'))"><span></span><span></span><span></span></button>
    <nav class="nav" aria-label="Main">{links}</nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap foot-grid">
    <div>
      <div class="foot-brands"><div class="brand foot-brand">{LOGO_DARK}{e(S["site_name"])}</div><a class="tmu-logo" href="{e(S["university_url"])}" target="_blank" rel="noopener" aria-label="{e(S["university"])}"><img src="assets/tmu-logo.png" alt="{e(S["university"])}"></a></div>
      <p>{e(DIR.get("name",""))}'s research group<br>{e(S["department"])}<br>{e(S["university"])}</p>
    </div>
    <div>
      <h4>Explore</h4>
      <a href="research.html">Research</a><a href="publications.html">Publications</a><a href="students.html">Students</a><a href="join.html">Join Us</a>
    </div>
    <div>
      <h4>Elsewhere</h4>
      {ext}
    </div>
  </div>
  <div class="wrap foot-bottom">© 2026 {e(S["site_name"])} · {e(S["university"])} · {e(S["address"].replace(chr(10), ", "))}</div>
</footer>
</body>
</html>
"""

def write(name, title, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(layout(name, title, body))

def page_hero(kicker, title):
    return f"""<section class="page-hero"><div class="wrap">
  <p class="kicker">{e(kicker)}</p><h1>{e(title)}</h1>
</div></section>"""

KIND = {"journal":"Journal","conference":"Conference","edited":"Edited issue"}
def pub_item(p, compact=False):
    doi = f'<a class="doi" href="https://doi.org/{e(p["doi"])}" target="_blank" rel="noopener">DOI ↗</a>' if p.get("doi") else ""
    tags = "".join(f'<span class="tag">{e(t)}</span>' for t in (p.get("tags") or []))
    pid = "abs-" + p["_slug"] + ("-c" if compact else "")
    if p["_body"]:
        paras = md(p["_body"])
        abs_btn = f'<button class="abs-btn" type="button" aria-expanded="false" aria-controls="{pid}" onclick="var d=document.getElementById(\'{pid}\');d.hidden=!d.hidden;this.setAttribute(\'aria-expanded\',!d.hidden);this.textContent=d.hidden?\'Abstract\':\'Hide abstract\'">Abstract</button>'
        abs_box = f'<div class="abstract" id="{pid}" hidden>{paras}</div>'
    elif p.get("doi"):
        abs_btn = f'<a class="abs-btn" href="https://doi.org/{e(p["doi"])}" target="_blank" rel="noopener">Abstract at publisher ↗</a>'; abs_box = ""
    else:
        abs_btn = abs_box = ""
    ptype = p.get("type", "journal")
    return f"""<li class="pub" data-year="{p['year']}" data-type="{ptype}" data-area="{e(p.get('area',''))}">
  <div class="pub-meta"><span class="pub-kind pub-kind-{ptype}">{KIND.get(ptype, ptype)}</span>{'' if compact else f'<span class="pub-year">{p["year"]}</span>'}</div>
  <div class="pub-body">
    <h3>{e(p['title'])}</h3>
    <p class="authors">{bold_pi(p.get('authors',''))}</p>
    <p class="venue">{e(p.get('venue',''))} {doi}</p>
    <div class="pub-actions">{abs_btn}{'' if compact else f'<div class="tags">{tags}</div>'}</div>
    {abs_box}
  </div></li>"""

# ------------------------------------------------------------------ build ---
if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)
shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))
shutil.copytree(os.path.join(ROOT, "admin"), os.path.join(OUT, "admin"))
open(os.path.join(OUT, ".nojekyll"), "w").close()

# ---- Home
area_cards = "".join(f"""<a class="area-card" href="research.html#{e(a['key'])}"><div class="area-icon">{icon(a)}</div><h3>{e(a['title'])}</h3><p>{e(a.get('summary',''))}</p><span class="more">Learn more →</span></a>""" for a in AREAS)
recent = "".join(pub_item(p, compact=True) for p in PUBS[:int(HOME.get("recent_count", 5))])
title_words = SETTINGS["site_name"].split()
hero_title = f'{e(" ".join(title_words[:-1]))} <span class="accent">{e(title_words[-1])}</span>' if len(title_words) > 1 else e(SETTINGS["site_name"])
home = f"""
<section class="hero"><div class="wrap hero-single">
  <div>
    <p class="kicker light">{e(HOME.get("hero_kicker",""))}</p>
    <h1>{hero_title}</h1>
    <p class="lead">{e(HOME.get("hero_lead",""))}</p>
    <div class="cta"><a class="btn btn-green" href="publications.html">Recent publications</a><a class="btn btn-ghost" href="join.html">Join the lab</a></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head"><p class="kicker">What we work on</p><h2>Research directions</h2></div>
  <div class="area-grid">{area_cards}</div>
</div></section>

<section class="section alt"><div class="wrap pi-grid">
  <div class="pi-card">
    <div class="pi-avatar" aria-hidden="true">{e(DIR.get("initials",""))}</div>
    <div><p class="kicker">Director</p><h2>{e(DIR.get("name",""))}</h2>
    <p class="muted">{e(DIR.get("title",""))}<br>{e(SETTINGS["department"].replace("Department of ", ""))}</p></div>
  </div>
  <div>
    {md(DIR.get("home_blurb",""))}
    <a class="link-arrow" href="about.html">About the lab →</a>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="section-head row"><div><p class="kicker">Latest</p><h2>Recent publications</h2></div><a class="link-arrow" href="publications.html">All publications →</a></div>
  <ul class="pub-list compact">{recent}</ul>
</div></section>

<section class="section cta-band"><div class="wrap">
  <h2>{e(HOME.get("cta_title",""))}</h2>
  <p>{e(HOME.get("cta_text",""))}</p>
  <a class="btn btn-green" href="join.html">How to apply</a>
</div></section>
"""
write("index.html", "Home", home)

# ---- About
tl = "".join(f'<li class="tl-item"><span class="tl-when">{e(t["when"])}</span><div class="tl-body"><h3>{e(t["title"])}</h3><p>{md_inline(t["text"])}</p></div></li>' for t in ABOUT_FM.get("timeline", []))
awards = "".join(f"<li>{md_inline(x)}</li>" for x in ABOUT_FM.get("awards", []))
roles  = "".join(f"<li>{md_inline(x)}</li>" for x in ABOUT_FM.get("roles", []))
dlinks = "".join(f'<li><a href="{e(l["url"])}" target="_blank" rel="noopener">{e(l["label"])} ↗</a></li>' for l in SETTINGS.get("links", [])[:2])
about = page_hero("About", ABOUT_FM.get("title", "About the Lab")) + f"""
<section class="section"><div class="wrap two-col">
  <div>
    {md(ABOUT_BODY)}
    <h2>Our history</h2>
    <ol class="timeline">{tl}</ol>
  </div>
  <aside class="side">
    <div class="side-card">
      <div class="pi-card compact">
        <div class="pi-avatar" aria-hidden="true">{e(DIR.get("initials",""))}</div>
        <div><p class="kicker">Director</p><h3>{e(DIR.get("name",""))}</h3><p class="muted">{e(DIR.get("title",""))}</p></div>
      </div>
      {md(DIR.get("bio",""))}
      <ul class="clean tight links">{dlinks}</ul>
    </div>
    <div class="side-card"><h3>Awards &amp; honours</h3><ul class="clean tight">{awards}</ul></div>
    <div class="side-card"><h3>Community roles</h3><ul class="clean tight">{roles}</ul></div>
  </aside>
</div></section>
"""
write("about.html", "About", about)

# ---- Research
def area_section(a):
    k = a["key"]
    related = [p for p in PUBS if p.get("type") != "edited" and p.get("area") == k][:3]
    rel = "".join(f'<li><a href="publications.html#theme-{e(k)}">{e(p["title"])}</a> <span class="muted">({p["year"]})</span></li>' for p in related)
    rel += f'<li><a class="link-arrow" href="publications.html#theme-{e(k)}">All papers in this area →</a></li>'
    return f"""<section class="section area-section" id="{e(k)}"><div class="wrap two-col">
  <div><div class="area-icon lg">{icon(a)}</div><h2>{e(a['title'])}</h2><p class="lead-sm">{e(a.get('summary',''))}</p>{md(a['_body'])}</div>
  <aside class="side"><div class="side-card"><h3>Selected papers</h3><ul class="clean tight links">{rel}</ul></div></aside>
</div></section>"""
write("research.html", "Research", page_hero("Research", "What we work on") + "".join(area_section(a) for a in AREAS))

# ---- Publications
years = sorted({int(p["year"]) for p in PUBS}, reverse=True)
theme_btns = '<span class="filter-label">Theme</span><button class="pill active" data-filter-area="all">All</button>' + "".join(f'<button class="pill" data-filter-area="{e(a["key"])}">{e(a["title"])}</button>' for a in AREAS)
year_btns  = '<span class="filter-label">Year</span><button class="pill active" data-filter-year="all">All</button>' + "".join(f'<button class="pill" data-filter-year="{y}">{y}</button>' for y in years)
type_btns  = '<span class="filter-label">Type</span><button class="pill active" data-filter-type="all">All</button>' + "".join(f'<button class="pill" data-filter-type="{k}">{v if k!="edited" else "Edited issues"}</button>' for k,v in KIND.items())
by_year = "".join(f'<div class="year-group"><h2 class="year-label">{y}</h2><ul class="pub-list">{"".join(pub_item(p) for p in PUBS if int(p["year"])==y)}</ul></div>' for y in years)
pubs = page_hero("Publications", "Recent Publications") + f"""
<section class="section"><div class="wrap">
  <div class="filters" role="group" aria-label="Filter publications">
    <div class="pill-row">{theme_btns}</div>
    <div class="pill-row">{year_btns}</div>
    <div class="pill-row">{type_btns}</div>
  </div>
  <p class="count muted" id="pub-count"></p>
  <div id="pub-groups">{by_year}</div>
  <p class="empty muted" id="pub-empty" hidden>No publications match this filter.</p>
  <div class="pub-foot"><a class="btn btn-purple" href="{e(SETTINGS["scholar_url"])}" target="_blank" rel="noopener">Full record on Google Scholar ↗</a></div>
</div></section>
<script>
(function(){{
  var year='all', type='all', area='all';
  function apply(){{
    var n=0, root=document.getElementById('pub-groups');
    root.querySelectorAll('.pub').forEach(function(li){{
      var ok=(year==='all'||li.dataset.year===year)&&(type==='all'||li.dataset.type===type)&&(area==='all'||li.dataset.area===area);
      li.hidden=!ok; if(ok)n++;
    }});
    root.querySelectorAll('.year-group').forEach(function(g){{ g.hidden=!g.querySelector('.pub:not([hidden])'); }});
    document.getElementById('pub-count').textContent=n+' publication'+(n===1?'':'s');
    document.getElementById('pub-empty').hidden=n>0;
  }}
  function bind(attr, set){{
    document.querySelectorAll('['+attr+']').forEach(function(b){{b.addEventListener('click',function(){{
      set(b.getAttribute(attr));document.querySelectorAll('['+attr+']').forEach(function(x){{x.classList.toggle('active',x===b)}});apply();}})}});
  }}
  bind('data-filter-area',function(v){{area=v}});
  bind('data-filter-year',function(v){{year=v}});
  bind('data-filter-type',function(v){{type=v}});
  var m=location.hash.match(/^#theme-(\\w+)$/);
  if(m){{var b=document.querySelector('[data-filter-area="'+m[1]+'"]');if(b)b.click();}}
  apply();
}})();
</script>
"""
write("publications.html", "Publications", pubs)

# ---- Students
tabs = panels = ""
for i, g in enumerate(GROUPS):
    members = [p for p in PEOPLE if p.get("group") == g["key"]]
    tabs += f'<button role="tab" class="tab{" active" if i==0 else ""}" id="tab-{e(g["key"])}" aria-controls="panel-{e(g["key"])}" aria-selected="{"true" if i==0 else "false"}">{e(g["label"])} <span class="tab-count">{len(members)}</span></button>'
    chips = "".join(f'<li class="person"><span class="initial" aria-hidden="true">{e(p["name"][0])}</span><span class="name">{e(p["name"])}</span></li>' for p in members)
    panels += f'<div role="tabpanel" id="panel-{e(g["key"])}" aria-labelledby="tab-{e(g["key"])}" class="panel"{"" if i==0 else " hidden"}><ul class="people">{chips}</ul></div>'
students = page_hero("People", "Students and Alumni") + f"""
<section class="section"><div class="wrap">
  <div class="tabs" role="tablist" aria-label="Student groups">{tabs}</div>
  {panels}
</div></section>
<script>
document.querySelectorAll('.tab').forEach(function(t){{t.addEventListener('click',function(){{
  document.querySelectorAll('.tab').forEach(function(x){{x.classList.toggle('active',x===t);x.setAttribute('aria-selected',x===t)}});
  document.querySelectorAll('.panel').forEach(function(p){{p.hidden=p.id!==t.getAttribute('aria-controls')}});
}})}});
</script>
"""
write("students.html", "Students", students)

# ---- Join
cards = "".join(f'<div class="join-card"><h3>{e(c["title"])}</h3>{md(c["text"])}</div>' for c in JOIN_FM.get("cards", []))
join = page_hero("Join Us", JOIN_FM.get("title", "Join Us")) + f"""
<section class="section"><div class="wrap">
  <div class="join-grid">{cards}</div>
  <div class="note-card"><h3>{e(JOIN_FM.get("how_to_apply_title","How to apply"))}</h3>{md(JOIN_BODY)}</div>
</div></section>
"""
write("join.html", "Join Us", join)

# ---- Contact
clinks = "".join(f'<li><a href="{e(l["url"])}" target="_blank" rel="noopener">{e(l["label"])} ↗</a></li>' for l in SETTINGS.get("links", []))
contact = page_hero("Contact", "Get in touch") + f"""
<section class="section"><div class="wrap contact-grid">
  <div class="side-card">
    <h3>{e(DIR.get("name",""))}</h3>
    <p>{e(DIR.get("title","").split(",")[0])}<br>{e(SETTINGS["department"])}<br>{e(SETTINGS["university"])}</p>
    <p><a href="mailto:{e(SETTINGS["email"])}">{e(SETTINGS["email"])}</a></p>
    <p>{e(SETTINGS["address"]).replace(chr(10), "<br>")}</p>
  </div>
  <div class="side-card"><h3>Online</h3><ul class="clean tight links">{clinks}</ul></div>
  <div class="map-card">
    <iframe title="Map of {e(SETTINGS["university"])}" src="https://www.openstreetmap.org/export/embed.html?bbox=-79.3835%2C43.6560%2C-79.3745%2C43.6610&layer=mapnik&marker=43.6577%2C-79.3788" loading="lazy"></iframe>
  </div>
</div></section>
"""
write("contact.html", "Contact", contact)

print(f"Built {len(NAV)} pages, {len(PUBS)} publications, {len(PEOPLE)} people into {OUT}")
