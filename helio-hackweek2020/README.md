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
A conda environment named "rapids" is available inside the container. You may use the container through Shell, or by starting a JupyterLab server inside the container to accessing the instance from your local browser.  The singularity container is close to 4.4GB.
```
singularity pull docker://nasanccs/helio-hackweek2020 # pull singularity image
singularity shell helio-hackweek2020_latest.sif       # get an interactive shell inside the image
source activate rapids                                # activate conda environment with all the available libraries
```
# Simple Test
MNIST CNN using TensorFlow and Keras with Mirrored distributed training for leveraging multiple GPUs.
```
ssh -X -Y hostname
singularity pull docker://nasanccs/helio-hackweek2020
singularity shell helio-hackweek2020_latest.sif
git clone https://github.com/jordancaraballo/hpc-containers
source activate rapids
python hpc-containers/helio-hackweek2020/test.py
```
# Main Packages
```
base: rapids ai cuda 10.1 docker container
additional packages:
         TensorFlow, Keras, SKLearn, Numpy, Pandas, Scipy, Sunpy, PySPEDAS, Pyflux
         Dask, Dask-image, Astropy, Jax, Numba, RAPIDS, AIAPy, CuPy, matplotlib
```
# Build and Push Container using Docker
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
[9] Pyflux https://longervision.github.io/2018/12/20/Finance/time-series-4-python-with-pyflux/ <br/>
[10] NGC Containers https://developer.nvidia.com/blog/how-to-run-ngc-deep-learning-containers-with-singularity/ <br/>
[11] DockerHub Container https://hub.docker.com/repository/docker/nasanccs/helio-hackweek2020/general

# Dockerfile
The Dockerfile for this repository lives in the following GitHub repository https://github.com/jordancaraballo/hpc-containers

# Possible Troubleshooting
1. "QStandardPaths: XDG_RUNTIME_DIR points to non-existing path '/run/user/836960261', please create it with 0700 permissions." <br/>
This warning might appear sometimes if the underlying system does not have the listed directory. A simple export pointing to an existing directory should remove this warning. <br/>
```
(rapids) Singularity> export XDG_RUNTIME_DIR=/home/username
```
2. Need to perform changes to the existing image
```
sudo -E singularity build --sandbox image.sif docker://nasanccs/helio-hackweek2020
sudo singularity shell --writable image.sif
# perform any changes, and they will be stored in disk
```
3. X11 not working <br/>
Make sure X11 is configured in the underlying system, and that the user running singularity has access to run X11. Make sure the following packages are installed.
```
xorg-x11-fonts-* xorg-x11-xauth # for CentOS 7
```
4. File system out of space while building the Singularity container <br/>
Make sure the following environment variables are defined in your ~/.bashrc file, and that they point to a place that has more than 8GB of space. Also, make sure you build the image using the -E option if using sudo.
```
export SINGULARITY_CACHEDIR="/path/with/space/singularity"
export SINGULARITY_TMPDIR="/path/with/space/singularity"
```
5. qt.qpa.xcb: could not connect to display. Aborted. <br/>
This happens when loading the PySPEDAS library without X11 configured. Make sure libraries from (3) are installed and that you SSH to the system using the following command.
```
ssh -X -Y hostname
```
Or, if X11 is not required, feel free to run the following command before requesting a shell inside the singularity container.
```
export QT_QPA_PLATFORM=offscreen
```
