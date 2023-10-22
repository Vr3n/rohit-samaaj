import json


with open("scraping/stateWiseDistrict.json", "r") as state_file:
    file_contents = state_file.read()

states_data: dict = json.loads(file_contents)

states_list = [state.capitalize() for state in list(states_data.keys())]


# Creating states fixture
state_fixture = [
    {
        "model": "survey.statemaster",
        "pk": i + 1,
        "fields": {
            "state": state,
            "country": 1  # Country defaults to India.
        }
    }
    for i, state in enumerate(states_list)
]

# Creating Countries fixture.
country_fixture = [
    {
        "model": "survey.countrymaster",
        "pk": 1,
        "fields": {
            "country": "India"
        }
    }
]


with open("fixtures/countrymaster.json", "w") as country_file:
    json.dump(country_fixture, country_file)


with open("fixtures/statemaster.json", "w") as state_file:
    json.dump(state_fixture, state_file)
