#Randomized Contraction Algorithm for computing minimum cut of undirected graph
import random

def rand_contr_algo(adj_lst):
    # 1 loop
    # each time loop iterates, num of vertices reduced by 1 until only 2 vertices remain
    # pick edge to contract uniformly at random
    # take 2 endpoints of randomly chosen edge and fuse into 1 vertex
    # remove self loops
    # return number of edges connected last 2 vertices

    # input: adjacency list-- column 1: vertex label
    #                         all other columns: all vertices that vertex is adjacent to
    for row_ind, row in enumerate(adj_lst):
        # choose 2 random vertices that comprise a "random edge"
        if row_ind < len(adj_lst)-2:
            # first random vertex row chosen
            rand_row1 = random.choice(adj_lst)

            # make sure random row chosen has not already been "contracted"
            while rand_row1 == 0:
                rand_row1 = random.choice(adj_lst)

            # first entry of row corresponds to vertex
            rand_vert1 = rand_row1[0]

            # second random vertex chosen from list of adjacent vertices to rand_vert1
            rand_vert2_ind = random.randint(1, len(rand_row1) - 1)
            rand_vert2 = adj_lst[rand_vert1-1][rand_vert2_ind]

            # make sure you didn't randomly choose adjacent vertex to be itself
            while rand_vert2 == rand_vert1:
                rand_vert2_ind = random.randint(1, len(rand_row1) - 1)
                rand_vert2 = adj_lst[rand_vert1 - 1][rand_vert2_ind]

            # *Edge Contraction*

            # reassign ownership of edge to new "fused" vertex (in this case its rand_vert1):
            # choose adj_lst row indexed by rand_vert2 and loop over all adjacent vertices to rand_vert2
            # for every row in adj_lst indexed by adjacent vertices to rand_vert2, remove rand_vert2 and replace with
            # rand_vert1 since contraction abstractly got rid of rand_vert2 and all its edges now belong to rand_vert1
            for vert in adj_lst[rand_vert2-1]:
                if vert != rand_vert2:
                    # go to row indexed by vert and remove all entries == rand_vert2
                    adj_lst[vert - 1] = [x for x in adj_lst[vert-1] if x != rand_vert2]
                    if vert != rand_vert1:
                        # replace rand_vert2 with rand_vert1(appended to end of list)
                        adj_lst[vert-1].append(rand_vert1)

            # remove any duplicates of rand_vert1 from row corresponding to rand_vert2 (contraction of edge)
            adj_lst[rand_vert2 - 1] = [y for y in adj_lst[rand_vert2 - 1] if y != rand_vert1]

            # take all adjacent vertices of rand_vert2(corresponding row) and append them to rand_row1
            adj_lst[rand_vert1-1] = adj_lst[rand_vert1-1] + adj_lst[rand_vert2-1][1:]

            #remove random row corresponding to rand_vert2--replace with "0"
            adj_lst[rand_vert2-1] = 0

        else:
            #filter out all "0" from list
            adj_lst = [z for z in adj_lst if z != 0]

    #return min cut which is number of adjacent vertices for any vertex(row in adj list)
    return len(adj_lst[0])-1

with open('kargerMinCut.txt') as f:
    adj_lst = f.readlines()

#adjacency list: each entry containing list of adjacent vertices
for row_ind, row in enumerate(adj_lst):
    #convert row of str to row of int
    adj_lst[row_ind] = map(int, row.split())

min_cut = rand_contr_algo(adj_lst)
print("Minimum Cut:")
print(min_cut)


