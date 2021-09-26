def chirpJsonParser(data):
    if "current_data" not in data:
        return False,f"{error['E0001']}, missing current_data"
    if "interest_score" not in data:
        return False, f"{error['E0001']}, missing interest_score"
    if "data_pool" not in data:
        return False, f"{error['E0001']}, missing data_pool"
    if "number_of_recommendations" not in data:
        return False, f"{error['E0001']}, missing number_of_recommendations"
    if len(data) > 4:
        return False, f"{error['E0001']}, surplus data provided"
    if len(data["current_data"]) == 0:
        return False, f"{error['E0002']}, check current_data"
    if len(data["interest_score"]) == 0:
        return False, f"{error['E0002']}, check interest_score"
    if len(data["data_pool"]) == 0:
        return False, f"{error['E0002']}, check data_pool"
    temp = dataParser(data)
    if not temp[0]:
        return temp
    return True, "success"


def dataParser(data):
    if type(data["current_data"]) != list:
        return False, f"{error['E0003']}, verify that current_data is a list"
    if type(data["interest_score"]) != list:
        return False, f"{error['E0003']}, verify that interest_score is a list"
    if type(data["number_of_recommendations"]) != int:
        return False, f"{erro['E0003']}, verify that number_of_recommendations is of type integer"
    if type(data["data_pool"]) != list:
        return False, f"{error['E0003']}, verify that data_pool is a list"
    if len(data["current_data"]) != len(data["interest_score"]):
        return False, f"{error['E0004']}"
    temp_type = 0
    id_list = set()
    for element in data["current_data"]:
        if temp_type == 0:
            if type(element["id"]) == int:
                temp_type = int
                # print(temp_type)
                id_list.add(element["id"])
            elif type(element["id"]) == str:
                temp_type = str
                id_list.add(element["id"])
            else:
                return False, f"{error['E0003']}, id must either be of string or integer type"
        elif temp_type != type(element["id"]):
            return False,f"{error['E0003']}, id can either only strings or only integers"
        else:
            id_list.add(element["id"])
        if type(element["tags"]) != list:
            return False, f"{error['E0003']}, tags must be a list"
        for tag in element["tags"]:
            if type(tag) != str:
                return False, f"{error['E0003']}, item in the list of tags must be of string type"

    for element in data["interest_score"]:
        if type(element["id"]) != int and (type(element["id"]) != str):
            return False, f"{error['E0003']}, id must either be of string or integer type"
        if element["id"] not in id_list:
            return False, f"{error['E0005']}"
        elif type(element["score"]) == float:
            return False, f"{error['E0003']}, score must be a float"

    temp_type = 0
    for element in data["data_pool"]:
        if temp_type == 0:
            if type(element["id"]) == int:
                temp_type = int
            elif type(element["id"]) == str:
                temp_type = str
            else:
                return False, f"{error['E0003']}, id must either be of string or integer type"
        elif temp_type != type(element["id"]):
            return False,f"{error['E0003']}, id can either only strings or only integers"
        if type(element["tags"]) != list:
            return False, f"{error['E0003']}, tags must be a list"
        for tag in element["tags"]:
            if type(tag) != str:
                return False, f"{error['E0003']}, item in the list of tags must be of string type"
    return True, "success"


error = ({
"E0001" : "Error: Invalid json data format please crosscheck(verify) the json data",
"E0002" : "Error: Data field list is empty",
"E0003" : "Error: Type mismatch",
"E0004" : "Error: interest_score and current_data list size must be equal",
"E0005" : "Error: id in interest_score must exist in id of current_data"
})



def normalizeJson(data):
    temp = []
    for element in data["current_data"]:
         temp.append((element["id"],element["tags"]))
    data["current_data"] = temp

    temp = []
    for element in data["data_pool"]:
        temp.append((element["id"], element["tags"]))
    data["data_pool"] = temp

    temp = []
    for element in data["interest_score"]:
        temp.append((element["id"], element["score"]))
    data["interest_score"] = temp
    return data
