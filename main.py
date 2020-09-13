from requests_html import HTMLSession

session = HTMLSession()

url = 'https://parkingapps.ucr.edu/spaces/'

r = session.get(url)

r.html.render(sleep=1, keep_page=True, scrolldown=1)

lots = r.html.find('.col-sm-6')

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

session.close()

# # ---- Gets and displays all info for all parking lots (for testing) ----
# lots = r.html.find('.col-sm-6')

# for lot in lots:
#     print(lot.text)