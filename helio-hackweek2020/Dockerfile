#---------------------------------------------------------------------------------
# NASA Helio Hackweek 2020 Docker Container
# This event will focus on implementation of open source, machine learning and AI 
# approaches for large datasets. The event is co-sponsored by the Center for 
# Helioanalytics, Computational and Information Science and Technology Office, 
# University of Maryland Department of Geographical Sciences, and NVIDIA. It is 
# supported by the NASA Center for Climate Simulation and the University of Maryland 
# Department of Geographical Sciences. https://heliohackweek.github.io/
#
# Build:
#     docker build --tag helio-hackweek2020:1.0 .
#
# Packages:
#     base: rapids ai cuda 10.1 container
#     additional packages: 
#         TensorFlow, Keras, SKLearn, Numpy, Pandas, Scipy, Sunpy, PySPEDAS, Pyflux
#         Dask, Dask-image, Astropy, Jax, Numba, RAPIDS, AIAPy, CuPy, matplotlib
# Usage:
#     A conda environment called "rapids" has been configured inside the container.
#     "source activate rapids" to activate the environment. For additional info
#     refer to the README attached.
#     
# Date: 08/10/2020 
# Author: Jordan A. Caraballo Vega
#---------------------------------------------------------------------------------

# Arguments to pass to the image
ARG CUDA_VER=10.1
ARG LINUX_VER=centos7
ARG FROM_IMAGE=nvcr.io/nvidia/rapidsai/rapidsai

# Import RAPIDS container as the BASE Image (cuda base image)
# CentOS 7 image with CUDA 10.1 support. runtime container 
# includes examples notebooks and jupyterhub server.
FROM ${FROM_IMAGE}:cuda${CUDA_VER}-runtime-${LINUX_VER}

# Adding ENV variables
ENV RAPIDS_DIR=/rapids

# Installing gcc, g++, and make - requirement from pyflux package
# opengl to support pyspedas.
RUN yum -y group install "Development Tools" \
    && yum -y install mesa-libGL mesa-libGL-devel \
       fontconfig freetype freetype-devel fontconfig-devel \
       libstdc++ libXrender libxkbcommon-x11

# Adding additional packages to BASE Image. Install additional packages.
# Note: Import Keras as from tensorflow import keras. Keras was only installed 
# to meet requirements, but should be used from inside TensorFlow.
# If Horovod is required, install MPI and install it with the following line.
# && HOROVOD_GPU_OPERATIONS=NCCL pip install horovod \
RUN source activate rapids \
    && pip install tensorflow keras \
    && pip install sunpy dask-image astropy pyspedas aiapy \
    && pip install pyflux

# Install Jax with CUDA support.
RUN source activate rapids \
    && pip install --upgrade https://storage.googleapis.com/jax-releases/cuda101/jaxlib-0.1.52-cp36-none-manylinux2010_x86_64.whl \
    && pip install --upgrade jax
