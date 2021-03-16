FROM python:alpine3.7 
COPY ./app01.py /app
WORKDIR /app
RUN pip3 install -r requirements.txt 
EXPOSE 1146 
ENTRYPOINT [ "python" ] 
CMD [ "app01.py" ] 