#!/usr/bin/env bash
nohup gunicorn alex_blog.wsgi:application --bind 0.0.0.0:8000 -w=4 -k=gevent &
