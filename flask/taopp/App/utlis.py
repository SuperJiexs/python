import uuid


MOVIE_USER='movie_user'
MOVIE_ADMIN_USER='movie_admin_user'
ADMIN_USER='admin_user'



def gen_token(pre=None):
    token=pre+uuid.uuid4().hex
    return token

def gen_movie_user_token():
    return gen_token(pre=MOVIE_USER)

def gen_admin_user_token():
    return gen_token(pre=ADMIN_USER)


def gen_movie_admin_token():
    return gen_token(pre=MOVIE_ADMIN_USER)



