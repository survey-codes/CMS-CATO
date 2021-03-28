FROM nginx:1.17.8

RUN rm /etc/nginx/conf.d/default.conf
ADD sites_enabled/ /etc/nginx/conf.d/
RUN ls -l /etc/nginx/conf.d/

EXPOSE 8003

