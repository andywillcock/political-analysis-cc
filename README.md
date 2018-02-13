### Approach

My approach focused on building a compact script that would leverage available data analysis packages in Python to 
efficiently complete the task at hand. 

##### Checking Data Validity
   
Using the guidelines from the challenge instructions I set up a series of boolean checks that would check each line of 
data as it was read in. These booleans quickly check if the row itself is valid and then check to see that each piece of
data of interest was validly formated.

##### Finding Donors of Interest

After reading in each row and checking the data validity the script then searches the full data set for any other rows
that contain the same name and zip code for a donor. The row is then checked to see if the year of the donation occurred
after the first donation found in the stream for that donor. The most recent occurance of this donor in the stream is 
then added to final set of donations and a new row of 

CMTE ID, ZIP CODE, TRANS_DT, TOTAL DONATIONS, DONATION AT GIVEN PERCENTILE, COUNT OF DONATIONS

is returned to be written out to the open output file.

This process is repeated so long as there are new rows in the input data stream.

##### Packages/Dependencies

numpy

pandas

argparse
