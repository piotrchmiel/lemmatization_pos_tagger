#!/bin/bash
echo "***** Unpacking classifiers *****"

if ! which xz > /dev/null; then
    echo "No xz found. Please install it first."
    exit
fi

find "${BASH_SOURCE[0]%/*}/Classifiers" -name "*.xz" -exec xz -d {} \;

echo "***** All done *****"
