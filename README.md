# MkDocs MPG Theme

A MkDocs plugin that makes the Material for MkDocs theme look a bit like MPG.

This plugin uses the "Material for MkDocs" theme and just adds some visual touches.

## Requirements

- [MkDocs](https://www.mkdocs.org/getting-started/)
- [Material for MkDocs theme](https://squidfunk.github.io/mkdocs-material/getting-started/)

## Demo

<https://tombreit.github.io/mkdocs-mpgtheme-plugin/>

## Usage

- Setup MkDocs and Material for MkDocs theme
- Install this plugin:

   ```bash
   pip install mkdocs-mpgtheme-plugin
   ```

- Activate and configure this plugin in your MkDocs project:

   ```yml
   # file: mkdocs.yml

   plugins:
     - search
     - mpgtheme
   theme:
     name: material
     logo: _assets/header-logo.svg
     footer_logo: _assets/footer-logo.svg
  extra:
     # all extras are optional
     support_email: mail@example.org
     support_phone: +49 123 456 789
     privacy_policy_url: https://example.org/privacy
     imprint_url: https://example.org/imprint
     copyright_string: ACME Inc.
   ```

- Save and reference your header and footer logo files.
- That's it.

## Notes

- Installing this plugin will install `mkdocs` and `mkdocs-material` as dependencies.
- For a more complete configuration, see our demo [`mkdocs.yml`](./mkdocs.yml).
- Due to licensing and copyright issues, the MPG logo files are not part of this project, but we ship placeholder files for `header-logo.svg` and `footer-logo.svg`. Just set your logos (format: SVG) via `logo` and `footer_logo` in the `theme` config (see above).
