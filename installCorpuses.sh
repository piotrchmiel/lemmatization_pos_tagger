#!/bin/bash

EXITCODE=0

echo "***** Checking if needed packages are installed *****"
if ! [ -x "$(command -v 7z)" ] ; then
    echo "Error: 7z is not installed."
    EXITCODE=1
fi

if ! [ -x "$(command -v wget)" ] ; then
    echo "Error: wget is not installed."
    EXITCODE=1
fi

if ! [ -x "$(command -v tar)" ] ; then
    echo "Error: tar is not installed."
    EXITCODE=1
fi

if [ "$EXITCODE" -ne 0 ] ; then
    echo "Please install necessary packages and run me again!"
    exit 1
fi


echo "***** Unpacking CorpusPwr *****"
if ! [ -d "CorpusPWr" ] ; then
    mkdir "CorpusPWr"
fi
7z x ./kpwr-1.2.6-disamb.7z -oq./CorpusPWr/ -y -r > /dev/null
EXITCODE=$?
if [ "$EXITCODE" -ne 0 ] ; then
    echo "Error: Unpacking went wrong. 7z returned: $EXITCODE."
    exit 1
fi


echo "***** Downloading NationalCorpus 1.2 *****"
if ! [ -d "NationalCorpus" ] ; then
    mkdir "NationalCorpus"
fi
wget -O ./NationalCorpus/NKJP-PodkorpusMilionowy-1.2.tar.gz "http://clip.ipipan.waw.pl/NationalCorpusOfPolish?action=AttachFile&do=get&target=NKJP-PodkorpusMilionowy-1.2.tar.gz"
EXITCODE=$?
if [ "$EXITCODE" -ne 0 ] ; then
    echo "Error: Downloading went wrong. wget returned: $EXITCODE."
    exit 1
fi


echo "***** Unpacking NationalCorpus *****"
tar -zxf ./NationalCorpus/NKJP-PodkorpusMilionowy-1.2.tar.gz -C ./NationalCorpus/
EXITCODE=$?
if [ "$EXITCODE" -ne 0 ] ; then
    echo "Error: Unpacking went wrong. tar returned: $EXITCODE."
    exit 1
fi


echo "***** All done *****"
