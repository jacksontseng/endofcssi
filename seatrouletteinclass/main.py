#!/usr/bin/env python

import webapp2
import jinja2
import os
import random
import logging

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        group_one = []
        group_two = []
        group_three = []
        group_four = []
        group_five = []
        groups = [group_one, group_two, group_three, group_four, group_five]
        students = ["Ahmed", "Phung", "Anne", "Tanvi", "Ethan",
        "Jenessa", "Milan", "Andrea", "Loni", "Jackson", "Faduma",
        "Ivan", "Liz", "Alycia", "Chloe", "Ryan", "Kelsi"]

        num_students = 17
        num_tables = 5
        spts = num_students/num_tables
        random.shuffle(students)

        # while students:
        #     i = 0
        #     logging.info("test")
        #     for tables in groups:
        #         logging.info("forloop")
                # print students(i)

                # groups[tables].append(students(0))
                # students.remove()
                # i+=1



        print group_one
        table_one = {"id": "table1", "students": group_one}
        table_two = {"id": "table2", "students": group_two}
        table_three = {"id": "table3", "students": group_three}
        table_four = {"id": "table4", "students": group_four}
        table_five = {"id": "table5", "students": group_five}

        tables = [table_one, table_two, table_three, table_four, table_five]


        template = jinja_environment.get_template('templates/index.html')
        self.response.out.write(template.render(tables = tables))


        #to print without using jinja, won't work with jinja running
        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.write(group_one)
        # self.response.write(group_two)
        # self.response.write(group_three)
        # self.response.write(group_four)
        # self.response.write(group_five)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
