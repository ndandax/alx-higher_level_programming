#!/bin/bash
#sending request to url
curl -s -o /dev/null -w '%{size_download}' $1
