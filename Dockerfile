# ARG CUDA_VERSION="10.2"
# ARG CUDNN_VERSION="7.6"
# ARG UBUNTU_VERSION="20.04"
# ARG DOCKER_FROM=nvidia/cuda:$CUDA_VERSION-cudnn$CUDNN_VERSION-devel-ubuntu$UBUNTU_VERSION

# Base NVidia CUDA Ubuntu image
FROM ubuntu


RUN apt update
RUN apt-get install -y python3 python3-pip

COPY . /app
COPY requirements.txt /tmp/requirements.txt
ENV PATH="/usr/local/cuda/bin:${PATH}"

# Install paddle
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -r /tmp/requirements.txt
RUN pip install paddlepaddle==2.4.2

WORKDIR /app

EXPOSE 8080


# CMD [ "python3", "runserver.py" ]