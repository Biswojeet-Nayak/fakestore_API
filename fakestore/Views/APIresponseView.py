from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests


class APIResponseView(APIView):
    def handle_request_exception(self, e, func_name):
        x = func_name.split("_")[-1].lower()
        error_message = f"Failed to retrieve the {x} data: {str(e)}"
        return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

    def handle_internal_server_error(self, e):
        error_message = f"Internal server error: {str(e)}"
        return Response({"error": error_message}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def api_response(self, func, *args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if isinstance(result, Response):
                return result
            return Response(result, status=status.HTTP_200_OK)
        except requests.exceptions.RequestException as e:
            return self.handle_request_exception(e, self.__class__.__name__)
        except Exception as e:
            return self.handle_internal_server_error(e)

