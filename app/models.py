import json


# Helper function that returns a dictionary object of entire dataset
def get_dict_from_file():
    obj = {}
    with open('election_data.json') as infile:
        obj = json.loads(infile.read())
    return obj

##
#  State:
#    state:     String      - the name of the state
#    counties:  [County]    - array of County objects
##
class State:
    ##
    # initializer function
    #  state:   String  - Name of the state. Case-sensitive. Used to retrieve the counties from the dataset
    def __init__(self, state):
        self.state = state
        # We retrieve the whole state object from the dataset and casts the data
        # as an array of County
        self.counties = self.set_counties(self.get_state(state))

    ##
    #  return an array of County objects
    #  counties:    {dict}  - Takes the full dictionary directly under the state key in the dataset
    #                           Includes multiple counties and all the nested voting info for each
    @staticmethod
    def set_counties(counties):
        return map(lambda county: County(county=county, voting_records=counties[county]), counties)

    ##
    #  return a list of all state names in the dataset
    @staticmethod
    def get_all_states():
        obj = get_dict_from_file()
        return {'states': list(obj.keys())}

    ##
    #  return an entire state dictionary from the dataset
    #  state:   String  - Name of the state. Case-sensitive
    @staticmethod
    def get_state(state):
        obj = get_dict_from_file()
        if state in obj:
            return obj[state]

    ##
    #  return a dictionary of every county for this state and the winning rep/dem for each
    def get_winners_all_counties(self):
        # Loop through each county and call the County.get_winners() ending with a dict
        return {x.county: x.get_winners() for x in self.counties}


##
#  County:
#    county:     String      - the name of the county
#    republicans:  [Votes]   - array of Vote objects for republican candidates
#    democrats:  [Votes]     - array of Vote objects for democratic candidates
##
class County:
    ##
    # initializer function
    #  county:          String      - Name of the county. Case-sensitive. Used to retrieve the county from the dataset
    #  state:           String      - (Optional) Name of the state. Used if calling County outside a State obj
    #  voting_records:  Dictionary  - (Optional) The republican and democrat dataset with candidates
    # TODO// make one of state or voting_records required if the other is not present
    def __init__(self, county, state=None, voting_records=None):
        self.county = county
        if voting_records:
            self.republicans = Votes('republican', voting_records["Republicans"])
            self.democrats = Votes('democrat', voting_records["Democrats"])
        if state:
            full = self.get_county_by_state_and_county(state, county)
            self.republicans = Votes('republican', full["Republicans"])
            self.democrats = Votes('democrat', full["Democrats"])

    ##
    #  return the dictionary of the county
    #  state:   String  - Name of the state. Case-sensitive
    #  county:  String  - Name of the county. Case-sensitive
    @staticmethod
    def get_county_by_state_and_county(state, county):
        obj = get_dict_from_file()
        if state in obj:
            if county in obj[state]:
                return obj[state][county]

    ##
    #  return a dictionary of the winning republican and democrat for the county
    def get_winners(self):
        # Calls Votes.get_winner() for republican and democrat and assigns the winner to their party
        return { x.party: x.get_winner() for x in [self.republicans, self.democrats] }

    ##
    #  return a list of the counties for a specific state
    #  state:   String  - Name of the state. Case-sensitive
    @staticmethod
    def get_counties_by_state(state):
        obj = get_dict_from_file()
        if state in obj:
            return {'counties': list(obj[state].keys())}


##
#  Votes:
#    party:     String  - Name of the political party. Should be either "republican" or "democrat"
#    records:   Dict    - Dictionary of the candidates and their vote totals
class Votes:
    ##
    #  initializer function
    #  party:             String  - Name of the political party. Should be either "republican" or "democrat"
    #  voting_records:    Dict    - Dictionary of the candidates and their vote totals
    def __init__(self, party, voting_records):
        self.party = party
        self.records = voting_records

    ##
    #  return the candidate with the most votes
    def get_winner(self):
        return max(self.records, key=self.records.get)
