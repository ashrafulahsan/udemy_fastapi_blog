from fastapi import Depends
from backend.db.models.user import User

def require_roles(*roles: str):
    from backend.apis.v1.route_login import get_current_user
    
    def role_checker(user: User = Depends(get_current_user)):
        if user.role not in roles:
            raise PermissionError("You do not have permission to access this resource.")
        return user
    return role_checker