#!/usr/bin/env sh# Getting static files for Admin panel hosting!
uwsgi --http "0.0.0.0:${PORT}" --module lilisSchool.wsgi --master --processes 4 --threads 2
