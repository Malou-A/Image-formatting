# Change image format

## Usage
```bash
python3 format_convertion.py -i INDIR -o OUTDIR -ift IN_FILETYPE -oft OUT_FILETYPE
```
Choose a directory with your files to convert, which format they are (e.g. C01, png, tiff, jpg), and name the output directory where you want to place the converted images, and what format you want to convert them to (e.g. C01, png, tiff, jpg).



## Installation

Download bftools and unzip it to your /home/bin folder and add to path:

```bash
cd ~/bin
wget http://downloads.openmicroscopy.org/latest/bio-formats/artifacts/bftools.zip
unzip bftools.zip
rm bftools.zip
export PATH=$PATH:~/bin/bftools
```
Download and install java (Link is for Linux x64)

```bash
cd ~/bin
wget https://javadl.oracle.com/webapps/download/AutoDL?BundleId=242980_a4634525489241b9a9e1aa73d9e118e6
tar zxvf jre-8u73-linux-x64.tar.gz
export PATH=$PATH:~/bin/jre-8u73-linux-x64
```

Required python packages
```python
pip install argparse
pip install os
pip install subprocess
pip install tqdm
pip install pathlib
```

