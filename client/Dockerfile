FROM node:8

WORKDIR /usr/src/client

COPY package.json .

RUN npm i

COPY . .

RUN chown -R node /usr/src/client

USER node