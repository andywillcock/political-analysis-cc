import numpy as np

def extract_repeat_donors(record_row,final_set,percent):
    """
    
    :param record_row (dict): Row of data checked for validity by data_check(), stored as a dictionary with column names as keys
    and data as values
    :param final_set (pd.DataFrame): Pandas DataFrame that will store all rows being used to calculate aggregate donations
    for all candidates by zipcode
    :param percent (int): Percentile to be used in calculations
    :return: repeated_donations (np.ndarray): Array of values to be written out to repeat_donors.txt
    """

    record_row['COUNT'] += 1
    final_set = final_set.append(record_row, ignore_index=True)

    agg_donations = final_set[(final_set['CMTE_ID'] == record_row['CMTE_ID']) &
                    (final_set['ZIP_CODE'] == record_row['ZIP_CODE']) &
                    (final_set['TRANS_DT'] == record_row['TRANS_DT'])]

    donation_amounts = sorted(agg_donations.TRANS_AMT.tolist())
    percentile = donation_amounts[int(round((30/100)*len(donation_amounts)))]

    repeated_donations = np.asarray([record_row['CMTE_ID'], record_row['ZIP_CODE'], record_row['TRANS_DT'],
    str(int(round(percentile, 0))),str(int(sum(agg_donations.TRANS_AMT))), str(int(sum(agg_donations.COUNT)))])

    return repeated_donations
