#!/usr/bin/env sh

if [ -d node_modules ]; then
  rm -rf node_modules
fi

npm install html5shiv

rm -rf js/html5shiv/resources/*
mv node_modules/html5shiv/dist/* js/html5shiv/resources/
rm -rf node_modules
