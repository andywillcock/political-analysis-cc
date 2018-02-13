from data_checks import *
from extract_repeat_donors import *
import argparse

import numpy as np
import pandas as pd

def find_repeat_donors(input_file,percentile_file,output_file):
    """
    Uses the provided files to pull relevant data from pipe-delimited file of FEC donation records. Writes out rows
    containing information defined in the output directions of the Insight_Readme.md file.

    :param input_file: Filepath of file containing rows of 21 pipedelimited filed as defined by the FEC
    :param percentile_file: File containing one number 1-100 defining what percentile to use in calculations
    :param output_file: Filepath for output file for results of analysis to be written to
    :return: None
    """

    records_names = ['CMTE_ID','NAME','ZIP_CODE','TRANS_DT', 'TRANS_AMT', 'OTHER_ID']

    # Open input file and read in as stream of data line by line
    with open(percentile_file,'r') as percent:
        percentile = int(percent.read())
    with open(input_file, 'r') as data:

        donors = pd.DataFrame(columns=records_names)
        holder = {'CMTE_ID':'','NAME':'','ZIP_CODE':'','TRANS_DT':0000,'TRANS_AMT':0,'COUNT':0}
        final_set = pd.DataFrame(data = holder,index=[0])
        outfile = open(output_file, 'w')

        for row in data:

                record_data = data_check(row)

                #find indices of all repeat donations in the current table (all rows read in)
                if record_data != False:
                    previous_donations =  map(int,donors.index[(donors['NAME'] == record_data['NAME']) &
                                               (donors['ZIP_CODE']== record_data['ZIP_CODE'])].tolist())

                    # Check if all the subsequent donations by the same donor came after the first donation's date
                    if previous_donations != []:

                        if donors.iloc[previous_donations[0]]['TRANS_DT'] <= record_data['TRANS_DT']:
                            # Adds the most recent donation by a given donor to the dataset that will be used to calculate
                            # the aggregate donation data
                            for i in previous_donations[-1:]:

                                repeaters, final_set = extract_repeat_donors(record_data,final_set,percentile)

                                # Write line of aggregated donations with total amount, percentile, and count for each
                                # Candidate, zipcode, and year
                                repeaters.tofile(outfile,sep='|',format='%s')
                                outfile.write('\n')

                    donors = donors.append(record_data, ignore_index=True)

        outfile.close()
        data.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file',
                        help='filepath containing political donors input data')
    parser.add_argument('percentile',
                        help='filepath containing percentile to be used in calculations')
    parser.add_argument('output_file',
                        help='filepath to store output data')
    args = parser.parse_args()
    input_filepath = args.input_file
    percentile_filepath = args.percentile
    output_filepath = args.output_file
    find_repeat_donors(input_filepath,percentile_filepath,output_filepath)


