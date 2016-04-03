#!/bin/bash

echo "***** Unpacking classifiers *****"
if ! [ -x "$(command -v xz)" ] ; then
    echo "Error: xz is not installed. Cannot continue."
    exit 1
fi

find "${BASH_SOURCE[0]%/*}/Classifiers" -name "*.xz" -exec xz -dk {} \;

echo "***** All done *****"
