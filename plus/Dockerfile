FROM python:3.6
COPY . /opt/plus/
RUN cd /opt/plus && \
    pip3.6 install -r requirements.txt
EXPOSE 5051
CMD ["python3.6", "/opt/plus/plus.py"]