# Borja :)
# Getting revcomp from file
from Bio import SeqIO
import os, sys, subprocess

def append_files(list_files, output_file):
        with open(output_file,'w+') as out_file:
            for f in list_files:
                with open(f,'r') as f_read:
                    for line in f_read.readlines():
                        out_file.write(line)
        return output_file

def get_revcomp_file(fw_file):
	output_file = fw_file.strip().split('.')[0]+'_comp.fasta'
	print('Output file: ',output_file)
	records = SeqIO.parse(fw_file, 'fasta')
	with open(output_file, 'w+') as f_write:
		for record in records:
			revcomp_seq = str(record.seq.reverse_complement())
			f_write.write('>'+record.id+'\n'+revcomp_seq+'\n')
	return output_file

if __name__ == '__main__':
	print('Revcomp: ', sys.argv[1])
	revcomp_file = get_revcomp_file(sys.argv[1])
	assert len(sys.argv) == 4	
	print('Append: ', sys.argv[2],' ',sys.argv[3])
	output_file = sys.argv[3].strip().split('.')[0]+'_complete.fasta'
	print('Output file: ', output_file)
	files = [sys.argv[3], revcomp_file]
	print('Appending: ', files)
	append_files(files, output_file)
