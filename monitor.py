# -*- coding: utf-8 -*-

import Eingabe
import requests
import sys
import re



suche=Eingabe.Station

filter = Eingabe.Verkehrsmittel

xml = """<?xml version=\"1.0\" encoding=\"utf-8\" ?>\r\n<ReqC ver=\"1.1\" prod=\"String\" lang=\"DE\">\r\n<LocValReq id=\"001\" maxNr=\"10\" sMode=\"1\">\r\n<ReqLoc type=\"ALLTYPE\" match=\""""+suche+"""\" />\r\n</LocValReq>\r\n</ReqC>"""




 





headers = {'Content-Type': 'application/xml'} # set what your server accepts
statResponse= requests.post('https://reiseauskunft.bahn.de/bin/query.exe/dol', data=xml, headers=headers).text
townPos= statResponse.find('Station name')
townPosE= statResponse.find('"',townPos+15)
town=statResponse[townPos+14:townPosE]
print ('\n\nBahnhof: '+town+'\n\n')
StatNbrPos= statResponse.find('ionNr="')
StatNbrPosE= statResponse.find('"',StatNbrPos+9)
station=statResponse[StatNbrPos+7:StatNbrPosE]


txt = "The rain in Spain"

def XmlFind(response,search,term,pos):
    posA=response.find(search,pos)+len(search)+2
    posE=response.find(term,posA)
    strgneu=''
    strgneu=response[posA:posE]
    return strgneu


		
respondb = requests.get('https://reiseauskunft.bahn.de/bin/stboard.exe/dn?start=yes&L=vs_java3&productsFilter='+filter+'&input='+station+'&boardType=dep').text

responsb = respondb.replace("&#x0028;","(")
response = responsb.replace("&#x0029;",")")

posneu =0
pos=0
posDel=0
posDelE=0
while pos != -1:
	
	pos= response.find('<Journey',posneu+2)
	posE=response.find('</Jour',posneu+20)
	strgneu=response[posneu:posE]
	time=XmlFind(response,'fpTime','"',posneu)
	edel=XmlFind(response,'e_delay','"',posneu)
	delay=XmlFind(response,'delay','"',posneu)
	posDir= strgneu.find('prod=')
	posDirE =strgneu.find('"',posDir+7)
	dir= strgneu[posDir+6:posDirE]
	if 'dir=' in strgneu:

		posName= strgneu.find('dir=')
		posNameE =strgneu.find('"',posName+7)
		Name= strgneu[posName+5:posNameE]
	else:
		
		posName= strgneu.find('targetLoc=')
		posNameE =strgneu.find('"',posName+12)
		Name= strgneu[posName+11:posNameE]
	
	name = dir[:dir.find('#')]
	if 'platform' in strgneu:
		posGleis= strgneu.find('platform=')
		posGleisE =strgneu.find('"',posGleis+10)
		gleis= 'Gleis '+strgneu[posGleis+10:posGleisE]
	else:
		gleis = ''
	
	x = re.search('\d', Name[:7])
	if (x):
		cut=Name.find(' ')
		Name=Name[cut+1:]
	Name=Name[:30]
	Name=Name.ljust(30)
	if edel != ' fpTime=':
		dep = edel
	else:
		dep = '--'
		
	if delay=='0':
		print('in '+"{:<3}".format(dep)+'min  '+time+'  '+u'\u00b1 0     '+'     '+name+'   '+Name+ '   '+gleis)
	else:
		print('in '+"{:<3}".format(dep)+'min  '+time+'  '+"{:<8}".format(delay)+'     '+name+'   '+Name+ '   '+gleis)
	
	

	
	posneu = pos
	 
	
	
	

	
	print ('\n_______________________________________________________________________________________\n')
	
''' " fpDate="13.02.20" delay="0" e_delay="0" targetLoc="Tivoli, Karlsruhe" dirnr="722029" prod="STR    4#STR" dir="4 Tivoli ber Hbf" administration="kvvSTR" is_reachable="0" delayReason=" " approxDelay="0"></Journey> '''
