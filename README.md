# Election Results
This application is built on the flask microframework.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install -r requirements.txt
```

The web server reads a JSON file containing election results. 
You can use the supplied JSON file [election_data.json](/election_data.json) if you would like. It contains several states and each state has several counties.

If you would like to generate a new data set you can do so by running the included python script [gen_data.py](/gen_data.py)
```bash
python3 gen_data.py
```
The file will be replaced.

## Usage
Run the application with `flask run`. You should see the server running.

```bash
 Serving Flask app 'election_results.py' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
[2022-05-24 22:07:03,430] INFO in __init__: Elections startup
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

Alternatively you can start the application in a docker file.  
Build the docker image with
```bash
docker build . -t election_results
```
You can launch the container with
```bash
docker run --rm -it election_results
```


## Endpoints
The server has several endpoints. The main endpoints are:

[/states/](http://localhost:5000/states/) - This endpoint returns a list of all states present in our data set  
[/states/Florida/](http://localhost:5000/states/Florida/) - When a state is present, each county is returned with the republican and democrat who received the most votes in that county.

[/states/Florida/counties/](http://localhost:5000/states/Florida/counties/) - This enpoint returns a list of all counties in that state present in our data set  
[/states/Florida/counties/Justinfurt/](http://localhost:5000/states/Florida/counties/Justinfurt/) - When a state and county is present, The republican and democrat who received the most votes in that county are returned.

There are 2 other endpoints registered but with no functionality due to time constraints.
[/overall](http://localhost:5000/overall) - Intended to return the calculated overall winner across all states and counties  
[/index](http://localhost:5000/index) - No intended use. Just the root path.


## TODO and other approaches
I originally explored [pandas](https://pandas.pydata.org/) as a way to import and calculate the winners. 
It ended up being much to time-consuming for me to figure out how to load the data into usable data structures.
It seemed like the out-of-the-box functionality was more useful for matrix data. I'm confident that the data could be 
loaded successfully, but it was out of scope for the task.

The final endpoint does not have any functionality. I would not have had time to document and finalize the code. I would have used a 
total votes approach and cumulatively added the ballots cast for each candidate in each county. I believe this is where the 
pandas library would have proved the most useful.

There are a lot of improvements that can be made. Some liberties were taken such as leniency on case-sensitive and white-space sanitization of input.  
Error catching would be another improvement.


### Author
Roy Myers: myersrdev@gmail.com

