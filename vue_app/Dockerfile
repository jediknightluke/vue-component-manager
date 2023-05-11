# vue_app/Dockerfile
FROM node:lts

WORKDIR /app

COPY package.json yarn.lock .eslintrc.* ./
RUN yarn install

COPY . .
RUN yarn build

CMD ["yarn", "serve"]
