# The Minimal Light Theme (Customized)

[![LICENSE](https://img.shields.io/github/license/yaoyao-liu/homepage?style=flat-square\&logo=creative-commons\&color=EF9421)](https://github.com/yaoyao-liu/minimal-light/blob/main/LICENSE)

[[Demo the original theme](https://minimal-light-theme.yliu.me/)]
[[简体中文](https://github.com/yaoyao-liu/minimal-light/blob/master/README_zh_Hans.md) | [繁體中文](https://github.com/yaoyao-liu/minimal-light/blob/master/README_zh_Hant.md) | [Deutsche](https://github.com/yaoyao-liu/minimal-light/blob/master/README_de.md)]

---

## About this repository

This repository hosts a **personal academic homepage** built on top of the **Minimal Light** Jekyll theme by Yaoyao Liu.

The original theme is used **without structural changes**. Customization is intentionally minimal and focused on:

* Small **CSS overrides** via Sass (no direct modification of the core theme files)
* Minor **presentation tweaks**, such as avatar size and shape
* Content customization (publications, teaching, work in progress)
* **Google Analytics disabled** for simplicity and privacy

The goal is to preserve the clarity, maintainability, and update-friendliness of the original theme while adapting it to a more traditional academic presentation.

---

*This theme is originally based on [minimal](https://github.com/orderedlist/minimal).*
*Feel free to use and share the original source code.*

An improved vision from [@Xiao-Chenguang](https://github.com/Xiao-Chenguang):
[https://github.com/Xiao-Chenguang/minimal-light](https://github.com/Xiao-Chenguang/minimal-light)

**The original author’s homepage is available here:**
[https://github.com/yaoyao-liu/homepage](https://github.com/yaoyao-liu/homepage)

---

## Features

* Simple and elegant personal homepage theme
* Jekyll theme, automatically deployed by GitHub Pages
* Basic search engine optimization
* Mobile friendly
* Supporting Markdown
* Supporting dark mode (can be disabled via configuration or overrides)

## Project Architecture

```
.
├── _data                    
|   |── publications.yml                      # the YAML file for publications
|   |── reading.yml                           # a YAML file that generate the reading list
|   └── work_in_progress.yml                  # a YAML for work in progress (no draft yet)
├── _includes                    
|   ├── publications.md                       # the Markdown file for publications
|   ├── reading.md                            # the Markdown file for the reading list
|   ├── services.md                           # the Markdown file for services to the profession
|   ├── teaching.md                           # the Markdown file for teaching activities
|   └── services.md                           # the Markdown file for services
├── _layouts                  
|   └── homepage.html                         # the HTML template for the homepage 
├── _sass
|   ├── minimal-light.scss                    # compiled into the main CSS file
|   └── minimal-light-no-dark-mode.scss       # variant with dark mode disabled
├── assets                                    # images, CSS, JS, files
├── html_source_file                          # precompiled HTML version
├── .gitignore
├── CNAME                                     # custom domain configuration
├── Gemfile                                   # Ruby dependencies
├── LICENSE
├── README.md
├── README_de.md
├── README_zh_Hans.md
├── README_zh_Hant.md
├── _config.yml                               # Jekyll configuration
└── index.md                                  # homepage content (Markdown)
```

## Getting Started

This template can be used in the following two ways:

* **Using GitHub Pages** (recommended)
* **Using Jekyll locally**, then uploading the generated HTML

Detailed instructions are provided below.

---

### Using with the GitHub Pages Service

There are two ways to use this theme on GitHub.

#### Fork this repository

* Fork this repository (or [use it as a template](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-from-a-template)) and rename it to:

  ```
  your-username.github.io
  ```

* Enable GitHub Pages following the official guide:
  [https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

#### Using this repository as a remote theme

To use the theme without copying its files, add the following to your `_config.yml`:

```yaml
remote_theme: yaoyao-liu/minimal-light
```

Note: using `remote_theme` applies all default settings.
To customize content (e.g. `index.md`, publications), you still need to copy those files into your repository.

---

### Using Locally with Jekyll

1. Install [Ruby](https://www.ruby-lang.org/en/) and [Jekyll](https://jekyllrb.com/):
   [https://jekyllrb.com/docs/installation/#guides](https://jekyllrb.com/docs/installation/#guides)

2. Clone the repository:

```bash
git clone https://github.com/yaoyao-liu/minimal-light.git
cd minimal-light
```

3. Install dependencies and run the server:

```bash
bundle install
bundle add webrick
bundle exec jekyll serve
```

4. View the site locally at:
   [http://localhost:4000](http://localhost:4000)

The generated static files will appear in the `_site` directory.

---

### Using the HTML Version

If you prefer not to use Jekyll, the compiled HTML files are available in the `html_source_file` directory.
You can edit and deploy those files directly on any static web server.

---

## Customizing

### Configuration Variables

The Minimal Light theme respects the following variables in `_config.yml`:

```yaml
# Basic Information 
title: Your Name
position: Ph.D. Student
affiliation: Your Affiliation
email: yourname (at) example.edu

# Search Engine Optimization (SEO)
keywords: minimal light
description: The Minimal Light is a simple and elegant jekyll theme for academic personal homepage.
canonical: https://minimal-light-theme.yliu.me/

# Links
google_scholar: https://scholar.google.com/
cv_link: assets/files/curriculum_vitae.pdf
github_link: https://github.com/
linkedin: https://www.linkedin.com/
twitter: https://twitter.com/

# Images
avatar: ./assets/img/avatar.png
favicon: ./assets/img/favicon.png
favicon_dark: ./assets/img/favicon-dark.png

# Footnote
enable_footnote: true

# Auto Dark Mode
auto_dark_mode: true

# Font
font: "Serif" # or "Sans Serif"

# Google Analytics
# Remove or comment out if not used
google_analytics: UA-111540567-4
```

---

### Editing `index.md`

Create or edit `index.md` to add your personal content.
Both **Markdown** and **HTML** syntax are supported.

---

### Included Files

By default, `index.md` includes:

```liquid
{% include_relative _includes/publications.md %}
{% include_relative _includes/services.md %}
```

You may remove or replace these includes as needed.

If you want to edit publications without changing the layout, edit:

```
_data/publications.yml
```

---

### Stylesheet

To customize styles:

* Edit `_sass/minimal-light.scss` **or**
* Add minimal override rules (recommended) to avoid touching the core theme

These Sass files are automatically compiled by Jekyll.

---

### Layouts

To modify the HTML structure, edit:

```
_layouts/homepage.html
```

---

## License

This work is licensed under a
[Creative Commons Zero v1.0 Universal License](https://github.com/yaoyao-liu/minimal-light/blob/master/LICENSE).

---

## Acknowledgements

This project uses code from:

* [https://github.com/pages-themes/minimal](https://github.com/pages-themes/minimal)
* [https://github.com/orderedlist/minimal](https://github.com/orderedlist/minimal)
* [https://github.com/alshedivat/al-folio](https://github.com/alshedivat/al-folio)

