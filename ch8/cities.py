def describe_city(city_name,country='canada'):
    print("\n" + city_name.title() + " is in " + country.title() + "!")

describe_city('montreal')
describe_city('new york',country='USA')
describe_city('paris',country='france')