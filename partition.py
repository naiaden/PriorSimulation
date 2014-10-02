class Partition:
    clusters = []

    def get_sum(self):
        return sum(self.clusters)

    def number_of_clusters(self):
        return len(self.clusters)

    def add_cluster(self, size=0):
        self.clusters.append(size)

    def update_cluster(self, cluster, size):
        self.clusters[cluster] = size

    def reset(self):
        self.clusters = []

    def get_clusters(self):
        return self.clusters

    def print_clusters(self):
        print ', '.join(str(c) for c in self.clusters)
