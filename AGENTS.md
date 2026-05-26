# Repository Guidelines

## Project

This repository is Andrea Maiani's personal academic website, built with Hugo and the Toha theme.

## Workflow

- Prefer small, reviewable changes.
- Run `hugo --minify` before handing off changes.
- Run `/home/skdys/.local/bin/actionlint` after editing GitHub Actions workflows.
- Use Node through `nvm`; this machine currently uses Node 24 and npm 11.
- Do not edit generated `public/`, `resources/`, or `node_modules/` directly.
- `hugo mod npm pack` may update `package.json`, `package-lock.json`, `assets/jsconfig.json`, and `packages/hugoautogen/`.

## Theme Policy

- Avoid overriding Toha theme templates in this website repo.
- If a bug or SEO/accessibility improvement is generally useful for Toha, prefer opening or preparing an upstream theme fix.
- Local overrides should only be temporary unblockers or clearly site-specific behavior. Document why they exist and remove them once the theme is fixed.
- Site-specific content, metadata, publication data, author profile data, robots policy, and copy edits belong in this repo.

## SEO Policy

- Keep canonical production URLs under `https://www.andreamaiani.com`.
- Keep metadata specific and human-readable.
- Search, taxonomy, pagination, sitemap generation, and generic structured-data rendering are theme-level concerns unless Toha exposes a documented site config option.

## Design Direction

- Keep the website restrained and academic.
- Avoid adding flashy portfolio-style effects, animated taglines, or decorative motion.
- Subtle transitions are acceptable when they support navigation or readability.
- Prefer clear research identity, publications, projects, teaching, and contact information over webdev-style presentation.

## Publishing

- Deployments happen through GitHub Actions on pushes to `main`.
- The generated site is published to the `gh-pages` branch.
