import partition
import matplotlib.pyplot as plt
import random

snclusters = []

for I in xrange(1,10):
    p = partition.Partition()
    p.reset()

    N = 100000

    nclusters = []

    # First customer sits at the first table
    p.add_cluster(1)

    for n in xrange(1, N):
        customers_in_restaurant = p.get_sum()
        r = random.randrange(0, customers_in_restaurant + 1)
    
        if r == 0:
            p.add_cluster(1)
        else:
            r = r - 1
            for table_number, number_seated in enumerate(p.get_clusters()):
                if number_seated > r:
                    p.update_cluster(table_number, number_seated+1)
                    break
                r = r - number_seated
    
        nclusters.append(p.number_of_clusters())
    snclusters.append(nclusters)

