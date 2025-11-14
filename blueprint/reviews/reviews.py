from flask import Blueprint,jsonify,request,make_response
from bson import ObjectId
import uuid

import globals
businesses = globals.db.biz

reviews_bp = Blueprint('reviews_bp',__name__)


@reviews_bp.route('/businesses/<string:biz_id>/reviews' ,methods=['POST'])
def postReview(biz_id):
    data = request.form


    if not data.get('username') or not data.get('comments') or not data.get('star'):
        return make_response(jsonify({"Error":"Missing required field"}),400)
    
    try:
        stars= int(data.get('star'))
        if stars < 1 or stars > 5:
            return make_response(jsonify({"Error":"Invalid star rating should be between 1 and 5"}),400)
    except ValueError:
            return make_response(jsonify({"error":"stars should be a number"}),400)
    business = businesses.find_one({"_id":ObjectId(biz_id)})
    if not business:
        return make_response(jsonify({"Error":"Business not found"}),404)
    
    new_review_id = str(uuid.uuid4())
    new_review={
        "_id":ObjectId(),
        "username":data.get('username'),
        "comments":data.get('comments'),
        "star":stars
    }
    businesses.update_one(
        {"_id":ObjectId(biz_id)},
        {"$push":{"reviews":new_review}}
    )

    new_review_link=f"http://127.0.0.1:5001/businesses/{new_review_id}"
    return make_response(jsonify({"URL":new_review_link}),200)
