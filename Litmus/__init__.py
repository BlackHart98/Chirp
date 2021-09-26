# ============================================================================ #
# Litmus is a python class for generating user specific content based off      #
# user taste                                                                   #
# ============================================================================ #
from Litmus.Vectorizer import LitmusVectorizer
from Litmus.Core import LitmusCore
from Litmus.Utils import error, warning


class Litmus:
    litmus_vectorizer_obj = LitmusVectorizer()
    litmus_core_obj = LitmusCore()
    all_data_vector = []
    data = {}
    data_pool_index = {}
    current_data_index = {}
    system_status = {}

    def getIndices(self):
        print("data_pool_index : {}\ncurrent_data_index : {}\n"
        .format(self.data_pool_index,
        self.current_data_index))
# =========================================================================== #
# vectorize data : create a set of tags which are used to generate a set of   #
# vectors for associated data                                                 #
# =========================================================================== #
    def preprocessData(self):
        self.litmus_vectorizer_obj.createTagSet()
        self.litmus_vectorizer_obj.vectorizeCurrentData()
        self.litmus_vectorizer_obj.vectorizeDataPool()


# =========================================================================== #
# Generate user taste vector                                                  #
# =========================================================================== #
    def generateUserTaste(self,mutation_rate):
        number_of_content = self.litmus_vectorizer_obj.getNumberOfContent()
        vector_size = self.litmus_vectorizer_obj.getVectorSize()
        associated_vector = (self.getPreprocessedData()
        ["vectorized current data"])
        interest_score_list = self.litmus_vectorizer_obj.getInterestScore()
        self.litmus_core_obj.setNumberOfContent(number_of_content)
        self.litmus_core_obj.setVectorSize(vector_size)
        self.litmus_core_obj.setCurrentDataVector(associated_vector)
        self.litmus_core_obj.setInterestScore(interest_score_list)
        self.litmus_core_obj.initialize(mutation_rate)
        self.litmus_core_obj.generateUserTaste()


# =========================================================================== #
# Generate content with user taste                                            #
# =========================================================================== #
    def generateUserContent(self,related_content_size):
        all_vector =  self.litmus_vectorizer_obj.getVectorizedDataPool()
        self.litmus_core_obj.setAllVector(all_vector)
        self.litmus_core_obj.findContentBasedOnTaste(related_content_size)


    def setData(self, current_data, data_pool, interest_score_list):
        temp_current_data = []
        temp_interest_score_list = []
        temp_data_pool = []
        for i in range(len(current_data)):
            self.current_data_index[i] = current_data[i][0]
            temp_current_data.append(current_data[i][1])

        for i in range(len(interest_score_list)):
            # self.data_pool_index[i] = interest_score_list[i][0]
            temp_interest_score_list.append(
            interest_score_list[i][1]
            )

        for i in range(len(data_pool)):
            self.data_pool_index[i] = data_pool[i][0]
            temp_data_pool.append(data_pool[i][1])

        self.litmus_vectorizer_obj.setCurrentData(temp_current_data)
        self.litmus_vectorizer_obj.setInterestScore(
        temp_interest_score_list)
        self.litmus_vectorizer_obj.setDataPool(temp_data_pool)
        self.data = (
        {"current data" : self.litmus_vectorizer_obj.getCurrentData(),
        "data pool" : self.litmus_vectorizer_obj.getDataPool(),
        "interest score list" : self.litmus_vectorizer_obj.getInterestScore()}
        )


    def getData(self):
        return self.data


    def getPreprocessedData(self):
        return ({"tag set" : self.litmus_vectorizer_obj.getTagSet(),
        "vectorized current data" : self.litmus_vectorizer_obj.getVectorizedCurrentData(),
        "vectorized data pool" : self.litmus_vectorizer_obj.getVectorizedDataPool()}
        )


    def getUserTaste(self):
        return  ({"user taste" : self.litmus_core_obj.getUserTaste()})


    def getAssociatedVector(self):
        return ({"related data" : self.litmus_core_obj.getAssociatedVector()})


    def getNewContent(self):
        result = []
        associated_vector = self.litmus_core_obj.getAssociatedVector()
        for item in associated_vector:
            result.append(self.data_pool_index[item[0]])
        return ({"new content" : result})


    def recommendContent(self,current_data,
    data_pool,interest_score_list,related_content_size,mutation_rate):
        if related_content_size > len(data_pool):
            self.system_status = {"status" : "failed","error" : error["E0001"]}
            return self.system_status
        self.system_status = {"status" : "success"}
        self.setData(current_data,data_pool,interest_score_list)
        self.preprocessData()
        # print(self.getPreprocessedData())
        self.generateUserTaste(mutation_rate)
        self.generateUserContent(related_content_size)
        return {"status" : "success" ,
        "new content" : self.getNewContent()["new content"]
        # "tag set" : self.getPreprocessedData()["tag set"],
        # "user taste" : self.getUserTaste()["user taste"]
        }

    def summary(self):
        if self.system_status["status"] == "failed":
            print(system_status[error])
        else:
            result = self.getNewContent()["new content"]
            if len(result) > 0:
                print("=====================================================")
                print("+          User Related Content                     +")
                print("-----------------------------------------------------")
                print("+    S/N                 +           ID             +")
                print("-----------------------------------------------------")
                for i in range(len(result)):
                    print(f"*   {i+1}                           {result[i]}")
                print("=====================================================")
