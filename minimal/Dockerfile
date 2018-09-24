FROM ubuntu:18.04

LABEL maintainers="Sascha Just <sascha.just@own-hero.net>,Nicolas Bettenburg <nicbet@gmail.com>" \
    version="0.1" \
    description="Minimal image configured to be used as a starting point for 'nicbet/datascience-shell'."

# For apt install
ENV DEBIAN_FRONTEND noninteractive

#______________________________________________________________________________________________________
# Add a Non-Privileged User
ENV NB_USER=datascience \
    NB_UID=1000 \
    NB_GID=100

ENV HOME=/home/$NB_USER

WORKDIR /tmp

#______________________________________________________________________________________________________
# Base packages and system-wide dependencies
RUN apt-get update \
    && apt-get install -y apt-utils \
    && apt-get install -y \
    curl \
    wget \
    git \
    bzip2 \
    sudo \
    locales \
    gnupg \
    software-properties-common \
    libtool \
    libtool-bin \
    libffi-dev \
    libczmq-dev \
    libzmq3-dev \
    autoconf \
    pkg-config

# Add microsoft packages to ubuntu to install SQL Server connectors.
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update

#______________________________________________________________________________________________________
# Set the locale
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Required to build HDF5 packages for the individual languages
RUN apt-get install -y hdf5-tools 

# Install dependencies for SQL Server
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN ACCEPT_EULA=Y apt-get install -y mssql-tools
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> /etc/bash_profile \
    && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> /etc/bashrc
RUN apt-get install unixodbc-dev

# Install fonts FiraSans, FiraMono, and FiraCode
ENV FIRA_VERSION=f54eeb3124c63fe9b5bcd36d09d1cd46788cd15e
ENV FIRA_DOWNLOAD_URL="https://github.com/bBoxType/FiraSans/tarball/${FIRA_VERSION}" \
    FIRA_DOWNLOAD_SHA256=f754f6d2698fce0fd6c82e8ad4cfe9f92b90e26e4844aaf4eaf9b315f74325ba \
    FIRA_DIR='bBoxType-FiraSans-f54eeb3'

RUN set -xe \
    && curl -fSL -o fira.tar.gz "${FIRA_DOWNLOAD_URL}" \
    && echo "$FIRA_DOWNLOAD_SHA256  fira.tar.gz" | sha256sum -c - \
    && tar xzf fira.tar.gz \
    && mkdir -p /usr/share/fonts/opentype/fira \
    && mkdir -p /usr/share/fonts/truetype/fira \
    && mkdir -p /usr/share/fonts/woff/fira \
    && find "${FIRA_DIR}/" -name "*.otf" -exec cp {} /usr/share/fonts/opentype/fira/ \; \
    && find "${FIRA_DIR}/" -name "*.ttf" -exec cp {} /usr/share/fonts/truetype/fira/ \; \
    && find "${FIRA_DIR}/" -name "*.woff" -exec cp {} /usr/share/fonts/woff/fira/ \; \
    && rm -rf "${FIRA_DIR}/" fira.tar.gz

#______________________________________________________________________________________________________
# Create datascience user with UID=1000 and in the 'users' group
# and make sure these dirs are writable by the `users` group.
USER root
WORKDIR /root
ADD fix-permissions /usr/local/bin/fix-permissions
RUN groupadd wheel -g 11 && \
    echo "auth required pam_wheel.so use_uid" >> /etc/pam.d/su && \
    useradd -m -s /bin/bash -N -u $NB_UID $NB_USER && \
    chmod g+w /etc/passwd && \
    fix-permissions $HOME

#______________________________________________________________________________________________________
# Node 8.x LTS
# https://gorails.com/setup/ubuntu/18.04
USER root
WORKDIR /tmp
RUN apt install -y curl \
    && curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list \
    && apt-get update \
    && apt-get install -y git-core curl zlib1g-dev build-essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev libcurl4-openssl-dev software-properties-common libffi-dev nodejs yarn

#______________________________________________________________________________________________________
# Entrypoint
USER $NB_UID
WORKDIR $HOME
EXPOSE 8888
CMD ["/bin/bash", "--login"]

