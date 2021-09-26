# this function is correct but can be improved on #
from Litmus.Genetics import LitmusGenetics
import Litmus.Functions as lf
import numpy as np


class LitmusCore:
 # ======================================================================================== #
 # Litmus class contains the following members:                                             #
 # vector size (the size of the vector )                                                    #
 # the current user taste vector u, the list of content associated to the users taste v[i]  #
 # the set of vectors C that represents the all the contents                                #
 # ======================================================================================== #
     number_of_content = 0
     vector_size = 0
     user_taste_vector = []
     pseudo_content = []
     associated_content = []
     all_content = []
     fitness = []
     litmus_genetics_obj = LitmusGenetics()
# ========================================================================================= #
# listmus methods includes the following:                                                   #
# an initialization function                                                                #
# a similarity function that finds contents that are similar to user taste function         #
# a taste generation function to generate the user taste                                    #
# ========================================================================================= #
     def initialize(self, mutation_rate):
        temp = []
        for i in range(self.vector_size):
            total = 0.0
            for j in range(self.number_of_content):
                total += self.associated_content[j][i]
            total /= self.number_of_content
            temp.append(total)
        self.user_taste_vector = temp
        self.litmus_genetics_obj.initialize(
        self.vector_size, self.number_of_content, mutation_rate, (0, 1))


     # def findContentBasedOnTaste(self):
     #    content_closeness_map = []
     #    for i in range(len(self.all_content)):
     #        closeness = euclidDistance(self.user_taste_vector, self.all_content[i])
     #        content_closeness_map.append((closeness, i))
     #    sorted_map = sorted(content_closeness_map)
     #    temp = []
     #    for i in range(self.number_of_content):
     #        temp.append(self.all_content[sorted_map[i][1]])
     #    self.associated_content = temp

     def findContentBasedOnTaste(self, related_content_size):
        content_closeness_map = []
        for i in range(len(self.all_content)):
            user_taste_vector = np.array(self.user_taste_vector,float)
            data = np.array(self.all_content[i][1],float)
            closeness = lf.euclidDistance(user_taste_vector,data)
            content_closeness_map.append((closeness, i))
        sorted_map = sorted(content_closeness_map)
        temp = []
        temp_dict = {}
        # print(sorted_map)
        for i in range(related_content_size):
            temp.append(self.all_content[sorted_map[i][1]])

        # for key in content_closeness_map:
        #     temp_dict[key] = key
        self.associated_content = temp

    # def findContentBasedOnTaste(self,number_of_content):
    #     content_closeness_map = []
    #     for i in range(len(self.all_content)):
    #         closeness = lf.euclidDistance(self.user_taste_vector,self.all_content[i][1])
    #         content_closeness_map.append((closeness, i))
    #     if number_of_content > self.number_of_content :
    #         print("Error")
    #     else:
    #         for i in range(number_of_content):
    #             temp.append(self.all_content[sorted_map[i][1]])
    #         self.associated_content = temp


     def generateUserTaste(self):
        self.generatePsuedoContent()
        # print(self.pseudo_content)
        temp = []
        for i in range(self.vector_size):
            total = 0.0
            for j in range(self.number_of_content):
                total += self.pseudo_content[j][i]
            total /= self.number_of_content
            temp.append(total)
        self.user_taste_vector = temp


     def generatePsuedoContent(self):
        self.pseudo_content = self.litmus_genetics_obj.findPseudoContent(self.fitness, self.associated_content)


# ========================================================================================== #
# litmus constructors, destructors, getters and setters                                      #
# ========================================================================================== #
     def __init__(self):
         pass

     def __del__(self):

         pass

     def getVectorSize(self):
         return self.vector_size

     def getNumberOfContent(self):
         return self.number_of_content

     def getUserTaste(self):
         return self.user_taste_vector

     def getAssociatedVector(self):
         return self.associated_content


     def getAllVector(self):
         return self.all_content


     def getInterestScore(self):
         return self.fitness

     def setVectorSize(self, vector_size):
         self.vector_size = vector_size

     def setNumberOfContent(self, number_of_content):
         self.number_of_content = number_of_content

     def setUserTaste(self, user_taste_vector):
         self.user_taste_vector = user_taste_vector

     def setCurrentDataVector(self, associated_content):
         self.associated_content = associated_content

     def setAllVector(self, all_content):
         self.all_content = all_content

     def setInterestScore(self, fitness):
         self.fitness = fitness
