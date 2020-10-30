# Author : David Herzog

import requests
import json


### ======================= version test ===========================

res_deal_id =  '{                               \
                    "code": "J123456",          \
                    "name": "toto",             \
                    "amount": 1000.0,           \
                    "zone": "AMER",             \
                    "devise": "EURO",           \
                    "borrower": "CFA INSTA",    \
                    "lender": "BNP",            \
                    "status": "STRUCTURING"     \
                }'

res_facility_id = ''

res_insurance_id =    '[                                \
                        {                               \
                            "id_facilite": "999",       \
                            "name": "test6",            \
                            "percentage": 0.7           \
                        },                              \
                        {                               \
                            "id_facilite": "999",       \
                            "name": "test put",         \
                            "percentage": 0.12          \
                        },                              \
                        {                               \
                            "id_facilite": "999",       \
                            "name": "test put2",        \
                            "percentage": 0.99          \
                        }                               \
                    ]'

""" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Récupération du data à aggréger chez les autres services
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

END_POINT = ""
PATH_DEALS = END_POINT + "/v1/deals"
PATH_FACILITIES = END_POINT + "/v1/facilities"
PATH_INSURANCES = END_POINT + "/insurance"

def fetchDataById( path, id ):
    response = requests.get( path + "/" + str(id) )
    return ( -1 if response.status_code != 200 else response.json() )

def fetchDealById( id ):
    """ retourne le Deal sous forme de dict()
        nom, montant, zone, devise, borrower, lender, status
    """
    return res_deal_id


def fetchAllDeals():
    """ retourne tous les Deals sous forme de liste de dict()
        code, nom, montant, zone, devise, borrower, lender, status
    """
    res_json = requests.get( PATH_DEALS )
    res_dict = json.loads( res_json )
    return res_dict


def fetchInsuranceById( id ):
    """ retourne l'Assurance sous forme de dict()
        nom, pourcentage
    """
    return res_insurance_id

def fetchAllInsurances():
    """ retourne toutes les Assurances sous forme de liste de dict()
        code, nom, pourcentage
    """
    res_json = requests.get( PATH_INSURANCES )
    res_dict = json.loads( res_json )
    return res_dict


def fetchFacilityById( id ):
    """ retourne la Facilité sous forme de dict()
        nom, facility_code, amount, devise, entities :  [
                                                            [name, calendar, percentage],
                                                            [name, calendar, percentage],
                                                            ...
                                                        ]
    """
    return res_facility_id

def fetchAllFacilities():
    """ retourne toutes les Facilités sous forme de liste de dict()
        deal_code, nom, facility_code, amount, devise, entities :   [
                                                                        [name, calendar, percentage],
                                                                        [name, calendar, percentage],
                                                                        ...
                                                                    ]
    """
    res_json = requests.get( PATH_FACILITIES )
    res_dict = json.loads( res_json )
    return res_dict