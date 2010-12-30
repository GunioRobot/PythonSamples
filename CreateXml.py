# encoding: iso-8859-1
# die erste Zeile wird gebraucht, damit Sonderzeichen erlaubt sind
# ansonsten gäb's Fehler wegen der äöüs in den Kommentaren

from lxml import etree
from lxml.builder import E

# gibt <abc>inhalt</abc> aus.
xml = E.abc("inhalt")
print etree.tostring(xml)

# man kann die tags auch verschachteln
# gibt <abc><xyz>text</xyz></abc> aus
xml = E.abc(
    E.xyz("text")
)
print etree.tostring(xml)

# anhängen von knoten
# gibt folgendes aus:
# <root><child>0</child><child>1</child><child>2</child><child>3</child><child>4</child></root>
xml = E.root()
for i in range(5):
    xml.append( E.child(str(i)) )
print etree.tostring(xml)

# speichern in eine Datei:
out = file('sample.xml','w')
tree = etree.ElementTree(xml)
tree.write(out,encoding='utf8',pretty_print=True)

