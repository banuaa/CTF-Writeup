#!/bin/sh
export name="mysimplewebsite"
export port="4444"
docker build --tag=$name .
docker run -p $port:4444 --rm --name=$name $name