#!/usr/bin/env python
# -*- codign: utf-8 -*-

from should_dsl import should
from domain.supportive.rule import rule
from domain.supportive.association_error import AssociationError
from domain.supportive.contract_matchers import be_decorated_by
from domain.base.decorator import Decorator
from bank_system.decorators.employee_decorator import EmployeeDecorator

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

    @classmethod
    @rule('association')
    def rule_should_contain_employee_decorator(self, decorated):
        ''' Decorated object should be already decorated by Employee '''
        decorated |should| be_decorated_by(EmployeeDecorator)
