import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepat, top):
	for path , dirlist, filelist in os.walk(top):
		for name in filelist:
			yield os.path.join(path, name)

def gen_opener(filenames):
	for filename in filenames:
		if filename.endswith('.gz'):
			f = gzip.open(filename, 'rt')
		elif filename.endswith('.bz2'):
			f = bz2.open(filename, 'rt')
		else:
			f= open(filename, 'rt')
		yield f

		f.close()


def gen_concatenate(iterators):

	for it in iterators:
		yield from it


def gen_grep(pattern, lines):
	pat = re.compile(pattern)
	for line in lines:
		if pat.search(line):
			yield line

listNumbers= open('Location of input file', 'rt')
filw= open('Location of files to search through', 'w')
for number in listNumbers:
	number = ''.join(number.split())
	if len(number) >= 10: 
		lognames = gen_find('', '.')
		files = gen_opener(lognames)
		lines = gen_concatenate(files)
		pylines = gen_grep('(?i)'+ number, lines)
		for line in pylines:
			filw.write(line+"\n")
			
			
