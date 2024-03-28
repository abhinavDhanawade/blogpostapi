from datetime import datetime
import json

class StandardizeApiResponseMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exclude_paths = ['/swagger/','/schema/']

    def __call__(self, request):
        if not any(request.path.startswith(path) for path in self.exclude_paths):
            response = self.get_response(request)            
            if response.status_code == 200 and 'application/json' in response.get('content-type', ''):
                response_data = json.loads(response.content)
                response.content = json.dumps({
                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),
                    "path": request.path,
                    "method": request.method,
                    "result": response_data
                })
            
            return response
        
        return self.get_response(request) 
