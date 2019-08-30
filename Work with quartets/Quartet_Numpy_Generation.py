import numpy as np
import subprocess
import collections

def three_taxa_seq_generator(taxa_list):
	l=len(taxa_list)
	no_of_triplets=(l*(l-1)*(l-2))/6
	used = 0
	list3=[]

	for i in range(0,l-2):
		pointer1=i
		elem = taxa_list[pointer1]
		elem += ','
		for j in range(1,l-used-1):
			pointer2 = pointer1+j
			elem += taxa_list[pointer2]
			elem += ','
			for k in range (1, l-pointer2):
				pointer3 = pointer2+k
				elem += taxa_list[pointer3]
				list3.append(elem)
				temp = elem.split(',')
				elem = temp[0] + ',' + temp[1] + ','
			temp = elem.split(',')
			elem = temp[0] + ','
		elem = ""
		used = used + 1

	return list3


def four_taxa_seq_generator(taxa_list):
	length=len(taxa_list)
	ret_list=[]
	for i in range(0,length-3):
		three_taxa_seq=three_taxa_seq_generator(taxa_list[i+1:])
		for j in range(0,len(three_taxa_seq)):
			seq=three_taxa_seq[j]
			seq_ret=taxa_list[i]+','+seq
			ret_list.append(seq_ret)
	return ret_list



def get_taxa_list_AND_gene_tree_list(input_file):
	taxa_map={}
	genetree_list=[]
	fl = open(input_file,"r+")
	while True:
		line = fl.readline().strip()
		if line == '':
			break
		else:
			genetree_list.append(line)
			xl = line.split(',')
			for i in range(0,len(xl)):
				xl[i] = xl[i].replace('(','')
				xl[i] = xl[i].replace(')','')
				xl[i] = xl[i].replace(';','')

			for x in xl:
				if(x not in taxa_map.keys()):
					taxa_map[x] = 1

	taxa_map = collections.OrderedDict(sorted(taxa_map.items()))
	taxa_list=[]
	for key,value in taxa_map.items():
		taxa_list.append(key)
	return (taxa_list,genetree_list)

def get_column_determinator(four_taxa_sequence):
	output_map={}
	column_determinator={}
	val=1
	type_1=1
	type_2=2
	type_3=3
	for each_seq in four_taxa_sequence:
		output_map[val]=each_seq
		temp2 = each_seq.split(',')
		t1=temp2[0]
		t2=temp2[1]
		t3=temp2[2]
		t4=temp2[3]
		s1='('+'('+t1+','+t2+')'+','+'('+t3+','+t4+')'+')'
		s2='('+'('+t1+','+t2+')'+','+'('+t4+','+t3+')'+')'
		s3='('+'('+t2+','+t1+')'+','+'('+t3+','+t4+')'+')'
		s4='('+'('+t2+','+t1+')'+','+'('+t4+','+t3+')'+')'

		s5='('+'('+t1+','+t3+')'+','+'('+t2+','+t4+')'+')'
		s6='('+'('+t1+','+t3+')'+','+'('+t4+','+t2+')'+')'
		s7='('+'('+t3+','+t1+')'+','+'('+t2+','+t4+')'+')'
		s8='('+'('+t3+','+t1+')'+','+'('+t4+','+t2+')'+')'

		s9='('+'('+t1+','+t4+')'+','+'('+t2+','+t3+')'+')'
		s10='('+'('+t1+','+t4+')'+','+'('+t3+','+t2+')'+')'
		s11='('+'('+t4+','+t1+')'+','+'('+t2+','+t3+')'+')'
		s12='('+'('+t4+','+t1+')'+','+'('+t3+','+t2+')'+')'
		#s2=t1+t3+t2
		
		column_determinator[s1]=str(val)+','+str(type_1)
		column_determinator[s2]=str(val)+','+str(type_1)
		column_determinator[s3]=str(val)+','+str(type_1)
		column_determinator[s4]=str(val)+','+str(type_1)

		column_determinator[s5]=str(val)+','+str(type_2)
		column_determinator[s6]=str(val)+','+str(type_2)
		column_determinator[s7]=str(val)+','+str(type_2)
		column_determinator[s8]=str(val)+','+str(type_2)

		column_determinator[s9]=str(val)+','+str(type_3)
		column_determinator[s10]=str(val)+','+str(type_3)
		column_determinator[s11]=str(val)+','+str(type_3)
		column_determinator[s12]=str(val)+','+str(type_3)
		val+=1
	with open("FourTaxaSeqMap", "w+") as f:
		f.write(str(output_map))
	return column_determinator



def get_numpy_array(genetree_list,four_taxa_sequence,column_determinator):
	no_of_gene_trees = len(genetree_list)
	no_of_four_taxa_seq = len(four_taxa_sequence)
	table = np.zeros((no_of_gene_trees,no_of_four_taxa_seq,3))
	count=0
	for index,gene_tree in enumerate(genetree_list):

		#print("Index-> "+ str(index) + "\nWorking with the tree " + gene_tree)
		if(index != -1):
			with open("Tree_Input.tree", "w+") as f:
			    f.write(gene_tree)
			subprocess.call(['./quartet-controller.sh','Tree_Input.tree','output.quartets'])
			with open("output.quartets", "r") as f2:
			    data = f2.read()
			    lines=data.split("\n")
			    no_of_lines=len(lines)

			for i in range(0,no_of_lines-1):
				quartet = lines[i].split(';')[0];
				if quartet in column_determinator.keys():
					
					count+= 1
					res = column_determinator[quartet].split(',')

					axis_y = int(res[0])
					axis_z = int(res[1])
					table[index][axis_y-1][axis_z-1] = 1

	test_file = "output_numpy_array"
	np.save(test_file,table,allow_pickle=True,fix_imports=True)
	#print(table)


def main():	
	input_file="StrongILS_ALLGT"	
	taxa_list,genetree_list=get_taxa_list_AND_gene_tree_list(input_file)
	four_taxa_sequence=four_taxa_seq_generator(taxa_list)
	column_determinator=get_column_determinator(four_taxa_sequence)
	get_numpy_array(genetree_list,four_taxa_sequence,column_determinator)

	

if __name__== "__main__":
  main()
				
