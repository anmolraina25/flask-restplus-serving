import io
import json

from flask import request
from flask import Response
from flask import send_file
from flask_restplus import Resource
from api.restplus import api
from api.gan.logic.tf_serving_client import make_prediction
from werkzeug.datastructures import FileStorage
from PIL import Image

# create dedicated namespace for GAN client
ns = api.namespace('ObjDet_client', description='Operations for ObjDet client')

# Flask-RestPlus specific parser for image uploading
UPLOAD_KEY = 'image'
UPLOAD_LOCATION = 'files'
upload_parser = api.parser()
upload_parser.add_argument(UPLOAD_KEY,
                           location=UPLOAD_LOCATION,
                           type=FileStorage,
                           required=True)


@ns.route('/detection')
class GanPrediction(Resource):
    @ns.doc(description='Detect bug on the image using ObjDet model. ' +
            'Return detection boxes,scores,classes',
            responses={
                200: "Success",
                400: "Bad request",
                500: "Internal server error"
                })
    @ns.expect(upload_parser)
    def post(self):
        try:
            image_file = request.files[UPLOAD_KEY]
            image = Image.open(io.BytesIO(image_file.read()))
        except Exception as inst:
            return {'message': 'something wrong with incoming request. ' +
                               'Original message: {}'.format(inst)}, 400

        try:
            result = make_prediction(image)
            #return {'prediction_result': result}, 200
            r=Response(response=json.dumps(str(result)),mimetype='application/json',status=200)
            r.headers["Content-Type"]="application/json; charset=utf-8"
            return r

        except Exception as inst:
            return {'message': 'internal error: {}'.format(inst)}, 500
