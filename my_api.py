from flask import Flask, jsonify, request
import os
from dotenv import load_dotenv
import pymongo
from bson.objectid import ObjectId
from bson.errors import InvalidId
from bson.json_util import dumps

load_dotenv()

app = Flask(__name__)

mongo_url = os.getenv("MONGO_URL")
client = pymongo.MongoClient(mongo_url)
db = client["student_db"]
collection = db["students"]


@app.route("/")
def home():
    return "Student API Running"


# ---------------- GET ALL ---------------- #

@app.route("/api/v1/students", methods=["GET"])
def student():
    students = list(collection.find())

    return app.response_class(
        response=dumps(students),
        mimetype="application/json"
    )


# ---------------- GET ONE ---------------- #

@app.route("/api/v1/student/<id>", methods=["GET"])
def get_student(id):

    try:
        student = collection.find_one({"_id": ObjectId(id)})
    except InvalidId:
        return jsonify({"error": "Invalid Student ID"}), 400

    if student is None:
        return jsonify({"error": "Student not found"}), 404

    return app.response_class(
        response=dumps(student),
        mimetype="application/json"
    )


# ---------------- CREATE ---------------- #

@app.route("/api/v1/student", methods=["POST"])
def create_student():

    student = {
        "name": request.form.get("name"),
        "country": request.form.get("country"),
        "city": request.form.get("city"),
        "skills": request.form.getlist("skills"),
        "bio": request.form.get("bio"),
        "birth_year": request.form.get("birth_year")
    }

    result = collection.insert_one(student)

    return jsonify({
        "message": "Student created successfully",
        "student_id": str(result.inserted_id)
    }), 201


# ---------------- UPDATE ---------------- #

@app.route("/api/v1/student/<id>", methods=["PUT"])
def update_student(id):

    try:
        query = {"_id": ObjectId(id)}
    except InvalidId:
        return jsonify({"error": "Invalid Student ID"}), 400

    student = {
        "name": request.form.get("name"),
        "country": request.form.get("country"),
        "city": request.form.get("city"),
        "skills": request.form.getlist("skills"),
        "bio": request.form.get("bio"),
        "birth_year": request.form.get("birth_year")
    }

    result = collection.update_one(query, {"$set": student})

    if result.matched_count == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student updated successfully"}), 200


# ---------------- DELETE ---------------- #

@app.route("/api/v1/student/<id>", methods=["DELETE"])
def delete_student(id):

    try:
        query = {"_id": ObjectId(id)}
    except InvalidId:
        return jsonify({"error": "Invalid Student ID"}), 400

    result = collection.delete_one(query)

    if result.deleted_count == 0:
        return jsonify({"error": "Student not found"}), 404

    return jsonify({"message": "Student deleted successfully"}), 200


if __name__ == "__main__":
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000)