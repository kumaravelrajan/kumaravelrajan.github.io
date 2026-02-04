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




