FROM nicbet/datascience-minimal

LABEL maintainers="Sascha Just <sascha.just@own-hero.net>,Nicolas Bettenburg <nicbet@gmail.com>" \
    version="0.1" \
    description="Image containing all programming languages to be used with a local shell."


#______________________________________________________________________________________________________
# Latest version of python in bionic is 3.6.5-3
# Python 3
USER root
WORKDIR /tmp
RUN apt install -y python3-pip \
    && pip3 install virtualenv virtualenvwrapper


ENV R_VERSION=3.5.1

#______________________________________________________________________________________________________
# Install R language
# https://www.digitalocean.com/community/tutorials/how-to-install-r-on-ubuntu-18-04
USER root
WORKDIR /tmp
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 \
    && add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/' \
    && apt update \
    && apt install -y r-base=${R_VERSION}-1bionic \
    && apt-mark hold r-base



ENV JULIA_PKGDIR=/opt/julia \
    JULIA_VERSION=1.0.0 \
    JULIA_CHECKSUM=bea4570d7358016d8ed29d2c15787dbefaea3e746c570763e7ad6040f17831f3

#______________________________________________________________________________________________________
# Julia Language
# https://julialang.org/downloads/platform.html
USER root
WORKDIR /tmp
RUN mkdir /opt/julia-${JULIA_VERSION} \
    && cd /tmp \
    && wget -q https://julialang-s3.julialang.org/bin/linux/x64/`echo ${JULIA_VERSION} | cut -d. -f 1,2`/julia-${JULIA_VERSION}-linux-x86_64.tar.gz \
    && echo "${JULIA_CHECKSUM} *julia-${JULIA_VERSION}-linux-x86_64.tar.gz" | sha256sum -c - \
    && tar xzf julia-${JULIA_VERSION}-linux-x86_64.tar.gz -C /opt/julia-${JULIA_VERSION} --strip-components=1 \
    && rm /tmp/julia-${JULIA_VERSION}-linux-x86_64.tar.gz
RUN ln -fs /opt/julia-${JULIA_VERSION}/bin/julia /usr/local/bin/julia




ENV GO_VERSION=1.11
ENV GO_DOWNLOAD_URL="https://dl.google.com/go/go${GO_VERSION}.linux-amd64.tar.gz" \
    GO_DOWNLOAD_SHA256=b3fcf280ff86558e0559e185b601c9eade0fd24c900b4c63cd14d1d38613e499

#______________________________________________________________________________________________________
# Install GO Language
# https://golang.org/doc/install
USER root
WORKDIR /tmp
RUN curl -fSL -o go-${GO_VERSION}.tar.gz "${GO_DOWNLOAD_URL}" \
    && echo "${GO_DOWNLOAD_SHA256} go-${GO_VERSION}.tar.gz" | sha256sum -c - \
    && tar -C /opt -xzf go-${GO_VERSION}.tar.gz \
    && mv /opt/go /opt/go-${GO_VERSION} \
    && echo "export PATH=$PATH:/opt/go-${GO_VERSION}/bin" >> /etc/profile.d/go.sh \
    && rm -rf go-${GO_VERSION}.tar.gz \
    && ln -s /opt/go-${GO_VERSION}/bin/go* /usr/local/bin/



ENV ELIXIR_VERSION=1.7.2-1 

#______________________________________________________________________________________________________
# Install Elixir Language
# https://elixir-lang.org/install.html
USER root
WORKDIR /tmp
RUN wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \
    && dpkg -i erlang-solutions_1.0_all.deb \
    && apt-get update \
    && apt-get install -y esl-erlang \
    && apt-get install -y elixir=${ELIXIR_VERSION} \
    && apt-mark hold elixir \
    && rm -rf erlang-solutions_1.0_all.deb

#______________________________________________________________________________________________________
# Hex Package Manager and rebar3
# https://github.com/erlang/rebar3#getting-started

ENV REBAR_VERSION="2.6.4"
ENV REBAR_DOWNLOAD_URL="https://github.com/rebar/rebar/archive/${REBAR_VERSION}.tar.gz" \
    REBAR_DOWNLOAD_SHA256="577246bafa2eb2b2c3f1d0c157408650446884555bf87901508ce71d5cc0bd07"

RUN set -xe \
    && mkdir -p /usr/src/rebar-src \
    && curl -fSL -o rebar-src.tar.gz "$REBAR_DOWNLOAD_URL" \
    && echo "$REBAR_DOWNLOAD_SHA256 rebar-src.tar.gz" | sha256sum -c - \
    && tar -xzf rebar-src.tar.gz -C /usr/src/rebar-src --strip-components=1 \
    && rm rebar-src.tar.gz \
    && cd /usr/src/rebar-src \
    && ./bootstrap \
    && install -v ./rebar /usr/local/bin/ \
    && rm -rf /usr/src/rebar-src

# Install Rebar to build ielixir
ENV REBAR3_VERSION="3.6.1"
ENV REBAR3_DOWNLOAD_URL="https://github.com/erlang/rebar3/archive/${REBAR3_VERSION}.tar.gz" \
    REBAR3_DOWNLOAD_SHA256="40b3c85440f3235c7b149578d0211bdf57d1c66390f888bb771704f8abc71033"

RUN set -xe \
    && mkdir -p /usr/src/rebar3-src \
    && curl -fSL -o rebar3-src.tar.gz "$REBAR3_DOWNLOAD_URL" \
    && echo "$REBAR3_DOWNLOAD_SHA256 rebar3-src.tar.gz" | sha256sum -c - \
    && tar -xzf rebar3-src.tar.gz -C /usr/src/rebar3-src --strip-components=1 \
    && rm rebar3-src.tar.gz \
    && cd /usr/src/rebar3-src \
    && HOME=$PWD ./bootstrap \
    && install -v ./rebar3 /usr/local/bin/ \
    && rm -rf /usr/src/rebar3-src

ENV RUBY_VERSION=2.5.1
ENV RUBY_DOWNLOAD_URL="http://ftp.ruby-lang.org/pub/ruby/" \
    RUBY_DOWNLOAD_SHA256=dac81822325b79c3ba9532b048c2123357d3310b2b40024202f360251d9829b1

#______________________________________________________________________________________________________
# Ruby
# https://gorails.com/setup/ubuntu/18.04
USER root
WORKDIR /tmp
RUN wget -q "${RUBY_DOWNLOAD_URL}`echo ${RUBY_VERSION} | cut -d. -f 1,2`/ruby-${RUBY_VERSION}.tar.gz" \
    && echo "${RUBY_DOWNLOAD_SHA256} *ruby-${RUBY_VERSION}.tar.gz" | sha256sum -c - \
    && tar -xzvf ruby-${RUBY_VERSION}.tar.gz \
    && cd ruby-${RUBY_VERSION}/ \
    && ./configure \
    && make \
    && make install \
    && ruby -v \
    && gem install bundler \
    && rm -f /tmp/ruby-${RUBY_VERSION}.tar.gz \
    && rm -rf /tmp/ruby-${RUBY_VERSION}


