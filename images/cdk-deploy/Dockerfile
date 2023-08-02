FROM node:20

RUN apt-get -y update && apt-get -y install --no-install-recommends python3-pip npm curl zip groff python3-virtualenv
RUN npm install -g aws-cdk

RUN curl -sSL https://get.docker.com/ | sh

COPY requirements.txt .

RUN pip3 install -r requirements.txt --break-system-packages

COPY ship-it.sh /usr/local/bin/ship-it
RUN chmod a+x /usr/local/bin/ship-it

ENTRYPOINT [ "/usr/local/bin/ship-it" ]
