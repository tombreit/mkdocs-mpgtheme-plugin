# MkDocs Material MPG Theme

A MkDocs plugin that makes the Material for MkDocs theme look a bit like MPG.

## Requirements

- [MkDocs](https://www.mkdocs.org/getting-started/)
- [Material for MkDocs theme](https://squidfunk.github.io/mkdocs-material/getting-started/)

## Usage

- Setup MkDocs and Material for MkDocs theme
- Install this plugin:

   ```bash
   pip install mkdocs-mpgtheme-plugin
   ```

- Activate this plugin in your MkDocs project:

   ```yml
   plugins:
    - mpgtheme
   theme:
    name: material
    logo: _assets/header-logo.svg
    footer_logo: _assets/footer-logo.svg
  extra:
    # all `extra`s are optional
    support_email: mail@example.org
    support_phone: +49 123 456 789
    privacy_policy_url: https://example.org/privacy-policy/
    imprint_url: https://example.org/imprint/
    copyright_string: ACME Inc.
   ```

- Save and reference your header and footer logo files.<br><p style="color: gray; font-size: smaller;">
Due to licensing and copyright issues, the logo files are not part of this project.
</p>

- Done
