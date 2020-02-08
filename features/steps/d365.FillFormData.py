import csv
from behave import *


@step('Fill form data from csv file "{file_name}"')
def step_impl(context, file_name):
    with open("./features/{}".format(file_name)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            context.d365Client.form_fill_attribute_by_display_name(row[0], row[1])
