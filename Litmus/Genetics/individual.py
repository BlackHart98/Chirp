import random

# This class is the individual chromosome
class individual:
	mating_pairs={}
	chromosome=[]
	fitness=0.0
	chrom_length=0

# The constructor for this class is initialized 
# with the lehgth of the individual string of genes
	def __init__(self,chrom_length):
		self.chrom_length=chrom_length


# This method fills the chromosome with genes
	def populate(self,search_space):
		temp=[]
		for i in range(self.chrom_length):
			r=random.randint(search_space[0],search_space[1])
			temp.append(r)
		self.chromosome=temp


#  this method returns the fitness of this chromosome
	def getFitness(self):
		return self.fitness


# This method sets the fitness value for this individual chromosome
	def setFitness(self,fit_val):
		self.fitness=fit_val


# This method returns the gene at the position passed in as its parameter
	def getGene(self,position):
		return self.chromosome[position]

	# def updatGenePos(self,position,search_space):
	# 	self.chromosome[position]=random.randint(search_space[0],search_space[1])


# This method return string of genes
	def getChromosome(self):
		return self.chromosome


# This method update the string of genes with a new one
	def updateChromosome(self,chromosome):
		self.chromosome=chromosome