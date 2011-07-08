#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from should_dsl import should
from domain.node.person import Person
from domain.supportive.association_error import AssociationError
from bank_system.decorators.attendant_decorator import AttendantDecorator
from bank_system.decorators.employee_decorator import EmployeeDecorator

class AttendantDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.an_employee_decorator = EmployeeDecorator()
        self.an_attendant_decorator = AttendantDecorator()
        self.a_person = Person()

    def it_decorates_a_person(self):
        #should fail
        (self.an_attendant_decorator.decorate, self.a_person) |should| throw(AssociationError)
        #should work
        self.an_employee_decorator.decorate(self.a_person)
        self.an_attendant_decorator.decorate(self.a_person)
        self.an_attendant_decorator.decorated |should| be(self.a_person)
        self.a_person |should| have(2).decorators
