from flask import Flask # we may need to pip install flask
from flask import render_template
import json

# we start by declaring our flask app
app = Flask(__name__)

# declare paths for routing
@app.route('/') # this is the ROOT of our service
def root():
    content = '''
    <h1>We are at the root of the service</h1>
    <a href='http://127.0.0.1:5000/home'>Home</a>
    '''
    return content

@app.route('/home') # we specify WHICH route should serve this asset
def home():
    return '<h1>Welcome to Flask Microservices</h1>'

@app.route('/data') # when passing data, it MUST be encoded, e.g. as JSON, html, text, xml etc.
def data():
    # struct = '{"name":"Deidre", "age":42, "member":true}'
    struct = {"name":"Deidre", "age":42, "member":True} # passes as JSON automatically
    struct_j = json.dumps(struct)
    # we can read json back to a structure
    s = json.loads(strut_j)
    print(type(struct_j))
    # we should consider adding 'headers' to our return, e.g. to specify data type
    return struct # Flask is intelligent to convert the dict to json for us

# here is a route with a parameter
@app.route('/hello') # .. for when there is no name
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('username.html', name=name)


if __name__ == '__main__':
    app.run() # call the app into play
    # to exercise this code:
    # - run this module (creates a server)
    # - open a browser
    # - browse to http://127.0.0.1:5000/home