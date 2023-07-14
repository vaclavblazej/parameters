# Parameter hierarchy

This repository contains the data and scripts that generate the [parameter hierarchy website](https://vaclavblazej.github.io/parameters/).

The web is meant to provide:

* a quick overview of
    * (partially done) parameter definitions
    * (partially done) bounding connections
    * (in future) graph classes that distinguish parameters (via ISGCI)
* (current focus) display relevant references
* (in future) single PDF
* (in future) interactive mode
    * let users with visualize the boundary of tractability and hardness for their problems
    * customize the view by hiding and positioning the nodes
    * output TikZ code that can be directly used in a scientific paper

It will take us a while to have majority of the parameter relations and their references.
To give your suggestions and fixes (with references) please open a [github issue](https://github.com/vaclavblazej/parameters/issues) or [mail us](vaclav.blazej@warwick.ac.uk).

* Any copied material must have a source link. Everything else will be slowly replaced.

## Repository folders and files

* main content
    * `content` markdown of the website
    * `scripts` source data and codes that export the data into human-readable form to the `content` folder
* website setup
    * `.github` setup for the website deployment
    * `hugo.toml` website settings
    * `layouts` custom components and templates for the website
    * `static` css files for the website
    * `themes` contains git submodule with the website style
* extras
    * `.git, .gitignore, .gitmodules` git versioning data
    * `README.md`, `todo.md`, documentation

## Inspired by

* 2013-2019 [Parameterized Hierarchy](https://manyu.pro/assets/parameter-hierarchy.pdf) by M. Sorge.
* [Comparing Graph Parameters](https://fpt.akt.tu-berlin.de/publications/theses/BA-Schr%C3%B6der.pdf) by J. Ch. B. Schröder
* 2010 [Comparing 17 graph parameters](https://core.ac.uk/download/pdf/30926677.pdf) by Róbert Sasák

## Generating content

In `scripts` folder, there are python source codes that generate the static content.
The content is pushed in the repository so there is no need to regenerate it to view raw website, however, it may be useful for seeing changed made to the data.
We use `venv` to manage python's enviroment.
Running the following activates the virtual python environment for you and it should 

```sh
cd scripts
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Now run `./build.py` to generate the content.

To add a new package:

```sh
pip install new_pip_package
pip freeze > requirements.txt
```

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

## Authors and Contributors

* [Václav Blažej](https://blazeva1.pages.fit/)

contributors

* [Šimon Schierreich](https://pages.fit.cvut.cz/schiesim/)
* Jan Pokorný
