# Based on scipy-notebook of the Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

ARG OWNER=jupyter
ARG BASE_CONTAINER=$OWNER/datascience-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Nikolas Garofil <nikolas.garofil@uantwerpen.be>"

USER root
RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends graphviz && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

USER ${NB_UID}
RUN pip3 install dot_kernel
RUN install-dot-kernel

WORKDIR "${HOME}"

#Note that install-dot-kernel creates some needed files in $HOME.
#So when binding volumes bind them to subdirs of $HOME not $HOME itself.
