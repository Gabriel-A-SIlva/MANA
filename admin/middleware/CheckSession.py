from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class CheckSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        allowed_paths = [
            '/admin/sign_in_admin',
            '/admin/logout_view',
            '/admin/static/',
        ]

        if request.path.startswith('/admin/static/'):
            return  # permitir arquivos estáticos

        if not request.session.get('user_id') and not any(request.path.startswith(p) for p in allowed_paths):
            return redirect('/admin/sign_in_admin')
