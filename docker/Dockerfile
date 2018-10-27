FROM resin/raspberry-pi-python:latest

RUN READTHEDOCS=True \
    pip install picamera

ENV RESOLUTION=800x600 \
    FRAMERATE=24

CMD ["/bin/bash"]
