cd /home/arpita/Documents/Latest-Work/Tandy_ds/gene-trees-miss
current_directory=$(pwd)
for d in ${current_directory}/*; do
  if [ -d "$d" ]; then
    cd "$d"
    for d1 in ${d}/*; do
	  if [ -d "$d1" ]; then
	    echo "$d1"
	    cat  ${d1}/true-genes.tre >> /home/arpita/Documents/Latest-Work/True_Gene_Trees.tre
	    cat  ${d1}/true-species.tre >> /home/arpita/Documents/Latest-Work/True_Species_Trees.tre	    
	  fi
	done
	cd ..

  fi
done