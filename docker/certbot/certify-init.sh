#!/bin/bash

# Waits for proxy to be available, then gets the first cert.

set -e

until nc -z proxy:80; do
    echo "Waiting for porxy..."
    sleep 5s & wait ${!}
done

echo "Getting certificate..."

certbot certonly \
    --webroot \
    --webroot-path "/vol/www/" \
    -d "$DOMAIN" \
    --email $EMAIL \
    --rsa-key-size 4096 \
    --agree-tos \
    --noninteractive