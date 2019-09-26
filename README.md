# circulaline
A tool to align circular genomes on a common feature


```sh
cat genomes/* | blastn -subject marker.fasta -outfmt 6 -dust no -word_size 7 | python3 get_location.py > locations.tsv
```

```sh
$ python3 circulaline.py genomes/ locations.tsv 
aaaaccccccccccccccccccccttttttttttttttttttttggggggggggggggggggggaaaaaaaaaaaaaaaa
aaaaccccccccccccccccccccttttttttttttttttttttggggggggggggggggggggaaaaaaaaaaaaaaaa
aaaaccccccccccccccccccccttttttttttttttttttttggggggggggggggggggggaaaaaaaaaaaaaaaa
aaaaccccccccccccccccccccttttttttttttttttttttggggggggggggggggggggaaaaaaaaaaaaaaaa
```



