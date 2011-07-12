#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from should_dsl import should
from domain.node.person import Person
from domain.node.machine import Machine
from domain.supportive.association_error import AssociationError
from bank_system.decorators.bank_account_decorator import BankAccountDecorator
from bank_system.decorators.attendant_decorator import AttendantDecorator
from bank_system.decorators.employee_decorator import EmployeeDecorator
from bank_system.decorators.client_decorator import ClientDecorator
from bank_system.decorators.attendant_decorator import InsuficientFunds
from bank_system.resources.check import Check

class AttendantDecoratorSpec(unittest.TestCase):

    def setUp(self):
        self.an_employee_decorator = EmployeeDecorator()
        self.an_attendant_decorator = AttendantDecorator()
        self.an_attendant = Person()

    def it_decorates_a_person(self):
        #should fail
        (self.an_attendant_decorator.decorate, self.an_attendant) |should| throw(AssociationError)
        #should work
        self.an_employee_decorator.decorate(self.an_attendant)
        self.an_attendant_decorator.decorate(self.an_attendant)
        self.an_attendant_decorator.decorated |should| be(self.an_attendant)
        self.an_attendant |should| have(2).decorators

    def it_gets_a_check(self):
        #Receiving a check
        self.an_employee_decorator.decorate(self.an_attendant)
        self.an_attendant_decorator.decorate(self.an_attendant)
        a_check = Check(id_="123", account_number="1234-5", value=10.0)
        #           Verifing check attributes
        #-------------------------------------------------
        a_check.id_ |should| equal_to("123")
        a_check.account_number |should| equal_to("1234-5")
        a_check.value |should| equal_to(10.0)
        #-------------------------------------------------

    def it_discount_a_check(self):
        #Discounting a check, it should work!
        a_machine = Machine()
        a_client = Person()
        a_client_decorator = ClientDecorator()
        a_client_decorator.decorate(a_client)
        a_bank_account_decorator = BankAccountDecorator(a_client,"1234-5")
        a_bank_account_decorator.average_credit = 100
        a_bank_account_decorator.decorate(a_machine)
        a_check = Check(id_="123", account_number="1234-5", value=10)
        self.an_attendant_decorator.discount_check(a_check)
        a_bank_account_decorator.average_credit |should| equal_to(90)
        #It should fail!
        other_bank_account_decorator = BankAccountDecorator(a_client,"1235-5")
        other_bank_account_decorator.average_credit = 100
        other_bank_account_decorator.decorate(a_machine)
        a_check = Check(id_="123", account_number="1235-5", value=110)
        (self.an_attendant_decorator.discount_check, a_check) |should| throw(InsuficientFunds)
        other_bank_account_decorator.average_credit |should| equal_to(100)

    def tearDown(self):
        BankAccountDecorator = []
