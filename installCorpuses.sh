echo "***** Checking if needed packages are installed *****"

if ! which 7z > /dev/null; then
    echo "No 7z found. Please install it first."
    exit
fi

if ! which wget > /dev/null; then
    echo "No wget found. Please install it first."
    exit
fi

if ! which tar > /dev/null; then
    echo "No tar found. Please install it first."
    exit
fi

echo "***** Unpacking CorpusPwr *****"

if [ ! -d "CorpusPWr" ]; then
    mkdir "CorpusPWr"
fi

7z x ./kpwr-1.2.6-disamb.7z -o./CorpusPWr/ -y -r

echo "***** Downloading NationalCorpus 1.2 *****"

if [ ! -d "NationalCorpus" ]; then
    mkdir "NationalCorpus"
fi

wget -O ./NationalCorpus/NKJP-PodkorpusMilionowy-1.2.tar.gz "http://clip.ipipan.waw.pl/NationalCorpusOfPolish?action=AttachFile&do=get&target=NKJP-PodkorpusMilionowy-1.2.tar.gz"

echo "***** Unpacking NationalCorpus *****"

tar -zxvf ./NationalCorpus/NKJP-PodkorpusMilionowy-1.2.tar.gz -C ./NationalCorpus/

echo "***** All done *****"
