from .base import Users

class _Singleton(type):
    """ A metaclass that creates a Singleton base class when called. """
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(_Singleton('SingletonMeta', (object,), {})): pass


class CurrentUser(Singleton):

    def __init__(self, login):
        self.login = login
        
        u = Users.query.filter(Users.login==login).one_or_none()
        self.full_name = 'Ананимус'
        self.lastname, self.firstname, self.middlename = 'None','None','None'
        self.role = 0
        if u:
            self.id = u.id
            self.full_name = f"{u.lastname} {u.firstname} {u.middlename}"
            self.role = u.role

    def json(self):
        return { 
            'id': self.id, 
            'full_name': self.full_name, 
            'role': self.role
            }
        # else:
        #     l = get_LDAP_entities(login)
        #     au = next(item for item in l if item["login"] == login)
        #     self.full_name = 'ananimus'
        #     self.unit = ""
        #     self.role = 0
        #     if au:
        #         self.full_name = au.get('full_name', '')
         
    
    # def get_AD_user(self):
    #     ldap = AppLdapUser(current_app.config.get('LDAP_HOST', ''), current_app.config.get('LDAP_USER', ''), current_app.config.get('LDAP_PASSWORD', ''), current_app.config.get('LDAP_SEARCH_BASE', '')) 
    #     ad_user = ldap.get_user(self.login)

    #     self.full_name = ad_user['name']
    #     if ad_user['memberof'] != None:
    #         for item in ad_user['memberof']:
    #             mixed = item.split(',')
    #             zol = list(map(lambda y: y.replace('CN=',''), list(filter(lambda x: x.find('CN=') != -1, mixed))))
    #             self.groups.append(zol[0])
    #     return ad_user