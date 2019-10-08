#!/bin/python

import unittest

import models
import tests

print("Attributes in 'models' module: " + str(dir(models)))
#print("Attributes in 'models' module: {}".format(dir(models)))

unittest.main(tests.TestOne)

while True:
    test = models.User(input("Enter your name: "))
