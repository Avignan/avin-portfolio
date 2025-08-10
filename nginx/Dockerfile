# Initiates nginx container
FROM nginx:alpine

# Initiates removal of default nginx config
RUN rm /etc/nginx/conf.d/default.conf

# Initiates copying of custom nginx config
COPY nginx.conf /etc/nginx/nginx.conf

# Initiates creating of directories for static files
RUN mkdir -p /var/www/static

# Initiates what ports will the nginx listen to
EXPOSE 80 443