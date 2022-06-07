from threading import activeCount
from brownie import *
import logging
from dotenv import load_dotenv
import json
from os.path import exists
load_dotenv()

def main():
    acc = accounts.load('huitzil_test_zeniq')
    #acc.transfer('0xbc9735f089Ac31c76FB75b81EbD0c6DAF297DB99', 10000000000000000)
    #t = Transaction.deploy('Transacion', 'TST', 1, 200, {'from': acc})
    #t = Transaction.transferFrom('0x11E59Cf068c02f2fb22F488b3cce87FB26261455', '0xbc9735f089Ac31c76FB75b81EbD0c6DAF297DB99', 100000000000000000000)
    t = Upload.deploy('aaaaaaaa', {'from': acc } )
    #print(t.storeData)
    
    print(t.address)
    print(acc)
    
    flag = True
    while flag:
        try:
            path = './build/deployments/383414847825/{address}.json'.format(address=t.address)
            f = open(path)
            data = json.load(f)
            if data:
                flag = False
            f.close()
            #print('abi',data['abi'])
            abi = json.dumps(data['abi'])
            contractAddresses = {
                data['deployment']['chainid']: data['deployment']['address']
            }            
            #print('contract',contractAddresses)
            contractAddresses = json.dumps(contractAddresses)
            print(abi)
            print(contractAddresses)
            
        except:
            pass

    #t.payBill()