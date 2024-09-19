#!/bin/bash
while ! curl -s http://selenium:4444/wd/hub/status > /dev/null; do
  echo "Waiting for Selenium to be ready..."
  sleep 1
done
echo "Selenium is ready!"