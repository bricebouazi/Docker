#!/usr/bin/env bash
from time import sleep
import re
def main():
    """
    for a given list of staffId, add BOOKMAKER_PAY, _REFUND & VOUCHER_PAY on a top group
    """

    print("Start of scenario_delete_role()")
    sleep(1)
    print("Chaque staffId doit être séparé par un espace. Les retours chariots ne sont pas acceptés.")
    print("Merci d'indiquer la liste des staffs à modifier")
    raw_data = input("> ")
    raw_data = raw_data.replace(",", "")
    raw_data = re.sub(r'\s+', ' ', raw_data) # removing occurence of spaces
    list_of_staffid = list(raw_data.split(" ")) # turn string into list

    sleep(1)
    print("Chaque RoleId doit être séparé par un espace. Les retours chariots ne sont pas acceptés.")
    print("Merci d'indiquer la liste des Role à Suprimé")
    print("#530=BOOKMAKER_BET #520=BOOKMAKER_CANCEL # 510 =bookmaker_pay # 521 =bookmaker_refund #531=VOUCHER_CREATOR #534=VOUCHER_READER #533 =voucher_pay  ")
    raw_data2 = input("> ")
    raw_data2 = raw_data2.replace(",", "")
    raw_data2 = re.sub(r'\s+', ' ', raw_data2) # removing occurence of spaces
    list_of_roles= list(raw_data2.split(" ")) # turn string into list
    count = len(list_of_staffid)
    print(f"Il y a {count} staffs à traiter")
    sleep(1)
    for index, staffid in enumerate(list_of_staffid):
        for roleid in list_of_roles:
            print(f"#{index+1} - remove role {roleid} to staff {staffid} ")
            
    if __name__ == '__main__':
        
    main()
    
