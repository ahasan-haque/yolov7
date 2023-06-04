# Use an official Python runtime as the base image

FROM python:3.9-slim

# Set the working directory
WORKDIR /app
COPY . /app

WORKDIR /app

# # need to run on /bin/bash mode
RUN apt update || true \
       && apt install -y software-properties-common \
       && add-apt-repository ppa:deadsnakes/ppa \
       && apt install -y unzip git vim build-essential \
       zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev \
       libssl-dev libreadline-dev libffi-dev wget build-essential \
       cmake git libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev \
       libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev \
       libv4l-dev v4l-utils libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
       libgtk2.0-dev mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev \
       libatlas-base-dev gfortran libeigen3-dev python3-dev python3-numpy 

RUN python3.9 -m pip install --upgrade pip && python3.9 -m pip install -r seg/requirements.txt

RUN git clone https://github.com/ahasan-haque/yolov7_object_detection

WORKDIR /app/yolov7_object_detection/seg

CMD sh -c 'python3.9 segment/predict.py'