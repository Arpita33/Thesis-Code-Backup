import numpy as np
import subprocess


def all_triplet_generator(taxa_list):
    l=len(taxa_list)
    no_of_triplets=(l*(l-1)*(l-2))/6
    #no_of_triplets.is_integer()
    #print(no_of_triplets)
    used = 0
    list3=[]

    for i in range(0,l-2):

        # print(taxa_list[i])
        pointer1=i
        elem = taxa_list[pointer1]
        elem += ','
        for j in range(1,l-used-1):
            pointer2 = pointer1+j
            elem += taxa_list[pointer2]
            elem += ','
            # print("Upto 2nd elem-> " + elem)
            # list3.append(taxa_list[pointer2])
            for k in range (1, l-pointer2):
                pointer3 = pointer2+k
                elem += taxa_list[pointer3]
                #print("Testing individual 3 taxa seq:" + elem)
                list3.append(elem)
                temp = elem.split(',')
                elem = temp[0] + ',' + temp[1] + ','

            temp = elem.split(',')
            elem = temp[0] + ','
        elem = ""
        used = used + 1

    #print(len(list3))
    return list3




taxa_map={}
genetree_list=[]
fl = open("removed_taxa_weakILSGT","r+")


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
				
#print(taxa_map.keys())

		


#print(genetree_list)
print(len(taxa_map.keys()))
three_taxa_sequence=all_triplet_generator(taxa_map.keys())
# print('three_taxa_sequence: ')
# print(three_taxa_sequence)

# print('\n')

# column_determinator={}
# val=1
# type_1=1
# type_2=2
# type_3=3
# for each_seq in three_taxa_sequence:
# 	temp2 = each_seq.split(',')
# 	t1=temp2[0]
# 	t2=temp2[1]
# 	t3=temp2[2]
# 	s1='('+t1+','+'('+t2+','+t3+'))'
# 	s2='('+t1+','+'('+t3+','+t2+'))'
# 	s3='('+t2+','+'('+t1+','+t3+'))'
# 	s4='('+t2+','+'('+t3+','+t1+'))'
# 	s5='('+t3+','+'('+t1+','+t2+'))'
# 	s6='('+t3+','+'('+t2+','+t1+'))'
# 	#s2=t1+t3+t2
	
# 	column_determinator[s1]=str(val)+','+str(type_1)
# 	column_determinator[s2]=str(val)+','+str(type_1)
# 	column_determinator[s3]=str(val)+','+str(type_2)
# 	column_determinator[s4]=str(val)+','+str(type_2)
# 	column_determinator[s5]=str(val)+','+str(type_3)
# 	column_determinator[s6]=str(val)+','+str(type_3)
# 	val+=1

# '''
# for x,y in column_determinator.items():
# 	print(x + " " + y)
# '''
# no_of_gene_trees = len(genetree_list)
# print(no_of_gene_trees)
# no_of_three_taxa_seq = len(three_taxa_sequence)
# print(no_of_three_taxa_seq)


# table = np.zeros((no_of_gene_trees,no_of_three_taxa_seq,3))


# for index,gene_tree in enumerate(genetree_list):
#     print("Working with the tree " + gene_tree)
#     with open("Tree_Input.tree", "w+") as f:
#         f.write(gene_tree)
#     subprocess.call(['./triplet-encoding-controller.sh','Tree_Input.tree','output.trip'])
#     with open("output.trip", "r") as f2:
#         data = f2.read()
#         lines=data.split("\n")
#         no_of_lines=len(lines)

#         #print("line: ")
#     	#print(lines)
#     	for i in range(0,no_of_lines-1):
#     		triplet = lines[i].split(';')[0];
#     		#print(triplet)
    		
#     		#triplet=lines[i][1]+lines[i][4]+lines[i][6]
#     		if triplet in column_determinator.keys():
    			

#     			res = column_determinator[triplet].split(',')
#     			axis_y = int(res[0])
#     			axis_z = int(res[1])

#     			#print(res[0] + " " + res[1])
#     			table[index][axis_y-1][axis_z-1] = 1
#     			'''
#     			if index == 1:
#     				print(str(index) + ", " +  triplet + ", " + str(axis_y-1) + ", " + str(axis_z-1))
#     			#print (str(index) + " " + column_determinator[triplet])
    			
#     			res = [x.strip() for x in column_determinator[triplet].split(',')]
#     			axis_y = int(res[0])
#     			axis_z = int(res[1])

#     			table[index][axis_y-1][axis_z-1] = 1
#     			#print(column_determinator[triplet][2])
#     			#axis_y=int(column_determinator[triplet])
#     			#axis_z=int(column_determinator[triplet][2])
#     			#print(axis_y+axis_z)
#     			'''

# print(table.shape)

# # test_file = open("Valid_file.npy","w+")
# # np.save(test_file,table)
# test_file = "weakILS_test_tree"
# np.save(test_file,table,allow_pickle=True,fix_imports=True)

# #test_tree_temp =  np.load("Valid_file.npy")
# #print(test_tree_temp.shape)


# '''
# print(table.shape)
# Train_file = open("Train_array.npy","w+")
# np.save(Train_file,table)

# xt = table[0]
# print(xt)

# Temp_file = open("Temp_table.txt", "w+")
# for x in table[0]:
# 	np.savetxt("Temp_table.txt"),x)

# with open("Temp_table.txt", "w+") as f:
#         f.write(table)
# #print(table)
# '''
