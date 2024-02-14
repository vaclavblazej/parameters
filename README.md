# HOPS frontend setup and generated markdowns

This repository contains content that is ready to be displayed on [HOPS](vaclavblazej.github.io/parameters/) when rendered using Hugo framework.

To see the source of the data about parameters look at [parameters-code](https://github.com/vaclavblazej/parameters-code) which contains all relevant entries and generates the `content` folder of this repository.

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

