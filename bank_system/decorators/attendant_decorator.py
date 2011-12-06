#!/usr/bin/env python
# -*- codign: utf-8 -*-

from should_dsl import should
from domain.supportive.rule import rule
from domain.supportive.association_error import AssociationError
from domain.supportive.contract_matchers import be_decorated_by
from domain.base.decorator import Decorator
from bank_system.decorators.employee_decorator import EmployeeDecorator
from bank_system.decorators.bank_account_decorator import BankAccountDecorator

class AttendantDecorator(Decorator):
    '''Attendant'''
    decoration_rules = ['should_be_instance_of_person']

    def __init__(self):
        Decorator.__init__(self)
        self.description = "An employee with attendant skills"

    def discount_check(self, a_check):
        for account in BankAccountDecorator.active_accounts:
            if account.number == a_check.account_number:
                if account.average_credit >= a_check.value:
                    account.draw(a_check.value)
                else:
                    raise InsuficientFunds("Insuficient Funds")

class InsuficientFunds(Exception):
    pass
