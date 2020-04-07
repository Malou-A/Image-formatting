# .C01 to .tiff format

## Usage
```bash
python3 C01_to_tiff -i INDIR -o OUTDIR
```
Choose a directory with your .C01 files to convert, and name the output directory where you want to place the .tiff converted images.



## Installation

Download bftools and unzip it to your /home/bin folder and add to path:

```bash
cd ~/bin
wget http://downloads.openmicroscopy.org/latest/bio-formats/artifacts/bftools.zip
unzip bftools.zip
rm bftools.zip
export PATH=$PATH:~/bin/bftools
```

Required python packages
```python
pip install argparse
pip install os
pip install subprocess
pip install tqdm
pip install pathlib
```

