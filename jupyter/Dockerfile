FROM nicbet/datascience-shell

LABEL maintainers="Sascha Just <sascha.just@own-hero.net>,Nicolas Bettenburg <nicbet@gmail.com>" \
    version="0.1" \
    description="Image featuring JupyterLab with corresponding kernels."


ARG JUPYTER_TOKEN=84a471ab58d5dbe8c23455b5b6a92f143cc871b1674a5457d83cbb377d06b18c

USER root
ENV TINI_VERSION v0.18.0

ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc /tini.asc
#RUN gpg --keyserver hkp://pool.sks-keyservers.net:80 --recv-keys 595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \
#    && gpg --verify /tmp/tini.asc
RUN chmod +x /tini && ln -s /tini /bin/tini

# Install jupyterlab and base packages
USER $NB_USER
RUN pip3 install \
    jupyterlab==0.34.12 \
    numpy==1.15.1 \
    pandas==0.23.4 \
    matplotlib==3.0.0

# TODO adjust this to the actual jupyter_core location created by pip
RUN set -xe \
    && echo 'c.Completer.use_jedi = True' >>/home/datascience/.local/lib/python3.6/site-packages/jupyter_core/tests/dotipython/profile_default/ipython_config.py

# Make port 8888 available to the world outside this containerENTRYPOINT ["tini", "-g", "--"]
ENTRYPOINT ["tini", "-g", "--"]
EXPOSE 8888
CMD jupyter lab --ip=* --port=8888 --no-browser --notebook-dir=/home/$NB_USER --allow-root --NotebookApp.token=${JUPYTER_TOKEN}

#----------------------------------------
# Install kernels


USER root
WORKDIR /tmp

ENV IELIXIR_VERSION=0.9.13
ENV IELIXIR_DOWNLOAD_SHA256=c466958c19b8f64ed80fe544196fab0dba3279da23c5bf775460ce13067a0626 \
    IELIXIR_DOWNLOAD_URL=https://github.com/pprzetacznik/IElixir/archive/${IELIXIR_VERSION}.tar.gz

RUN set -xe && \
    mkdir -p /opt/ielixir-${IELIXIR_VERSION} && \
    curl -fSL -o ielixir-${IELIXIR_VERSION}.tar.gz ${IELIXIR_DOWNLOAD_URL} && \
    echo "${IELIXIR_DOWNLOAD_SHA256} *ielixir-${IELIXIR_VERSION}.tar.gz" | sha256sum -c - && \
    tar -xzf ielixir-${IELIXIR_VERSION}.tar.gz -C /opt/ielixir-${IELIXIR_VERSION} --strip-components=1 && \
    rm /tmp/ielixir-${IELIXIR_VERSION}.tar.gz && \
    cd /opt/ielixir-${IELIXIR_VERSION} && \
    sed -i -e 's#^ *elixir: ".*#     elixir: ">= 1.1.0",#g' mix.exs && \
    sed -i -e "s#^ *\"display_name\": \".*#   \"display_name\": \"Elixir ${ELIXIR_VERSION}\",#g" install_script.sh && \
    mix local.hex --force && \
    mix deps.get && \
    mix local.rebar --force && \
    mix deps.compile && \
    ./install_script.sh 


# Julia kernel
USER $NB_USER
WORKDIR $HOME
COPY packages/julia-kernel.jl .
RUN /usr/local/bin/julia --color=yes julia-kernel.jl

# IRkernel and R libraries
USER root
WORKDIR /tmp

RUN echo 'install.packages("devtools")' | R --no-save
RUN echo 'devtools::install_github("IRkernel/IRkernel")' | R --no-save
RUN echo 'IRkernel::installspec(user = FALSE)' | R --no-save


# IRuby kernel and Ruby gems
USER root
WORKDIR /tmp
RUN gem install cztop iruby rbczmq -- --with-system-libs

USER $NB_USER
WORKDIR $HOME
RUN iruby register --force