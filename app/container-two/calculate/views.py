import csv
import os

from rest_framework.response import Response
from rest_framework.views import APIView


class CalculateView(APIView):
    def post(self, request):

        # Extract file and product from JSON data
        file_name = request.data['file']
        product = request.data['product']

        try:
            # Construct the file path based on the mounted volume
            file_path = os.path.join('../bhishman_PV_dir', file_name)

            # Read the header separately
            with open(file_path, 'r') as file:
                header = next(file).strip().split(',')
                if set(header) != {'product'.strip(), 'amount'.strip()}:
                    raise Exception(
                        f"Invalid columns in the first row of the file {file_path}. Expected: 'product' and 'amount'.")

            # Read and process the CSV file
            with open(file_path, 'r') as file:
                csv_reader = csv.DictReader(file)

                sum_value = 0

                for row in csv_reader:
                    # Check if 'amount' and 'product' fields are present and valid
                    if 'amount' not in row or 'product' not in row:
                        raise Exception(f"Missing 'amount' or 'product' field in the file {file_path}. Row: {row}")

                    if ' ' in row['product']:
                        raise Exception(
                            f"Invalid 'product' value (contains spaces) in the file {file_path}. Row: {row}")

                    if ' ' in row['amount']:
                        raise Exception(
                            f"Invalid 'amount' value (contains spaces) in the file {file_path}. Row: {row}")

                    if not row['product'] or not isinstance(row['product'], str):
                        raise Exception(f"Invalid 'product' value in the file {file_path}. Row: {row}")

                    if not row['amount'] or not row['amount'].isdigit():
                        raise Exception(f"Invalid 'amount' value in the file {file_path}. Row: {row}")

                    if len(row) != len(header):
                        raise Exception(f"Invalid number of columns in the file {file_path}. Row: {row}")

                    sum_value += int(row['amount']) if row['product'] == product else 0

            # Return the result in the appropriate JSON format
            return Response({"file": file_name, "sum": sum_value})

        except Exception as e:
            print("EXCEPTION ---------------------- ", e, flush=True)
            with open(file_path, 'r') as f2:
                data = f2.read()
                print(data, flush=True)
            return Response({"file": file_name, "error": "Input file not in CSV format."})
