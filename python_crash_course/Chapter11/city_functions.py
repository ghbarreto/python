def city_country(city, country):
    ans = f"{city.title()}, {country.title()}"
    return ans

def population(city, country, population =''):
    if population:
        ans = f"{city.title()}, {country.title()}, {population.title()}"
        return ans
    else:
        ans = f"{city.title()}, {country.title()}"
        return ans