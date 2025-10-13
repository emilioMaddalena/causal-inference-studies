# Contributing to causal-inference-studies

Thanks for your interest! 🙏 🙏 🙏

Contributions of all kinds are welcome: notebooks, docs, examples, fixes... Here's a quick guide to it

- Spotted errors or have ideas or questions: **open an Issue**
- Small fixes: **open a Pull Request directly**
- Wanna add a new notebook or page to the project: **open an Issue to discuss approach, only then open a Pull Request**

## Project structure 📂

The project contents are organized as follows:

- Pages are defined as raw `.md` files under the `material` folder
- Any images needed go in `material/imgs`
- Notebooks are in `material/notebooks`
- The site navigation bars are defined in `mkdocs.yml`
- Custom elements like tables can be found in `material/css/style.css`
  
## Tools needed to develop it 🔧

To build the project locally and see the effects of any changes instantly, we use [mkdocs](https://www.mkdocs.org/getting-started/).

After cloning the repo and installing `mkdocs`, just run `mkdocs build` followed by `mkdocs serve` in your terminal.

As for the python dependencies, we use [uv](https://docs.astral.sh/uv/). After installing it, just run `uv init` followed by `uv sync` in the main folder. Voilà, you have a python environment that can run all notebooks.

## How to proceed 🏗️

- To create a new page: define it as a Markdown file in `material` and add it to the site by editing `mkdocs.yml`
- To create a new notebook: create it under `material/notebooks` and add it to the site by editing `mkdocs.yml`

N.B. Notebook pages are not defined as markdown files, but rendered directly from `.ipynb`.
N.B. For notebooks, make sure the first headline e.g. `# Uplift modelling` matches your entry in the YAML file e.g. `- Uplift modelling: notebooks/uplift_modelling.ipynb`. Otherwise the former name will take precedence over the latter in the navigation bar.
