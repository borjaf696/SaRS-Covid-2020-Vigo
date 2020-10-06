contigs=$1
dir=$2
ref=$3
sam="$dir/contigs_aligned.sam"
bam="$dir/contigs_aligned.bam"
sortedbam="$dir/contigs_aligned.sorted.bam"
tsv="$dir/contigs_variants.tsv"
bowtie2 -x ../bowtie_index/covid/covid -f $contigs -S $sam && samtools view -bS $sam > $bam && samtools sort $bam -o $sortedbam && samtools index $sortedbam
samtools mpileup --reference $ref -A -d 600000 -F 0 -B -Q 0 $sortedbam | ivar variants -p $tsv -q 20 -t 0.0
