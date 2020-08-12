# NASA Helio Hackweek 2020 Docker Container

This event will focus on implementation of open source, machine learning and AI
approaches for large datasets. The event is co-sponsored by the Center for
Helioanalytics, Computational and Information Science and Technology Office,
University of Maryland Department of Geographical Sciences, and NVIDIA. It is
supported by the NASA Center for Climate Simulation and the University of Maryland
Department of Geographical Sciences. https://heliohackweek.github.io/. <br/>
Date: 08/10/2020 <br/>
Author: Jordan A. Caraballo Vega

# Pulling and Working with the Container
A conda environment named "rapids" is available inside the container. You may use the container through Shell, or by starting a JupyterLab server inside the container to accessing the instance from your local browser. 
```
singularity pull docker://nasanccs/helio-hackweek2020 # pull singularity image
singularity shell helio-hackweek2020_latest.sif       # get an interactive shell inside the image
source activate rapids                                # activate conda environment with all the available libraries
```
# Main Packages
```
base: rapids ai cuda 10.1 container
additional packages:
         TensorFlow, Keras, SKLearn, Numpy, Pandas, Scipy, Sunpy, PySPEDAS, Pyflux
         Dask, Dask-image, Astropy, Jax, Numba, RAPIDS, AIAPy, CuPy, matplotlib
```
# Build and Push Container
```
cd helio-hackweek/
docker build --tag helio-hackweek2020:1.0 .
docker login
docker tag helio-hackweek2020:1.0 nasanccs/helio-hackweek2020:latest
docker push nasanccs/helio-hackweek2020
```

# References

[1] RAPIDS AI https://rapids.ai/ <br/>
[2] Singularity https://sylabs.io/docs/ <br/>
[3] Sunpy https://github.com/sunpy/sunpy <br/>
[4] Pyspedas https://pypi.org/project/pyspedas/ <br/>
[5] Dask-image http://image.dask.org/en/latest/installation.html <br/>
[6] Astropy https://www.astropy.org/ <br/>
[7] Jax https://github.com/google/jax <br/>
[8] Aiapy https://pypi.org/project/aiapy/ <br/>
[9] Pyflux https://longervision.github.io/2018/12/20/Finance/time-series-4-python-with-pyflux/
[10] NGC Containers https://developer.nvidia.com/blog/how-to-run-ngc-deep-learning-containers-with-singularity/
[11] DockerHub Container https://hub.docker.com/repository/docker/nasanccs/helio-hackweek2020/general

# Dockerfile
The Dockerfile for this repository lives in the following GitHub repository https://github.com/jordancaraballo/hpc-containers


$ docker run --gpus all --rm -it -p 8888:8888 -p 8787:8787 -p 8786:8786 \
         nvcr.io/nvidia/rapidsai/rapidsai:cuda10.2-runtime-ubuntu18.04

NOTE: This will open a shell with JupyterLab running in the background on port 8888 on your host machine.
