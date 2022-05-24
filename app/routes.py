from app import app
from app.models import State, County, Votes
from markupsafe import escape

# app = Flask(__name__)

@app.route("/")
def index():
    return "index"


@app.route("/state/", methods=['GET'])
@app.route("/state/<state>", methods=['GET'])
def state_winners(state=None):
    state = state.capitalize()#str.casefold(state)
    if not state:
        return escape(State.get_all())
    s = State(state)
    return {'Winners': escape(s.get_winners_all_counties())}

@app.route("/state/<state>/county/")
@app.route("/state/<state>/county/<county>")
def county_winners(state, county=None):
    state = state.capitalize()
    if not county:
        return escape(County.get_counties_by_state(state))
    county_full = County(state=state, county=county)
    return {'republican': county_full.republicans.get_winner(), 'democrat': county_full.democrats.get_winner()}

@app.route("/overall")
def overall_winners():
    return f'overall primary winners'
