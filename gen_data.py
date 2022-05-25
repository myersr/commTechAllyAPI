from faker import Faker
import numpy as np
import json

fake = Faker()

state_limit = 20
dem_limit = 6
rep_limit = 7
mast_json = {}
states = [fake.unique.state() for i in range(state_limit)]
dem_candidates = [fake.unique.last_name() for i in range(1, dem_limit)]
rep_candidates = [fake.unique.last_name() for i in range(1, rep_limit)]
for x in states:
    state_level = {}
    counties = [fake.unique.city() for i in range(np.random.randint(2, 5))]
    for y in counties:
        county_level = {}
        democrat_level = {}
        for z in dem_candidates:
            democrat_level[z] = np.random.randint(0,600)
        county_level["Democrats"] = democrat_level
        republican_Level = {}
        for z in rep_candidates:
            republican_Level[z] = np.random.randint(0,600)
        county_level["Republicans"] = republican_Level
        state_level[y] = county_level
    mast_json[x] = state_level

with open('election_data.json', 'w') as outfile:
    json.dump(mast_json, outfile, indent=2)