
def data_check(row):
    from datetime import datetime
    """
    Performs checks on row of political donation data to see if all data in that row is valid. If data is valid a
    dictionary containing the relevant data (column name:data) for further processing.
    :param row: row of data read in from open pipe delimited file formatted FEC 2015 Data Dictionary
    :return: record_data - dictionary of relevant data (column name:data)
    """
    # Check to see if the line of data is in the format described by the FEC data dictionary. Each line needs to have
    # 21 pipe-separated values
    if len(row.split('|')) != 21:
        return False

    # Read row of data into list and check if each data points meets the requirements outlined in the Input File
    # Considerations instructions
    record_data = [row.strip('\n').split('|')[i] for i in [0, 7, 10, 13, 14, 15]]
    now = datetime.now()
    if record_data[0] == '' or len(record_data[2]) < 5 or record_data[3] == '' or \
            len(record_data[3].strip(" ")) != 8 or datetime.strptime(record_data[3], '%m%d%Y') > now \
            or record_data[4] == '' or record_data[5] != '':

        return False

    # If data passes all checks return a dictionary with the relevant data headers as keys and the data as values
    else:
        record_data = {'CMTE_ID': record_data[0], 'NAME': record_data[1], 'ZIP_CODE': record_data[2][0:5],
                       'TRANS_DT': int(record_data[3][-4:]),
                       'TRANS_AMT': float(record_data[4]), 'OTHER_ID': record_data[5], 'COUNT': 0}

        return record_data




