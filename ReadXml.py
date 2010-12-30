# encoding: iso-8859-1
from lxml import etree

# einlesen des xml aus datei. hier wird die datei sample.xml
# vorausgesetzt, die in CreateXml.py erzeugt wurde
input = file('sample.xml')
xml = etree.parse(input)

# elemente lassen sich am besten mit XPath greifen. XPath ist
# eine SEHR m�chtige sprache. hier die einfache "suche" nach
# allen knoten die "child" hei�en:
for child in xml.xpath('//child'):
    print child.text

# als kleines Beispiel: selektiere alle knoten, die "child"
# hei�en und als text "3" haben:
for child in xml.xpath("//child[text()=3]"):
    print child.text


# unsinniges etwas komplexeres beispiel: gib' mir alle knoten,
# die "child" hei�en und als text "4" haben, von dort gehe im
# baum eine ebene hoch und nimm von dem knoten das erste kind
for child in xml.xpath("//child[text()=4]/../*[1]"):
    print child.text

# generell solltet ihr fast alle "normalen" probleme l�sen k�nnen,
# wenn ihr die ausdr�cke einfach wie pfadangaben auf dem xml baum
# schreibt. falls ihr komplexere probleme habt, sagt einfach bescheid
