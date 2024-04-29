FROM node:21-alpine

COPY . /app
WORKDIR /app

RUN npm install --legacy-peer-deps

CMD ["npm", "run", "deploy"]
