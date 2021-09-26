import Litmus.Genetics.population as lg

class LitmusGenetics:
    population_size = 0
    mutation_rate = 0
    search_space = ()
    vector_size = 0

    def setVectorSize(self, vector_size):
        self.vector_size = vector_size


    def setPopulationSize(self, population_size):
        self.population_size = population_size

    def setMutationRate(self, mutation_rate):
        self.mutation_rate = mutation_rate

    def setSearchSpace(self, lower_bound, upper_bound):
        self.search_space = (lower_bound, upper_bound)


    def getPopulationSize(self, population_size):
        return self.population_size

    def getMutationRate(self, mutation_rate):
        return self.mutation_rate

    def getSearchSpace(self, lower_bound, upper_bound):
        return self.search_space

    def initialize(self, vector_size, population_size, mutation_rate, search_space):
        self.setPopulationSize(population_size)
        self.setVectorSize(vector_size)
        self.setMutationRate(mutation_rate)
        self.setSearchSpace(search_space[0], search_space[1])


    def findPseudoContent(self, fitness, associated_content):
        gene_obj = lg.population(self.population_size, self.vector_size, self.mutation_rate, self.search_space)
        gene_obj.initialize()
        gene_obj.setGeneString(associated_content)
        # print(gene_obj.getIndividual(0).getChromosome())
        gene_obj.setFitness(fitness)
        gene_obj.epoch()
        pseudo_content = []
        for i in range(self.population_size):
            # print(gene_obj.getIndividual(i).getChromosome())
            pseudo_content.append(gene_obj.getIndividual(i).getChromosome())
        return pseudo_content
