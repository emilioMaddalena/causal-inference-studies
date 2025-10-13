# Contributing to causal-inference-studies

Thanks for your interest! 🙏 🙏 🙏

Contributions of all kinds are welcome: notebooks, docs, examples, fixes... Here's a quick guide to it

- Spotted errors or have ideas or questions: **open an Issue**
- Small fixes: **open a Pull Request directly**
- Wanna add a new notebook or page to the project: **open an Issue to discuss approach, only then open a Pull Request**

## Tools needed to develop it 🔧

To build the project locally and see the effects of any changes instantly, we use [mkdocs](https://www.mkdocs.org/getting-started/).

After cloning the repo and installing `mkdocs`, just run `mkdocs build` followed by `mkdocs serve` in your terminal.

As for the python dependencies, we use [uv](https://docs.astral.sh/uv/). After installing it, just run `uv init` followed by `uv sync` in the main folder. Voilà, you have a python environment that can run all notebooks.

## Project structure 📂

The project is built by `mkdocs`. To develop locally and checking out your changes instantly, download 

The project contents are organized as follows:

- Pages are defined as raw `.md` files under the `material` folder
- Any images needed go in `material/imgs`
- Notebooks are in `material/notebooks`

