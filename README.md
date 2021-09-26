# Chirp (Readme)
## Response
All response is of the json format

```json
{
  "data": "The list of ids",
  "message": "status report details",
  "status" : "status of the system"
}
```

## Request
**GET "/"**
Returns the Readme html page

**GET "/recommend"**
Returns a valid json request for chirp is of the format listed below


```json
{
  "current_data" : "List of current data",
  "interest_score" : "List interest scores related to the current data",
  "data_pool" : "List of data to be selected for recommendation",
  "number_of_recommendations" : "Number of recommendation"
}
```

## Json Get Request Schema Description

1. **current_data** - list of current data
2. **id** - integer or string for the id of the data
3. **tags** - list of strings of document tags
4. **interest_score** - list of interest score(floating point values) for all curreht data
5. **data_pool** - list of all data to be pooled from
6. **number_of_recommendations** - integer for the amount of expected recommendation

### Sample Request
```json
{
    "current_data":[
        {
        "id" : 1,
        "tags" : ["fashion","sport"]
        },
        {
            "id" : 4,
            "tags" : ["music","fashion"]
        }
        ],
    "interest_score":[{
        "id" : 1,
        "score" : 1
    },
    {
        "id" : 4,
        "score" : 0
     }
    ],
    "data_pool":[
        {"id" : 2,
        "tags" : ["music"]
        },
        {
            "id" : 3,
            "tags" : ["sport"]
        }
    ],
    "number_of_recommendations" : 1
}
```

## Json Response Schema Description
1. **data** - list of id
2. **message** - string of the resulting message from the system
3. **status** - string the status of the system which could either be failed or success

### Sample Response
```json
{
    "data": [
        2
    ],
    "message": "",
    "status": "success"
}
```

### Another Sample Response
```json
{
    "data": [],
    "message": "Error: Type mismatch, id can either only strings or only integers",
    "status": "Failed"
}
```
