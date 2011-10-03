#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should_dsl import should, ShouldNotSatisfied
from domain.base.decorator import Decorator
from domain.node.machine import Machine
from domain.resource.operation import operation
from domain.supportive.association_error import AssociationError
from bank_system.decorators.client_decorator import ClientDecorator
from bank_system.rules.bank_system_rule_manager import BankSystemRuleManager

class BankAccountDecorator(Decorator):
    '''Bank Account'''

    active_accounts = []

    decoration_rules = ['should_be_instance_of_machine']

    def __init__(self, client, number):
        Decorator.__init__(self)
        self.description = "A bank account"
        #log area for already processed resources
        self.log_area = {}
        #should it mask Machine.tag? decorated.tag = number?
        self.number = number
        self.balance = 0
        self.restricted = False
        self.average_credit = 0
        try:
            BankAccountDecorator.rule_should_contain_client_decorator(client)
        except:
            raise AssociationError('Client must be decorated by ClientDecorator previously')
        self.client = client

    def decorate(self, decorated):
        try:
            BankAccountDecorator.rule_should_be_machine_instance(decorated)
        except:
            raise AssociationError('Machine instance expected, instead %s passed' % type(decorated))
        self.decorated = decorated
        self.decorated.decorate(self)
        BankAccountDecorator.active_accounts.append(self)

    @operation(category = 'business')
    def deposit(self, value):
        ''' Makes a banking deposit '''
        self.average_credit += value

    @operation(category = 'business')
    def draw(self, value):
        ''' Makes a banking draw '''
        self.average_credit -= value

    @classmethod
    #@rule('association')
    def rule_should_be_machine_instance(self, decorated):
        ''' Decorated object should be a Machine '''
        decorated |should| be_instance_of(Machine)

    @operation(category='business')
    def register_credit(self, value):
        ''' Register a credit in the balance '''
        self.balance += value

    @operation(category='business')
    def send_message_to_account_holder(self, message):
        ''' Sends a message to the account holder '''
        return message

    @classmethod
    #@rule('association')
    def rule_should_contain_client_decorator(self, client):
        ''' Client object must contain ClientDecorator '''
        client.decorators |should| contain(ClientDecorator.__doc__)
