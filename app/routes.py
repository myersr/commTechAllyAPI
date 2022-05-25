from app import app
from app.models import State, County
from markupsafe import escape


@app.route("/")
def index():
    return "index"

##
# `/states/`
#     returns a list of all states present in our data set
# `/states/<state>/`
#     @state: String - The name of the state to query
#     When a state is present, each county is returned with the republican
#     and democrat who received the most votes in that county.
##
@app.route("/states/", methods=['GET'])
@app.route("/states/<state>/", methods=['GET'])
def state_winners(state=None):
    if not state: # If state is not present we return a list of all states
        return escape(State.get_all_states())

    state = state.capitalize()#str.casefold(state) # Ideally would be sanitized at the routing level
    s = State(state)
    return s.get_winners_all_counties() # Return the list of counties and related winners

##
# `/states/<state>/counties/`
#     @state: String - The name of the state to query
#     returns a list of all counties in that state present in our data set
# `/states/<state>/counties/<county>/"`
#     @state: String - The name of the state to query
#     @county: String - The name of the county to query
#     When a state and county is present, The republican
#     and democrat who received the most votes in that county are returned.
##
@app.route("/states/<state>/counties/")
@app.route("/states/<state>/counties/<county>/")
def county_winners(state, county=None):
    state = state.capitalize() # State is the only case independent variable
    if not county: # If county is not present we return a list of all counties present
        return escape(County.get_counties_by_state(state))
    county_full = County(county, state) # We retrieve the data and cast as app.models#County

    # We call get_winner() to retrieve the winning republican and democrat
    # TODO// validate an absence of candidates
    return {'republican': county_full.republicans.get_winner(), 'democrat': county_full.democrats.get_winner()}

##
# `/overall/`
#     Intended to return the overall winning primary election democrat and republican
#     The logic was not finished
##
@app.route("/overall")
def overall_winners():
    return f'overall primary winners'
