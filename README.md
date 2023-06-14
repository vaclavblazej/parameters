# Parameter hierarchy

This repository contains the data and scripts that generate the parameter hierarchy website.

[See the resulting website.](https://vaclavblazej.github.io/parameters/)

What it the parameter hierarchy meant to provide:

* provide quick overview of parameters
* allow quick access to references (parameter definitions, bounds, counterexamples, etc.)
* (in future) help users with visualizing the boundary of tractability and hardness for their problems
* (in future) customize the view by hiding and positioning the nodes
* (in future) output TikZ code that can be directly used in a paper

It will take us a while to have majority of the parameter relations and references.
To give your suggestions and fixes (with references), please open a [github issue](https://github.com/vaclavblazej/parameters/issues) or [mail us](vaclav.blazej@warwick.ac.uk).

* Any copied material has a source link -- this is the preferred way. Everything else will be slowly replaced.

## Repository folders and files

* main content
    * `content` markdown of the website
    * `data` holds raw data; hard to work with without the scripts
    * `scripts` has source codes that export the data into human-readable form in the `content` folder
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

## Rendering

The page is setup using the [Hugo](https://gohugo.io/) static page generator which can be run locally with `hugo server`.
Automatic deployment is made with github pages.
