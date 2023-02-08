FROM continuumio/miniconda3 AS builder

# Updating system libraries
RUN apt-get update
RUN apt-get install -y build-essential

# Copying environment yml file
COPY env.yml env.yml

# Creating new enviroment from env.yml
RUN conda env create -f env.yml -n tfdv-dev

# Debian image
FROM debian:11-slim

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Updating system libraries
RUN apt-get update --yes && \
    apt-get clean

# Installing certificates in image
RUN apt install -y ca-certificates

# Copying gcp-ctt environment to image
COPY --from=builder /opt/conda/envs/tfdv-dev /opt/conda/envs/tfdv-dev

# Copying all files to image
COPY . .

# Setting python path in enviroment
ENV PATH="/opt/conda/envs/tfdv-dev/bin:$PATH"