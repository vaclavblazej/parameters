# HOPS frontend code

## Repository folders and files

* main content
    * `content` markdown of the website
* website setup
    * `.github` setup for the website deployment
    * `hugo.toml` website settings
    * `layouts` custom components and templates for the website
    * `static` css files for the website
    * `themes` contains git submodule with the website style
* extras
    * `.git, .gitignore, .gitmodules` git versioning data

## Rendering

First, download git submodule for theme.

```sh
git submodule init
git submodule update
```

The page is setup using the [Hugo](https://gohugo.io/) static page generator which can be run locally with:
```sh
hugo server
```

Automatic deployment is made with github pages that has its settings in `.github` folder.

## License

This project is licensed under [MIT](LICENSE) license.

