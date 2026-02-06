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

# Dynamically alter HTML using Jinja templates

Flask using the Jinja templating language in order to alter the HTML served to browsers based on python code. 
    
## Passing list to HTML and using control structures

```py

# py

# Pass list to HTML
@app.route("/displaylist")
def displayList_fun():
    mylist = [10, 20, 30, 40, 50]
    return render_template("displaylist_template.html", mylist = mylist)
```

```html
<!-- html -->
{%raw%}
<body>
    <h1>Jinja variables: Lists</h1>
    <p>The below List is rendered using Jinja variables:</p>
    
    <ul>
        {%for item in mylist%}

            <li {%if item == 20 %} style = "color: red" {%endif%}>
                {{ item }}
            </li>

        {%endfor%}
    </ul>
</body>
{%endraw%}
```

# Inheriting templates

Certain sections like the navigation bar and footer are present in every single web page. In order to avoid duplicating this HTML code we can create a base template and inherit from it. 

Here, the home.html that serves the "/" url and displaylist_template.html that serves the "displaylist" url inherit from the base.html file. app.py remains unchanged.

```py
# app.py

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates") #!

# --------------------------------------------------
# Manipulating HTML templates using Jinja
# --------------------------------------------------

# Pass strings to HTML
@app.route("/")
def index():
    return render_template("home.html", hello_str = "Hello", world_str = "World")

# Pass list to HTML
@app.route("/displaylist")
def displayList_fun():
    mylist = [10, 20, 30, 40, 50]
    return render_template("displaylist_template.html", mylist = mylist)

```


{%raw%}
```html

<!-- base.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> {%block title%}Default value{%endblock%} </title>
</head>
<body>

    <p>This is from base.html and will always be present here.</p>

    {%block content%}

    {%endblock%}
    
</body>
</html>

```

```html

<!-- home.html -->

 {%extends "base.html" %}

{%block title%} Home page {%endblock%}

{%block content%}
<h1>Jinja variables</h1>
<p>The below text is rendered using Jinja variables:</p>
<p>{{hello_str}} {{world_str}} </p>

{%endblock%}

```

```html

<!-- displaylist.html -->

 {%extends "base.html"%}

{%block title%} Display list {%endblock%}

{%block content%}

<h1>Jinja variables: Lists</h1>
<p>The below List is rendered using Jinja variables:</p>

<ul>

    {%for item in mylist%}

        <li {%if item == 20 %} style = "color: red" {%endif%}>
            {{ item }}
        </li>

    {%endfor%}

</ul>

{%endblock%}

```

{%endraw%}

# Jinja filters

Filters manipulate data in ways we want. For example passing a string through the "upper" filter using {{mystring | upper}} gives back the mystring in upper case. 

Filters can be both predefined and custom defined.

{%raw%}

```html
<!-- home.html -->

<!-- Built in filters -->
<p>{{(hello_str ~ " " ~ world_str) | upper}}</p>
<p>{{(hello_str ~ " " ~ world_str) | lower}}</p>
<p>{{(hello_str ~ " " ~ world_str) | reverse}}</p>
<p>{{(hello_str ~ " " ~ world_str) | wordcount}}</p>

<!-- Custom filter -->
<p>{{(hello_str ~ " " ~ world_str) | title_case}}</p>

```

```py

# app.py

# --------------------------------------------------
# Custom filters
# --------------------------------------------------

@app.template_filter()
def title_case(s: str):
    newstring = ""
    for index, c in enumerate(s):
        if index % 2 == 0:
            newstring += c.upper()
        else:
            newstring += c.lower()

    return newstring

```

{%endraw%}

# Dynamic URL and Redirection

The URL for a page can also be dynamically assigned instead of being statically assigned. That is, consider a function index() serving home.tml initially given the static url "/". Then, for whatever the reason, we need to change the url to "/index". In this case, any other HTML referring to "/" with the intent of getting home.html will now have a broken link. To avoid this we can create dynamic links. 

We can also redirect a user wanting to visit "/" with the intent of getting hold of home.html to "/index".

1. Dynamic URL using url_for()

    The below HTML code will always correctly refer to the displayList_fun that renders displaylist_template.html irrespective of how the route of displayList_fun is changed. It could be "/displaylist" or "/displaylistnew". The link to displaylist_template.html in home.html will always point to the correct one.

    {%raw%}

    ```py

    # app.py

    # Pass list to HTML
    @app.route("/displaylist")
    def displayList_fun():
        mylist = [10, 20, 30, 40, 50]
        return render_template("displaylist_template.html", mylist = mylist)
    
    ```

    ```html

    <!-- home.html linking to /displaylist -->

    <!-- Dynamic link to displaylist_template.html being served by displaylist() py function in app.py-->

    <a href="{{url_for("displayList_fun")}}">Click here to navigate to DisplayList site.</a>
    
    ```

    {%endraw%}

1. Redirecting from one url to another

    Whenever someone tries accessing /redirect_endpoint they are redicted to /displaylist.

    ```py

    @app.route("/redirect_endpoint")
    def redirect_endpoint():
        return redirect(url_for("displayList_fun"))
    
    ```

