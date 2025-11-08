from flask import Flask,jsonify,request,make_response
from bson import ObjectId

import globals
bsuinesses = globals.db.biz

business_bp = Blueprint('business_bp',__name__)

@business_bp.route('/business' ,methods=['GET'])
@jwt_required
def showBusinesses():
    return jsonify({"message":"Welcome to Coffe mart"})

@business_bp.route('/businesses' ,methods=['GET'])
def getAllBusiness():
    data_to_return = []
    page_num = request.args.get('page',default=1,type=int)
    page_size = request.args.get('size',default=10,type=int)
    page_start = (page_num-1)*page_size

    try:
        businesses_cursor = businesses.find().skip(page_start).limit(page_size)
        for business in businesses_cursor:
            business['_id'] = str(business['_id'])
            data_to_return.append(business) 
        
        return make_response(jsonify(data_to_return),200)
    except ConnectionError:
        return make_response(jsonify({"error":"No MongoDB connection"}),500)
    except Exception as e:
        return make_response(jsonify({"error":"no mongodb connection","details":str(e)}),500)

@business_bp.route('/businesses/<string:biz_id>' ,methods=['GET'])
def getOneBusiness(biz_id):
    biz = businesses.find_one({"_id":ObjectId(biz_id)})
    if biz is not None:
        biz["_id"] = str(biz["_id"])
        for review in biz['reviews']:
            review['_id'] = str(biz['_id'])
        return make_response(jsonify(biz),200)
    else:
        return make_response(jsonify({"Error":"Not found"}), 404)
    

@business_bp.route('/businesses' ,methods=['POST'])
def addBusiness():
    data = request.form

    if data and 'name' in data and 'town' and 'rating' in data:
        new_business = {
            "name":data.get("name"),
            "town":data.get("town"),
            "rating":data.get("rating",0),
            "reviews":[]
        }
        results = businesses.insert_one(new_business)
        new_business_id = str(results.inserted_id)
        new_business_link = f"http://127.0.0.1:5001/businesses/{new_business_id}"
        return make_response(jsonify({"URL":new_business_link}),200)
    else:
        return make_response(jsonify({"Error":"Missing Data"}),400)

         


@business_bp.route('/businesses/<string:biz_id>' ,methods=['PUT'])
def updateBusiness(biz_id):
    data = request.form
    update_field = {}
    if data.get('name'):
        update_field['name'] = data.get('name')
    if data.get('town'):
        update_field['town'] = data.get('town')
    if data.get('rating'):
        update_field['rating'] = data.get('rating')

    if not update_field:
        return make_response(jsonify({"Error":"no valid data passed"}),400)
    
    results = businesses.update_one(
        {"_id":ObjectId(biz_id)},
        {"$set":update_field}
        )
    if results.modified_count == 1:
        updated_Business_link = f"http://127.0.0.1:5001/businesses/{biz_id}"
        return make_response(jsonify({"URL":updated_Business_link}),200)
    else:
        return make_response(jsonify({"message":"No changes made"}), 404)

    
    
#delete
@business_bp.route('/businesses/<string:biz_id>' ,methods=['DELETE'])
def deleteBusiness(biz_id):
    results = businesses.delete_one({"_id":ObjectId(biz_id)})
    if results.deleted_count ==1:
     return make_response(jsonify({"message":"deleted"}),200)
    else:
     return make_response(jsonify({"message":"Not found"}), 404)