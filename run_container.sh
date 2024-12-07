#!/bin/bash
# run lxn_d2l:1.0 container and mount the host directory to the container
docker run -it --privileged --name divp --ipc=host --gpus=all \
    -v /home/lxn/DIVP_test:/root/DIVP_test \
    divp:1.0 \
    /bin/bash
