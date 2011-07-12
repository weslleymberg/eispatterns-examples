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
    def __init__(self):
        Decorator.__init__(self)
        self.description = "An employee with attendant skilss"

    def decorate(self, decorated):
        try:
            AttendantDecorator.rule_should_contain_employee_decorator(decorated)
        except:
            raise AssociationError('Person must be previously decorated by Employee Decorator')
        self.decorated = decorated
        self.decorated.decorators[self.__doc__] = self

    def discount_check(self, a_check):
        for account in BankAccountDecorator.active_accounts:
            if account.number == a_check.account_number:
                if account.average_credit >= a_check.value:
                    account.average_credit -= a_check.value
                else:
                    raise InsuficientFunds("Insuficient Money")

    @classmethod
    @rule('association')
    def rule_should_contain_employee_decorator(self, decorated):
        ''' Decorated object should be already decorated by Employee '''
        decorated |should| be_decorated_by(EmployeeDecorator)


class InsuficientFunds(Exception):
    pass
