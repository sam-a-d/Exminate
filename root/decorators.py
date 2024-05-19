from django.shortcuts import redirect
from django.http import HttpResponse

def allowed_user_groups(allowed_groups=[]):

    # transform all the groupname in lowercase 
    allowed_groups = [grp.lower() for grp in allowed_groups]
    
    def grand_wrapper_func(main_func):

        def wrapper_func(request, *args, **kwargs):
            
            user = request.user

            if user.groups.exists():
                
                # Listing the groups, in lowercase, that are associated with the user
                groups_of_the_user = [u.name.lower() for u in user.groups.all()]

                # check if the groups assingned to the user matchs the permiitted user group(s)
                permission_granted = bool(set(allowed_groups) & set(groups_of_the_user))
                
                # if permission is okay allow user to visit the URL, show warning otherwise
                if permission_granted:
                    return main_func(request, *args, **kwargs)
                else:
                    return HttpResponse('Permission denied')
            
            # if the user does not have a group assigned
            else:
                return HttpResponse('You are not authorized to access this page')

            return main_func(request, *args, **kwargs)
            
        return wrapper_func

    return grand_wrapper_func