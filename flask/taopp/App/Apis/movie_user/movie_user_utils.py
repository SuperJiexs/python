from App.model.movie_user.MovieUser import MovieUser


def get_users(user_ident):

    if not user_ident:
        return None

    # id
    user=MovieUser.query.get(user_ident)

    if user:
        return user
    # phone
    user=MovieUser.query.filter(MovieUser.phone == user_ident).first()
    if user:
        return user
    # username
    user=MovieUser.query.filter(MovieUser.username == user_ident).first()
    if user:
        return user
    return None

