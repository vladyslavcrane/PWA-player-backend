FROM nginx:latest

RUN apt update && apt -qy install vim

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/nginx.conf
COPY player_backend.conf /etc/nginx/conf.d/
COPY proxy_params /etc/nginx/proxy_params
