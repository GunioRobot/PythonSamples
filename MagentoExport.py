from magento import Customer
from magento.api import API

from lxml import etree
from lxml.builder import E

from Config import *

with API(url, apiuser,apipass) as api:
    orders = api.call('sales_order.list',[])
    xml = E.orders(
        *[E.order(*[getattr(E,name)(value) for name,value in order.items() if value]) for order in orders]
    )
    file('out.xml','w').write(etree.tostring(xml, encoding='iso-8859-1', pretty_print=True))
