import xmlrpclib
import csv

server = "http://localhost:8069"
database = "database"
user = "admin"
pwd = "admin"

common = xmlrpclib.ServerProxy( '%s/xmlrpc/2/common' %server)

print common.version()

uid = common.authenticate(database,user,pwd, {})

print uid

OdooApi = xmlrpclib.ServerProxy('%s/xmlrpc/2/object' %server)


dietfacts_ids = OdooApi.execute_kw(
    database, uid, pwd, 'product.template', 'search',
    [[('categ_id', '=', 7)]])
report = xmlrpclib.ServerProxy('{}/xmlrpc/2/report'.format(server))
result = report.render_report(database, uid, pwd, 'product.nutrition', dietfacts_ids)
report_data = result['result'].decode('base64')

with open('report.pdf', 'w') as f:
        f.write(report_data)

 