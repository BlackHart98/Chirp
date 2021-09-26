# litmus vectorizer takes in list of words and generate vectors

class LitmusVectorizer:
    tag_set = set()
    current_data = []
    data_pool = []
    data_pool_vector = []
    current_data_vector = []
    fitness = []


    def createTagSet(self):
        # collapse data into a linear array
        collapsed_data = []
        for item in self.current_data[0]:
            collapsed_data.append(item)

        for i in range(1,len(self.current_data)):
            for item in self.current_data[i]:
                collapsed_data.append(item)

        for i in range(len(collapsed_data)):
            self.tag_set.add(collapsed_data[i])


    def vectorizeCurrentData(self):
        # vectorize tags for associated tag set
        current_data_vector = []
        for i in range(len(self.current_data)):
            temp = []
            for tag in self.tag_set:
                if tag in self.current_data[i]:
                    temp.append(1)
                else:
                    temp.append(0)
            current_data_vector.append(temp)
        self.current_data_vector = current_data_vector


    def vectorizeDataPool(self):
        # vectorize tags  for all tag set
        data_pool_vector = []
        for i in range(len(self.data_pool)):
            temp = []
            for tag in self.tag_set:
                if tag in self.data_pool[i]:
                    temp.append(1)
                else:
                    temp.append(0)
            data_pool_vector.append((i,temp))
        self.data_pool_vector = data_pool_vector


    def setInterestScore(self, interest_score_list):
        self.interest_score_list = interest_score_list


    def setCurrentData(self, current_data):
        self.current_data = current_data


    def setDataPool(self, data_pool):
        self.data_pool = data_pool


    def getCurrentData(self):
        return self.current_data


    def getDataPool(self):
        return self.data_pool


    def getInterestScore(self):
        return self.interest_score_list


    def getTagSet(self):
        return self.tag_set


    def getVectorizedCurrentData(self):
        return self.current_data_vector


    def getVectorizedDataPool(self):
        return self.data_pool_vector


    def getVectorSize(self):
        return len(self.tag_set)


    def getNumberOfContent(self):
        return len(self.current_data)
