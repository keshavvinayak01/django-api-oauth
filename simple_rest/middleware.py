class BaseTestMiddleware : 
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		print('Start', self.middleware_name)
		response = self.get_response(request)
		print('End', self.middleware_name)

class Testmiddleware1(BaseTestMiddleware):
	middleware_name = 'First'

class Testmiddleware2(BaseTestMiddleware):
	middleware_name = 'Second'

class Testmiddleware3(BaseTestMiddleware):
	middleware_name = 'Third'
	