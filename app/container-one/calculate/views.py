import os

from rest_framework.response import Response
from rest_framework.views import APIView
import requests


class CalculateView(APIView):
    def post(self, request):

        # Validating if the file name provided in not null
        if request.data['file'] is None or request.data['file'] == '':
            return Response({"file": None, "error": "Invalid JSON input."})

        # Construct the file path in the shared volume
        file_path = os.path.join('../bhishman_PV_dir', request.data['file'])

        # Check if the file exists in the shared volume
        if not os.path.exists(file_path):
            return Response({"file": request.data['file'], "error": "File not found."})

        # Send data to Container 2
        response = requests.post('http://service-two:6001/calculate', json=request.data)
        # If both the validations are passed, we send the response to the second container
        return Response(response.json())
