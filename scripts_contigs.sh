contigs=$1
index=$2
echo 'Index: '$index
echo 'Contigs: '$contigs
# --norc avoid reverse complement alignment
bowtie2 -x $index -f $contigs --un matches_rev_comp.fa --al matches_ref.fa -S output.sam --very-sensitive --norc
