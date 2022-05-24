from app import app

@app.errorhandler(404)
def not_found_error(error):
    return f'Location Results not found', 404


@app.errorhandler(500)
def internal_error(error):
    return f'Sorry, something went wrong on our end. Please try again.', 500