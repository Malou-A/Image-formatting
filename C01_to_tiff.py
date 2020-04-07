#!/usr/bin/python3

import argparse
import os
import os.path
import subprocess
from tqdm import tqdm
from pathlib import Path


usage = 'Enter the directory name of the C01 files, and name a directory where you want the tiff files to end up.'
parser = argparse.ArgumentParser(description=usage)

parser.add_argument(
	'-i',
	dest = 'infile',
	metavar = 'INDIR',
	type = str,
    help = 'set the directory where the .C01 files are located',
	required = True
	)

parser.add_argument(
	'-o',
	dest = 'outfile',
	metavar = 'OUTDIR',
	type = str,
    help = 'set the directory to store the .tiff files',
	required = True
	)

args = parser.parse_args()

input_dir = os.path.abspath(args.infile)
output_dir = os.path.abspath(args.outfile)
my_file = Path(output_dir)
if not my_file.exists():
    os.mkdir(output_dir)

if not os.path.isdir(input_dir):
    raise argparse.ArgumentTypeError('Input must be a directory')
if not os.path.isdir(output_dir):
    raise argparse.ArgumentTypeError('Output must be a directory')

C01_files = []
tiff_files = []
os.chdir(input_dir)
for i in os.listdir():
    C01_files.append(input_dir + '/' + i)
    tiff_files.append(output_dir + '/' + i.split('.')[0] + '.tiff')

for i,j in tqdm(zip(C01_files,tiff_files), total = len(C01_files)):
    subprocess.run(['bfconvert', '-overwrite', '-nogroup',i,j],stdout = subprocess.PIPE, stderr = subprocess.DEVNULL) #Runs bftools which needs to be preinstalled, output to DEVNULL.
    subprocess.run(['convert', i, '-auto-level', '-depth', '16', '-define', 'quantum:format=unsigned', '-type', 'grayscale', j],stdout = subprocess.PIPE, stderr = subprocess.DEVNULL) #Convert images to 16-bits tiff images.
