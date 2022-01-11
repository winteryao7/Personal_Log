# Personal_Log
A list of personal logs for data processing

About converting data from Refteck format to Mseed

rt_mseed is an older version and hard to transplant to other machine; 
rt2ms could be an alternative choice. 

Try: install passoft3 from following link (https://www.passcal.nmt.edu/content/software-resources)

conda activate passoft3 

1. Put raw refteck output (normall organized as DATE/SensorID/1) under RAWDATA/
Note: I like to put ZIP file under each directory, and unzip into different daily folders
2. rt2ms -d RAWDATA -e (this would result in a parfile; a list of different channels)
3. rt2ms -d RAWDATA -p parfile.txt (then bingo; a new directory would be created, called MSEED/)

About running NoisePy 

I stored my data as mseed format, and then using S0B_to_ASDF.py to convert to h5 format
A few places: a) it takes some time to generate the file allfiles_time.txt; b) modify 
a few parameters if necessary (sampling rate; frequency range; instrument response, etc)

# Setup connection to remote host 

systemctl status sshd 

systemctl start sshd

figure out the ip address: ifconfig
