# -*- coding: utf-8 -*-
"""module models"""
from sqlalchemy import Table
from fusion.mysql.database import metadata

ifcdta = Table('ifc_dta_t', metadata, autoload=True)
ifcfed = Table('ifc_fed_t', metadata, autoload=True)
wkedta = Table('wke_dta_t', metadata, autoload=True)
wkeifc = Table('wke_ifc_t', metadata, autoload=True)