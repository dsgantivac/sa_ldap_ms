#from ldap3 import Server, Connection, ALL



#server = Server('192.168.99.101')
#conn = Connection(server,"admin",password="admin",raise_exceptions=False)
#conn.open()
#conn.bind("dc=arqsoft,dc=unal,dc=edu,dc=co")
##print(conn)
#print("LDAP:",server)
#print("CONN:",conn)

import ldap
#pip3 install python-ldap
ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT,0)
con = ldap.initialize("ldaps://192.168.99.101:636")
con.set_option(ldap.OPT_PROTOCOL_VERSION, 3)
#
user_dn = "cn=David Gantiva,dc=arqsoft,dc=unal,dc=edu,dc=co"
user_password = "1234"
con.simple_bind_s(user_dn,user_password)


print(con)


