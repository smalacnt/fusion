"""module wke: wke data CRUD operations """
from fusion.mysql.models import wkedta, wkeifc
from fusion.mysql.database import conn
from fusion.flask.exception import InvalidUsage

def addwke(name, ifcs):
    print(ifcs)
    """add wke, overwrite if existed """
    msg = dict()
    if not name or not ifcs:
        raise InvalidUsage('wke name or interfaces cannot be empty ')
    
    conn.execute(wkedta.delete().where(wkedta.c.wkecod == name))
    conn.execute(wkeifc.delete().where(wkeifc.c.wkecod == name))

    conn.execute(wkedta.insert(), wkecod=name)

    ifcdtas = []
    for ifc in ifcs:
        if not ifc['name'] or not ifc['direction']:
            raise InvalidUsage('interface name or dir cannot be empty ')
        ifcdtas.append({'wkecod': name, 'ifcnam': ifc['name'], 'ifcdir': ifc['direction']})
    conn.execute(wkeifc.insert(), ifcdtas)

    msg['message'] = 'success'
    return msg

def getwke(name):
    """get wke """
    result = dict()
    if not name:
        raise InvalidUsage('wke name cannot be empty ')
    
    wke = conn.execute(wkedta.select().where(wkedta.c.wkecod == name)).first()
    if not wke:
        raise InvalidUsage(('wke %s not defined' % name))

    ifcs = []
    for row in conn.execute(wkeifc.select().where(wkeifc.c.wkecod == name)):
        ifcs.append({'name': row.ifcnam, 'direction': row.ifcdir})

    result['name'] = wke.wkecod
    result['description'] = wke.wkedsc
    result['interfaces'] = ifcs
    return result
