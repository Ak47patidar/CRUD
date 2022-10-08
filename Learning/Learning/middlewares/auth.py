#this is code copied from django documenttation for creating own middleware

def auth_Middleware(get_response):  

    def middleware(request):       
        print("middleware is running")
        response = get_response(request)
        return response
    return middleware