from App.model.admin.admin_users_models import Admin_Users


def get_users(users_ident):

    if not users_ident:
        return None
    users=Admin_Users.query.get(users_ident)
    if  users:
        return users
    users=Admin_Users.query.filter(Admin_Users.name==users_ident).first()
    if users:
        return users
    return None









