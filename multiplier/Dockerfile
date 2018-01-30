FROM python:3.6
COPY . /opt/multi/
RUN cd /opt/multi && \
    pip3.6 install -r requirements.txt
EXPOSE 5053
CMD ["python3.6", "/opt/multi/multi.py"]