from flask import Flask, request, jsonify
import json
import Litmus as lt
import utils
import os
import markdown

app = Flask(__name__)

# TIMEOUT = 1800

recommender_system = lt.Litmus()

# @app.route('/', methods = ["GET"])
# def index():
#     with open('README.md','r') as readme:
#         content = readme.read()
#         return markdown.markdown(content)


# @app.route('/recommend', methods = ["GET"])
# def recommendation():
#     data = request.get_json()
#     try:
#         new_data = utils.normalizeJson(data)
#         result = recommender_system.recommendContent(
#         new_data["current_data"], new_data["data_pool"],
#         new_data["interest_score"], new_data["number_of_recommendations"],
#         0.0
#         )
#         if result["status"] == "failed":
#             return jsonify(
#             {"data" : [],
#             "message" : "System failed, please use /recommend_debug to see the error",
#             "status" : "failed"
#             }
#             )
#         return jsonify(
#         {"data" : result["new content"],
#         "message" : "",
#         "status" : result["status"]}
#         )
#     except:
#         return jsonify(
#         {
#         "data" : [],
#         "message" : "System failed, please use /recommend_debug to see the error",
#         "status" : "failed"
#         }
#         )

@app.route('/',methods = ["POST"])
def recommendationDebug():
    data = request.get_json()
    parse = utils.chirpJsonParser(data)
    if parse[0]:
        new_data = utils.normalizeJson(data)
        # print(new_data)
        result = recommender_system.recommendContent(
        new_data["current_data"], new_data["data_pool"],
        new_data["interest_score"], new_data["number_of_recommendations"],
        0.0
        )
        if result["status"] == "failed":
            return jsonify(
            {"data" : [],
            "message" : result["error"],
            "status" : result["status"]
            }
            )
        return jsonify(
        {"data" : result["new content"],
        "message" : "",
        "status" : result["status"]}
        )
    else:
        return jsonify({"data" : [], "message" : parse[1], "status" : "Failed"})

if __name__ == "__main__":
    app.run(debug = True)
