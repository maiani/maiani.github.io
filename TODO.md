# TODO

Private notes: keep this file untracked (the repo is public).

## Standing procedures

- Publications (`data/en/sections/publications.yaml`) and talks
  (`data/en/sections/talks.yaml`) follow the CV in `~/workspace/cv/`;
  newest first.
- After CV changes, rebuild the public resume (`just public` in the CV repo) and
  copy `public_resume.pdf` to `static/files/resume.pdf`.
- Research posts are page bundles in `content/posts/research_post/<slug>/`. A post
  about a paper is authored in that paper's project repo (e.g.
  `~/workspace/amtextures_helix/manuscript/outreach/blog-post/`) and copied here;
  copy edits made here back.

## Toha theme

- Upstream PRs opened 2026-10-08 on `hugo-themes/toha` (formerly
  `hugo-toha/toha`), one per branch in `../toha`; follow up on review:
  - #1228 `seo-metadata`: sitemap, meta descriptions, og:image, noindex, JSON-LD.
  - #1229 `valid-markup`: empty/invalid markup, valid page frame and
    sections, section anchors, hidden empty share row.
  - #1230 `publication-contact-fields`: DOI/arXiv/volume/article-number,
    list of footer emails.
  Each needs a maintainer label (enforce-label); lighthouse-check cannot run
  on fork PRs. Everything else passes.
- Possible follow-up PR: the remaining validator errors on the example site
  (achievements section repeats ids per card, tied to `achievements.js`;
  shortcode demos; sample content).
- New theme fixes: commit on the matching PR branch (or a new one off
  upstream `main`), merge into `site`, push both.
- Once a Toha release contains what this site needs, move to it and drop the
  `replace` in `go.mod` and the fork clone in both workflows.

## Ideas

- Theme: an `orcid` key in the footer `contactInfo` (would also feed the
  JSON-LD `sameAs`; the ORCID is currently only in the about links).
- Theme: a restrained academic profile mode (no animated taglines, less
  motion, publication-first layout).
- Enable LinkedIn and email share buttons for research posts (all are off in
  `hugo.yaml`).
