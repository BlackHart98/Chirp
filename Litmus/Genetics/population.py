import random
import Litmus.Genetics.individual as lg


# This class is the group of chromosomes
class population:
	pop_size=0
	chrom_size=0
	mutation_rate=0.0
	chrom_set=[]
	fit_prob=[]
	pair_list=[]
	search_space=()
	# best=[]


# The constructor for this class is instantiated with population size,
# length of the genes string of each chromosome, mutation rate, search space
	def __init__(self,pop_size,chrom_size,mutation_rate,search_space):
		self.pop_size=pop_size
		self.chrom_size=chrom_size
		self.mutation_rate=mutation_rate
		self.search_space=search_space


# This method intialize all the chromosomes according to the population size
	def initialize(self):
		for i in range(self.pop_size):
			temp=lg.individual(self.chrom_size)
			temp.populate(self.search_space)
			# print("Generated chromosomes: ")
			# print(temp.getChromosome())
			self.chrom_set.append(temp)


# This method is the selection phase
	def select(self):
		add=.0
		self.pair_list=[]
		for i in range(self.pop_size):
			# print(self.chrom_set[i].getFitness())
			add+=self.chrom_set[i].getFitness()

		if add == 0:
			for i in range(self.pop_size):
				self.fit_prob.append(1/self.pop_size)
		else:
			for i in range(self.pop_size):
				self.fit_prob.append(self.chrom_set[i].getFitness()/add)

		for i in range(self.pop_size):
			r=random.random()
			j=0
			while r>0:
				r-=self.fit_prob[j]
				j+=1
			if j != 0:
				j-=1
			r=random.random()
			k=0
			while r>0:
				r-=self.fit_prob[k]
				k+=1
			if k!=0:
				k-=1
			self.pair_list.append((j,k))


# This method is the crossover phase
	def crossover(self):
		for i in range(self.pop_size):
			temp=[]
			for j in range(self.chrom_size):
				if j < self.chrom_size/2:
					temp.append(self.chrom_set[self.pair_list[i][0]].getGene(j))
				else:
					temp.append(self.chrom_set[self.pair_list[i][1]].getGene(j))

			# print(temp)
			self.chrom_set[i].updateChromosome(temp)


# This method gets individual chromosome object at the position passed as the parmeter
	def getIndividual(self,position):
		return self.chrom_set[position]


# this method set the mutation rate
	def setMutationRate(self,val):
		self.mutation_rate=val


# This method get the mutation rate
	def getMutationRate(self,val):
		return self.mutation_rate


#  This method mutates the chromosome according to the mutation rate
	def mutate(self):
		for i in range(self.pop_size):
			mutant=self.chrom_set[i].getChromosome()
			for j in range(self.chrom_size):
				r=random.random()
				if r < self.mutation_rate:
					mutant[j]=random.randint(self.search_space[0],self.search_space[1])


# This method utilizes simple max-search to find the best candidate
	def getBestCandidate(self):
		max_index=0
		for i in range(1,self.pop_size):
			# print("yepa {} : {}".format(self.chrom_set[i].getFitness(), self.chrom_set[max_index].getFitness()))
			if self.chrom_set[i].getFitness() > self.chrom_set[max_index].getFitness():
				max_index=i
		return self.chrom_set[max_index]


# This method performs selection, crossover and mutation
	def epoch(self):
		self.select()
		self.crossover()
		self.mutate()


# This method set the fitness value of all the population of chromosome
	def setFitness(self,fit_val):
		for i in range(self.pop_size):
			self.chrom_set[i].setFitness(fit_val[i])


# This method get the fitness value of all the population of chromosome
	def getFitness(self):
		fit_list=[]
		for i in range(self.pop_size):
			fit_list.append(self.chrom_set[i].getFitness())
		return fit_list

	def setGeneString(self, gene_string_list):
		for i in range(self.pop_size):
			self.chrom_set[i].updateChromosome(gene_string_list[i])
