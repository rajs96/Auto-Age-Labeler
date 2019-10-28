# base image
# much is adopted from Stephen Grider's course on Docker
FROM node:alpine as builder

# set working directory
WORKDIR '/app'


# install and cache app dependencies
COPY ./package.json ./
RUN npm install

COPY . .

RUN npm run build

# production server
FROM nginx
EXPOSE 3000
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/build /usr/share/nginx/html
