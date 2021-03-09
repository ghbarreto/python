print("==============================================")
print("")
print("Exercise 8-6 City Names")

def city_country(city, country):
    formatted = print(f"{city.title()}, {country.title()}")
    return formatted

city_country(country='canada', city='vancouver')

print("==============================================")
print("")
print("Exercise 8-7 Album")

def make_album(artistName, album):
    formatted = print(f"'{artistName}': '{album}'")
    return formatted

make_album(artistName='Bon Jovi', album='Livin on a Prayer')
make_album(album='Highway to hell', artistName='AC/DC')
make_album(artistName='Black Sabbath', album='Heaven and hell')



print("==============================================")
print("")
print("Exercise 8-8 User Albums")

def make_albums(artistName, album):
    formatted = print(f"The artist name is: '{artistName}', and the album is: '{album}'")
    return formatted

albumCreation = True

while albumCreation:
    artist = input("Choose an artist name: ")
    albumName = input("choose an album name: ")
    exits = input('To exit, press q')
    make_albums(artistName= artist, album= albumName) 
    
    if(exits == 'q'):
        albumCreation = False
