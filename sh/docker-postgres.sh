#!/bin/sh
docker run --name myapp-dev.db -p 8032:5432 -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -d postgres:9.6
