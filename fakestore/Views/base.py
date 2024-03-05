from rest_framework.views import APIView

import requests


class base(APIView):
    base_url = "https://fakestoreapi.com"

    def get_base_url(self):
        return self.base_url

    def send_request(self, endpoint, method="GET", params=None, data=None):
        url = f"{self.get_base_url()}/{endpoint}"

        if method == "GET":

            response = requests.get(url)  # Use requests.get without params
        elif method == "POST":
            response = requests.post(url, data)
        elif method == "PUT":
            response = requests.put(url, data)
        elif method == "PATCH":
            response = requests.patch(url, data)
        elif method == "DELETE":
            response = requests.delete(url)
        else:
            raise ValueError("Invalid Method")
        response.raise_for_status()
        return response.json()

# def get(self, request):
#     limit = request.query_params.get('limit')
#     sort = request.query_params.get('sort')
#
#     # Check if parameters are present
#     if limit or sort:
#         # If parameters are present, make the request using requests.get directly
#         params = {'limit': limit, 'sort': sort}
#         try:
#             data = self.send_request(self.endpoint, params=params)
#             return Response(data)
#         except requests.exceptions.RequestException as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         # If parameters are absent, proceed with the existing logic
#         try:
#             data = self.send_request(self.endpoint)
#             return Response(data)
#         except requests.exceptions.RequestException as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


# if params:
#     response = requests.get(url, params=params)  # Use requests.get with params
# else:

# if params:
#     url += "?" + "&".join([f"{key}={value}" for key, value in params.items()])
