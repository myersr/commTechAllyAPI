import json


def get_dict_from_file():
    obj = {}
    with open('election_data.json') as infile:
        obj = json.loads(infile.read())
    return obj

def get_state_dict_by_state(state):
    obj = {}
    with open('election_data.json') as infile:
        obj = json.loads(infile.read())


class State:
    def __init__(self, state):
        self.state = state
        self.counties = self.set_counties(self.get_state(state))
        # self.data = data


    @staticmethod
    def set_counties(counties):
        return map(lambda county: County(county=county.key(), voting_records=county[county.key()]),   counties)

    @staticmethod
    def get_all_states():
        obj = get_dict_from_file()
        print(list(obj.keys()))
        return { 'states': list(obj.keys()) }

    @staticmethod
    def get_state(state):
        obj = get_dict_from_file()
        if state in obj:
            return obj[state]

    def get_winners_all_counties(self):
        outer = map(lambda x: {x.county: x.get_winners()}, self.counties)
        print(str(outer))
        return outer

class County:
    def __init__(self, county, voting_records):
        self.county = county
        self.republicans = Votes(voting_records["Republicans"])
        self.democrats = Votes(voting_records["Democrats"])

    def __init__(self, state, county):
        self.county = county
        full = self.get_county_by_state(state, county)
        self.republicans = Votes(full["Republicans"])
        self.democrats = Votes(full["Democrats"])

    @staticmethod
    def get_county_by_state(state, county):
        obj = get_dict_from_file()
        if state in obj:
            if county in obj[state]:
                return obj[state][county]

    def get_winners(self):
        return map(lambda x: x.get_winner(), [self.republicans, self.democrats])

    @staticmethod
    def get_counties_by_state(state):
        obj = get_dict_from_file()
        if state in obj:
            return {'counties': list(obj[state].keys())}


class Votes:
    def __init__(self, voting_records):
        self.records = voting_records

    def get_winner(self):
        return max(self.records, key=self.records.get)
