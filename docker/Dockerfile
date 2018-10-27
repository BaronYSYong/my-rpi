FROM resin/raspberry-pi-python:latest

RUN READTHEDOCS=True \
    apt-get update && apt-get install -y \
    software-properties-common wget lsb-release && \
    pip install picamera

ENV RESOLUTION=800x600 \
    FRAMERATE=24

CMD ["/bin/bash"]
