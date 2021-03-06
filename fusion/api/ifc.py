# -*- coding: utf-8 -*-
"""module ifcdta: interface data CRUD operations """
from fusion.mysql.models import ifcdta, ifcfed
from fusion.mysql.database import engine
from fusion.flask.exception import InvalidUsage

def addifc(name, fields):
    """add interface, overwrite if existed """
    msg = dict()
    if not name or not fields:
        raise InvalidUsage('interface name or fields cannot be empty ')

    with engine.begin() as conn:
        conn.execute(ifcfed.delete().where(ifcfed.c.ifcnam == name))
        conn.execute(ifcdta.delete().where(ifcdta.c.ifcnam == name))

        conn.execute(ifcdta.insert(), ifcnam=name)

        feds = []
        for fedseq, fednam in enumerate(fields):
            if not fednam:
                raise InvalidUsage('field name cannot be empty ')
            feds.append({'ifcnam': name, 'fedseq': fedseq, 'fednam': fednam})
        conn.execute(ifcfed.insert(), feds)

        msg['message'] = 'success'
    return msg

def getifc(name):
    """get interface """
    result = dict()
    if not name:
        raise InvalidUsage('interface name cannot be empty ')

    fields = []
    for row in engine.execute(ifcfed.select().where(ifcfed.c.ifcnam == name)):
        fields.append(row.fednam)
    
    if not fields:
        raise InvalidUsage('interface does not existed ')

    result['name'] = name
    result['fields'] = fields
    return result
