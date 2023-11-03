#!/bin/bash
# Runs the sonar_qube scanner
docker run \
    --rm \
    -e SONAR_HOST_URL="http://host.docker.internal:9000" \
    -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=vu-systems-quality" \
    -e SONAR_TOKEN="sqp_37f320ed9c9bad984dac10052d0bf1856e273743" \
    -v "/Users/martynasjasinskas/vu-programu-kokybe:/usr/src" \
    sonarsource/sonar-scanner-cli
