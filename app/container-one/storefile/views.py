import json
import os

from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class StoreFileView(APIView):
    def post(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        file_name = json_data.get('file')
        data = json_data.get('data')

        if not file_name or not data:
            return Response({"file": file_name, "error": "Invalid JSON input."}, status=400)

        # Remove spaces from the data
        data = "\n".join([line.replace(" ", "") for line in data.split("\n")])

        try:
            with open(os.path.join('../bhishman_PV_dir', file_name), 'w') as f:
                f.write(data)
            return Response({"file": file_name, "message": "Success."})
        except Exception as e:
            return Response({"file": file_name, "error": "Error while storing the file to the storage."}, status=500)
