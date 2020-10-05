# SaRS-Covid-2020-Vigo

Contigs reportados por viaDBG para los datasets provistos. Salvo para el directorio "33_0/" que se corresponde con el dataset 3.C3_0 el resto solo contienen los contigs reportados en formato fasta, . En el caso de 3.C3_0 o 33_0 se tienen más documentos para poder realizar la visualización de las variantes via sequencetubemap (https://github.com/vgteam/sequenceTubeMap).

La información provista por directorio sería:
 * Contigs reportados por viaDBG - el nombre del archivo hace referencia a: "dataset.kmer_size.fa"
 * Consensus (ivar) por dataset - consensus.fa
 * Evaluación de resultados a través de metaquast (https://github.com/ablab/quast)
   
   * MN908947.3 as reference.
   * Consensus as reference.
 * Variantes reportadas por iVar.

# Table summary reports

| Dataset | #Contigs (>500 bp) | N50   | Mismatches (100kbp) (consensus) | Mismatches (100kbp) (reference) | % Genome Fraction (consensus) | Bases aligned (consensus) | % Genome Fraction (reference) | Bases aligned (reference) | Total bases | % Aligned (consensus) | Largest Alignment |
|---------|--------------------|-------|---------------------------------|---------------------------------|-------------------------------|---------------------------|-------------------------------|---------------------------|-------------|-----------------------|-------------------|
| 33_0    | 23                 | 6577  | 20.51                           | 61.54                           | 98.08                         | 99368                     | 97.82                         | 99368                     | 99383       | 99.98                 | 11289             |
| 33_38   | 30                 | 10621 | 23.84                           | 85.13                           | 98.47                         | 165885                    | 98.21                         | 165885                    | 165907      | 99.98                 | 18870             |
| 33_380  | 39                 | 13908 | 20.43                           | 173.65                          | 98.45                         | 306445                    | 98.21                         | 306445                    | 306475      | 99.99                 | 19255             |
| 33_3_80 | 35                 | 10093 | 23.65                           | 131.75                          | 99.26                         | 228064                    | 98.99                         | 228064                    | 228097      | 99.99                 | 19486             |
| 84_0    | 28                 | 11102 | 23.63                           | 246.41                          | 99.32                         | 216589                    | 99.07                         | 216589                    | 216609      | 99.98                 | 22292             |
| 84_38   | 28                 | 7270  | 23.68                           | 186.04                          | 99.12                         | 133741                    | 98.86                         | 133741                    | 133761      | 99.99                 | 11035             |
| 84_380  | 26                 | 10208 | 23.63                           | 195.77                          | 99.33                         | 151855                    | 99.07                         | 151855                    | 151877      | 99.98                 | 15979             |
| 84_3_80 | 20                 | 11286 | 20.25                           | 195.79                          | 99.32                         | 175922                    | 99.06                         | 175922                    | 175937      | 99.99                 | 22293             |

La tabla de resultados muestra una recopilación de estadísticos de importancia en la evaluación de los ensambladores tradicionales:
  * #Contigs o número de contigs de más de 500 bases de longitud - el número reportado por viaDBG suele ser ligeramente más alto del ideal pues comete en ocasiones el error de construir vías duplicadas (en vías de arreglo).
  * N50 o "media" de la longitud de los contigs, entendiendo en este caso la "media" como el contig de menor tamaño tal que con contigs de todo tamaño superior se alcanza el 50% de la longitud del genoma de referencia.
  * Se muestran los resultados de mismatches, % genoma recuperado, bases alineadas, bases total y alineamiento más largo frente a la secuencia consenso producida con el pipeline de iVar (https://github.com/andersen-lab/ivar) y frente a la referencia original (MN908947.3).
