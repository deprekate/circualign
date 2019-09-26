# circulaline
A tool to align circular genomes on a common feature


A set of four identical circular "genomes", where the first three are offset and the fourth is reverse complemented.
```sh
$ cat genomes/*
>one
aaaaaaaaaaaaaaaaaaaaccccccccccccccccccccttttttttttttttttttttgggggggggggggggggggg
>two
aaaaaaaaaaaccccccccccccccccccccttttttttttttttttttttggggggggggggggggggggaaaaaaaaa
>thre
ggggggggggggggggggggaaaaaaaaaaaaaaaaaaaacccccccccccccccccccctttttttttttttttttttt
>four
tttttttttccccccccccccccccccccaaaaaaaaaaaaaaaaaaaaggggggggggggggggggggttttttttttt
```

1. The first step is finding a common starting point.  One way to do this is to supply a marker sequence/gene to blastn (the -dust and -word_size flags are for this specific small example, and not needed for typical queries).
2. The tab delimited output from blast is then piped to the script `get_locations.py`, which determines the alignment direction (same direction or reverse complemented) and pulls out the according query start column.
3. The output is then stored in a 'locations' file.
```sh
cat genomes/* | blastn -subject marker.fasta -outfmt 6 -dust no -word_size 7 | python3 get_location.py > locations.tsv
```


```sh
$ python3 circulaline.py genomes/ locations.tsv 
>one
aaaaccccccccccccccccccccttttttttttttttttttttggggggggggggggggggggaaaaaaaaaaaaaaaa
>two
aaaaccccccccccccccccccccttttttttttttttttttttggggggggggggggggggggaaaaaaaaaaaaaaaa
>thre
aaaaccccccccccccccccccccttttttttttttttttttttggggggggggggggggggggaaaaaaaaaaaaaaaa
>four
aaaaccccccccccccccccccccttttttttttttttttttttggggggggggggggggggggaaaaaaaaaaaaaaaa
```



