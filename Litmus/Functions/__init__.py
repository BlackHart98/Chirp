import math
import numpy as np
# =========================================================================== #
# This class of distance function is for computing distance between two       #
# vectors with equal length                                                   #
# =========================================================================== #
def euclidDistance(vector_1, vector_2):
    result = 0.0
    nn = len(vector_1)
    for i in range(nn):
        result += (vector_1[i] - vector_2[i])**2
    return math.sqrt(result)


def manhattanDistance(vector_1, vector_2):
    result = 0.0
    nn = len(vector_1)
    for i in range(nn):
        result += (vector_1[i] - vector_2[i])
    return math.sqrt(result)


def cosineSimilarity(vector_1, vector_2):
    dotproduct = norm_1 = norm_2 = 0.0
    nn =  len(vector_1)
    for i in range(nn):
        dotproduct += vector_1[i]*vector_2[i]
        norm_1 += vector_1[i]
        norm_2 += vector_2[i]
    dotproduct = math.sqrt(dotproduct)
    norm_1 = math.sqrt(norm_1)
    norm_2 = math.sqrt(norm_2)
    return dotproduct/(norm_1*norm_2)





def vectorDistanceLambda(func_name, vector_1, vector_2):
    if func_name == "euclidDistance":
        return euclidDistance(vector_1,vector_2)
    elif func_name == "manhattanDistance":
        return manhattanDistance(vector_1,vector_2)
    elif func_name == "cosineSimilarity":
        return cosineSimilarity(vector_1,vector_2)
    else:
        return 0.0
