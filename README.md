# docker-datascience

A Jupyter Lab based container for data science projects.

### Quickstart

Available images:

- nicbet/datascience-minimal
- nicbet/datascience-shell
- nicbet/datascience-jupyter
- nicbet/datascience-complete

Fetch the image you want to use:
```
docker pull nicbet/datascience-complete
```

Start the image in a dynamic container:
```
docker run --rm -it -p 8888:8888 -v $(pwd):/home/datascience/work nicbet/datascience-complete
```

or create a container to reuse:

```
docker create --name datascience-complete -p 8888:8888 -v $(pwd):/home/datascience/work nicbet/datascience-complete
docker start --attach datascience-complete
```

## The datascience-minimal image

This is an `ubuntu:18.04` based image and adds a minimal set of libraries required in all higher-order stacks.
It also sets up the data science user and adds install resources.

## The datascience-shell image

This image contains all installations of the following programming languages which can be used in a shell:

- Python
- R
- Julia
- Go
- Elixir
- Ruby

## The datascience-jupyter image

This image adds JupyterLab and JupyterNotebook. It also runs JupyterLap using tini and provides an entry point at port 8888.

## The datascience-complete image

This image adds all packages for Python, Julia and R that are required for proper data science computations.
