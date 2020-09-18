from requests_html import HTMLSession

session = HTMLSession()

url = 'https://parkingapps.ucr.edu/spaces/'

r = session.get(url)

r.html.render(sleep=1, keep_page=True, scrolldown=1)

lots = r.html.find('.col-sm-6')

filename = 'parking_data.csv'
f = open(filename, 'w')

headers = 'lot, empty_spaces, time\n'
f.write(headers)

for i in range(0, len(lots) - 1):
    # Info for each lot is returned as list of strings.
    # All info for single lot is a single string with data seperated with newlines
    # e.g ('Lot 24-\n3:40pm\nCanyon Crest Drive\nFree Spaces\n405\nOccupancy\n0%\n')
    split_string = lots[i].text.split('\n') 
    parking_lot = {
        'Parking Lot' : split_string[0].replace('-', ''),
        'Time' : split_string[1],
        'Free Spaces' : split_string[4],
        'Occupancy' : split_string[6],
    } 
    print(parking_lot)

    f.write(parking_lot.get('Parking Lot') + ',' + parking_lot.get('Free Spaces') + ',' + parking_lot.get('Time') + '\n')

f.close()
session.close()

# # ---- Gets and displays all info for all parking lots (for testing) ----
# lots = r.html.find('.col-sm-6')

# for lot in lots:
#     print(lot.text)