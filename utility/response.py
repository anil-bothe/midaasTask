from rest_framework.response import Response


class ApiResponse(object):
    def __init__(self, message="Okay", code=200, success=True, data={}):
        if data is None:
            data = dict()
        self.message = message
        self.code = code
        self.success = success
        self.data = data

    def response_ok(self, message="Ok", code=200, success=True, data={}):
        data = {"message": message, "code": code, "success": success, "data": data}
        return Response(data=data, status=code)

    def response_bad_request(self, message="Bad Request", code=400, success=False, data={}):
        data = {"message": message, "code": code, "success": success, "data": data}
        return Response(data=data, status=code)

    def response_not_found(self, message="Not Found", code=404, success=False, data={}):
        data = {"message": message, "code": code, "success": success, "data": data}
        return Response(data=data, status=code)
