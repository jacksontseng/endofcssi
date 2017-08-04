#!/usr/bin/env python

import webapp2
import os
import jinja2

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render())
        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.write('GET: Hello world!')

    def score(my_vars):
        points = 0
        if my_vars["corndog"] == "no":
            points +=1
        if my_vars["fried_chicken"] == "yes":
            points +=1
        if

        return points
    def post(self):


        my_vars = {
            "corndog":self.request.get("corndog"),
            "fried_chicken":self.request.get("fried_chicken"),
            "definition":self.request.get("celebrity"),
            "cut_in2":self.request.get("cut_in2"),
            "color":self.request.get("color"),
            "enthusiast":self.request.get("enthusiast"),
            "score":score(my_vars)
        }


        if not my_vars["enthusiast"] == "checked":
            template = jinja_environment.get_template('templates/try_again.html')
            self.response.out.write(template.render(my_vars))
        else:
            template = jinja_environment.get_template('templates/results.html')
            self.response.out.write(template.render(my_vars))
        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.write('POST: Hello, World!')


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
