FROM aehrc/quickumls-rest:1.2.3-2018AA 

LABEL maintainer="Bevan Koopman <bevan.koopman@csiro.au>"

# Install requirements
ADD requirements.txt /app
RUN pip install -r requirements.txt

# Add the app
ADD . /QuickUMLS-1.2.3

CMD python3 server.py /quickumls-data-2018AA-L
