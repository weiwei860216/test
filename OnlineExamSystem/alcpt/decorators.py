from django.contrib.auth.decorators import login_required


def permission_check(required_user_type):
    def decorator(view):
        @login_required
        def check(request, *args, **kwargs):
            if not required_user_type:
                raise ValueError("Loss argument 'required_user_type'")

            if not request.user.has_perm(required_user_type):
                raise PermissionError()

            return view(request, *args, **kwargs)
        return check
    return decorator
