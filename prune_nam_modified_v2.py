#!/lusr/bin/python
'''
Created on Jun 3, 2011

@author: namphuon
'''
import dendropy
from dendropy import Tree
from dendropy import TreeList
import sys
import os


##################### IMPORTANT dendropy 3.8.1 is required

if __name__ == '__main__':
    
    taxonRemoveFile = sys.argv[1]
    treeName = sys.argv[2]
    outFile = sys.argv[3]
    
    print "Prunning %s according to %s to %s" %(treeName,taxonRemoveFile ,outFile)
   # tree = Tree(stream=open(treeName,"r"), schema='newick', as_rooted=True)  # as_rooted=True na hole tree gulak unrooted hishabe treat korbe
    #tree = TreeList.get_from_path(treeName, 'newick')
    trees = dendropy.TreeList.get_from_path(treeName, 'newick',as_rooted=True,preserve_underscores=True)
    # prune all taxa 	    
    handle = open(taxonRemoveFile,"r")	    
    line = handle.readline()
    taxon_sets = line.split()
    handle.close()

    out = open(outFile,'w');   	
    for tree in trees:	
	    prTree= Tree(tree)
	    prTree.prune_taxa_with_labels(taxon_sets, update_splits=True, delete_outdegree_one=True)        
            s = prTree.as_newick_string()
            s = s[0:s.rfind(")")+1]
	    out.write(s);
	    out.write(";\n")	
    out.close()
