
def dburi(dbinfo):
    engine=dbinfo.get('ENGINE') or 'sqlite'
    driver=dbinfo.get('DRIVER') or 'sqlite'
    user=dbinfo.get('USER') or ''
    password=dbinfo.get('PASSWORD') or ''
    host=dbinfo.get('HOST') or ''
    port=dbinfo.get('PORT') or ''
    name=dbinfo.get('NAME') or ''

    return "{}+{}://{}:{}@{}:{}/{}".format(engine,driver,user,password,host,port,name)

class Config:
    DEBUG = False
    TESTING = False

    # 禁用重定向debug
    DEBUG_TB_INTERCEPT_REDIRECTS=False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY='ZXsdjhaskljdhaklhaiugfpoiua15564.;.;jdfhklskfklkjdlfkd-=-=;;.[[[J'

    SESSION_TYPE='redis'

    #邮件配置

    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    # MAIL_USE_TLS=False
    # MAIL_USE_SSL=True
    MAIL_USERNAME = '13931909312@163.com'
    MAIL_PASSWORD = 'MBHUIJHYBQEMLQMN'




#一个环境 多个环境同理
class DevelopConfig(Config):
    DEBUG = True
    dbinfo={
        'ENGINE':'mysql',
        'DRIVER':'pymysql',
        'USER':'SuperJie',
        'PASSWORD':'Zxj6593955.0',
        'HOST':'localhost',
        'PORT':'3306',
        'NAME':'Flask_restful',
    }
    SQLALCHEMY_DATABASE_URI=dburi(dbinfo)




envs={
    'development':DevelopConfig,
}