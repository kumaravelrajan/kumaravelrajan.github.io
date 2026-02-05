---
categories:

    - programming
    - py

description: Learning about Flask web framework and about the web in general.

published: true
---

# Web servers, WSGI servers and web applications

The heirarchy of how web requests from browsers reach our Flask web application is as follows.

**Client sends Request** &#8596; **Web server** (NGINX, Apache) &#8596; **WSGI server** (Gunicorn) &#8596; **Flask web app**

Earlier, without WSGI it used to be the case the when the user chose a python web framework they were also tied to use a specific web server. They could not switch between servers. WSGI was created to solve this problem as the common gateway between web servers and python web applications. 

Here is how a request-response cycle looks like:

1. Request: 

    Client sends a HTTP request to web server. Server receives this and send raw data to WSGI server. The WSGI server packages the raw data in the form of a python dictionary and sends it to our Flask app. The flask app matches the URL with the routes we have configured and starts executing the corresponding function.

1. Response:

    Our Flask app returns the status code and repsonse body data to the WSGI server. The WSGI server packages our response body into a legitimate HTTP response and forward to web server. The webserver adds its server specific headers and sends the data packets over the internet.

# URL processors vs URL params (also Query params v/s Path params)

**URL parameters** is any data passed to the web app using URL. URL parameters can be Query parameters or path parameters. 

**Path parameters** passed as part of the URL path.

**Query parameters** are passed as key=value pairs with a "?" separating the path and query parameters.

**URL Processor** refers to any code on the web app side that handles data passed on in the URLs.

```py

#--------------------
# Path URL parameters
#--------------------

# Getting a string and displaying a string
@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}!"

# Getting a string but wanting it to behave like numbers
@app.route("/add_wrong/<num1>/<num2>")
def add_wrong(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}" # For num1 = 20 and num2 = 30, this returns 2030.

# Getting path params as int and not as string
@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}" # Correct sum of 20 + 30 = 50 is shown.

#--------------------
# Query URL parameters
#--------------------
@app.route("/login")
def handle_params():
    username = request.args.get("username") 
    password = request.args.get("password")

    return f"Username: {username} <br>Password: {password}"

```

# GET vs POST request in HTTP
Flask functions by default handle only GET requests. If a POST request is made from the browser to a function handling only GET requests, an error will be returned to the broser. In fact, control never even reaches the corresponding py function in our web app.

```py

#------------------------------------------------------------
# GET vs POST request and handling them separately in flask
#------------------------------------------------------------

# Configure method to allow both flask GET and POST methods
@app.route("/getandpost", methods = ["GET", "POST"])
def getandpost():
    if request.method == "GET":
        return "GET method used."
    elif request.method == "POST":
        return "POST method used."
    else:
        return "This message will never be returned."

```

# Specifying status codes in response

```py
#--------------------
# Returning status codes
#--------------------

# Directly in return statement
@app.route("/get202status")
def get202status():
    return "get200status() method successfully called.", 202

# Using make_response()
@app.route("/get202statuswithmakeresponse")
def get202statuswithmakeresponse():
    response = make_response()

    response.status_code = 202
    response.data = "get202statuswithmakresponse() successfully called"
    response.content_type = "text/customkumartext" #!!!!

    return response
```