#!/opt/anaconda/bin/python


#import libraries
import os
from datetime import datetime as dati
import requests

#get time as string
now=dati.now()
date_string = now.strftime("%Y%m%d")

#use to make filename
file_name = f'naptan_{date_string}.zip'

#set naptan url
naptan_url = "http://naptan.app.dft.gov.uk/DataRequest/Naptan.ashx?format=csv"

#set dest folder
dest_folder = "/naptan_store/naptan_by_date/"

#get the content from the url
resp = requests.get(naptan_url)

#get the data
thedata= resp.content

#make full filename of the destinationfile
my_full_filename = os.path.join(dest_folder, file_name)

#open your new file
zfile= open(my_full_filename, 'wb')

#write the data
zfile.write(thedata)

#close the file
zfile.close()



