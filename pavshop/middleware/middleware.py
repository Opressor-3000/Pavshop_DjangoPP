from django.utils.deprecation import MiddlewareMixin


class CustomeMiddleware(MiddlewareMixin):
   def process_request(self, request):
      pass

   def process_response(self, response):
      pass

