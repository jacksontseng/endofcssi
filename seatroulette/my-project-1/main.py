# !/usr/bin/env python
import webapp2
import jinja2
import os
import webapp2
import logging
import random

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render(people))
        self.response.out.write(template.render(random_order))
        logging.info("test")
def split(dict):
    pass
def shuffle():
    list = []
    list = random.sample(range(17),17)
    return list
random_order = shuffle()

people = {"person":[{"name":"Jackson"}, {"name":"Alycia"}, {"name":"Phung"}, {"name":"Kelsi"},
{"name":"Ivan"}, {"name":"liz"}, {"name":"Tanvi"}, {"name":"Ahmed"}, {"name":"Andrea"}, {"name":"Milan"},
 {"name":"Chloe"}, {"name":"Anne"}, {"name":"Ryan"}, {"name":"Ethan"}, {"name":"Faduma"}, {"name":"Loni"}, {"name":"Jenessa"}],
 "random_order":random_order}

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
