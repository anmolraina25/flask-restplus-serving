# flask-restplus-serving

1. You need a docker image with tensorflow serving build in it.
    -refer create tf serving environment in:
    -https://medium.freecodecamp.org/how-to-deploy-an-object-detection-model-with-tensorflow-serving-d6436e65d1d9

2. settings.py file has values for different constants.

3. api/gan/endpoint/client.py is the flask restful client.

4. api/gan/logic/tfservingclient.py handles image from client.py, passes it to tf serving server via grpc and protobuf and sends result to client.py

5. client.py jsonifies tensor and displays on swagger UI.

6. app.py is the flask server and includes the various params for our flask-restful app.

7. build the image of this repo using Dockerfile provuded.

8 use docker compose to create and initialize containers for both images. It runs the multi image container.

This article for further explanation: https://becominghuman.ai/creating-restful-api-to-tensorflow-models-c5c57b692c10

IMP: Change flask server in settings.py and docker-compose.yaml to "0.0.0.0"...I changed it to "192.168..." just to check wether it would work on my local network. 

