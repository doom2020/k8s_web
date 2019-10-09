


class HomeViewHandle:
    def __init__(self, request):
        self.request = request

    def get_handle(self):
        post_type = self.request.POST('post_type')
        handle = None
        home_view_cool = HomeViewCool(self.request)
        if hasattr(home_view_cool, post_type):
            handle = getattr(home_view_cool, post_type)



class HomeViewCool:
    def __init__(self, request):
        self.request = request

    def get_table_data(self):
        pass



class LoginViewHandle:
    def __init__(self, request):
        self.request = request

    def get_handle(self):
        post_type = self.request.POST.get('post_type')
        handle = None
        login_view_cool = LoginViewCool(self.request)
        if hasattr(login_view_cool, post_type):
            handle = getattr(login_view_cool, post_type)

class LoginViewCool:
    def __init__(self, request):
        self.request = request



class RegisterViewHandle:
    def __init__(self, request):
        self.request = request

    def get_handle(self):
        post_type = self.request.POST.get('post_type')
        handle = None
        register_view_cool = RegisterViewCool(self.request)
        if hasattr(register_view_cool, post_type):
            handle = getattr(register_view_cool, post_type)



class RegisterViewCool:
    def __init__(self, request):
        self.request = request