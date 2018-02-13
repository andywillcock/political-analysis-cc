import pytest
from data_checks import *

def test_good_data():

    row1 = 'C00999999|N|M2|P|201702039042412112|15|IND|WILLCOCK, ANDREW|SAN FRANCISCO|CA|941156146|CVS HEALTH|' \
          'VP, RETAIL PHARMACY OPS|01122017|500||2017020211435-887|1147467|||4020820171370030285'

    record1 = {'CMTE_ID': 'C00999999', 'NAME': 'WILLCOCK, ANDREW', 'ZIP_CODE':'94115',
                       'TRANS_DT': 2017,
                       'TRANS_AMT': 500, 'OTHER_ID': '', 'COUNT': 0}

    data_check_output1 = data_check(row1)


    assert record1 == data_check_output1

def test_bad_date():

    row2 = 'C00999999|N|M2|P|201702039042412112|15|IND|WILLCOCK, ANDREW|SAN FRANCISCO|CA|941156146|CVS HEALTH|' \
           'VP, RETAIL PHARMACY OPS|01122|500||2017020211435-887|1147467|||4020820171370030285'

    record2 = False
    
    data_check_output2 = data_check(row2)

    assert record2 == data_check_output2
