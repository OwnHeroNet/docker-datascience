# docker-datascience

Quickstart:

Available images:

- nicbet/datascience-minimal
- nicbet/datascience-shell
- nicbet/datascience-jupyter
- nicbet/datascience-all

Fetch the image you want to use:
```
docker pull nicbet/datascience-all
```

Start the image in a dynamic container:
```
docker run --rm -it -p 8888:8888 -v $(pwd):/home/datascience/work nicbet/datascience-all
```

or create a container to reuse:

```
docker create --name datascience-all -p 8888:8888 -v $(pwd):/home/datascience/work nicbet/datascience-all
docker start --attach datascience-all
```

### Description 
A Jupyter Lab based container for data science projects.

### Usage
`docker run --rm -it -p 8888:8888 nicbet/jupyter-datascience` starts the jupyter lab server on port 8888. Then connect to http://localhost:8888 with the token printed to the console.

### Included Packages:
- python>=3.6.6
- rpy2>=2.9.4
- r-base=3.4.1
- r-irkernel>=0.8.12
- r-plyr>=1.8.4
- r-devtools>=1.13.6
- r-tidyverse>=1.1.1
- r-irkernel>=0.8.12
- r-plyr>=1.8.4
- r-devtools>=1.13.6
- r-shiny>=1.0.5
- r-rmarkdown>=1.9
- r-forecast>=8.2
- r-rsqlite>=2.0
- r-reshape2>=1.4.3
- r-nycflights13>=1.0.0
- r-caret>=6.0_80
- r-rcurl>=1.95_4.11
- r-crayon>=1.3.4
- r-randomforest>=4.6_12
- r-htmltools>=0.3.6
- r-sparklyr>=0.8.3
- r-htmlwidgets>=1.0
- r-hexbin>=1.27.2
- tensorflow>=1.9.0
- keras>=2.2.2
- pytorch=0.4.*
- chainer=4.3.*
- theano=1.*.*
- opencv
- caffe
- jupyterthemes>=0.19.6
- plotly>=3.1.1
- imbalanced-learn>=0.3.3
- psycopg2>=2.7.5
- tabulate>=0.8.2
- ipywidgets>=7.4.0
- pandas=0.23*
- numexpr=2.6*
- matplotlib=2.2*
- scipy=1.1*
- seaborn=0.9*
- scikit-learn=0.19*
- scikit-image=0.14*
- sympy=1.1*
- cython=0.28*
- patsy=0.5*
- statsmodels=0.9*
- cloudpickle=0.5*
- dill=0.2*
- numba=0.38*
- bokeh=0.12*
- sqlalchemy=1.2*
- hdf5=1.10*
- h5py=2.7*
- vincent=0.4.*
- beautifulsoup4=4.6.*
- protobuf=3.*
- xlrd
- jupyter_nbextensions_configurator=0.4*
- jupyter_contrib_nbextensions=0.5*
- Elixir 1.7
- Julia 1.0
