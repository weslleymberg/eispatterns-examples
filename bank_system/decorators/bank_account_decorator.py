#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should_dsl import should, ShouldNotSatisfied
from domain.base.decorator import Decorator
from domain.node.machine import Machine
from domain.resource.operation import operation
from domain.supportive.association_error import AssociationError
from bank_system.decorators.client_decorator import ClientDecorator

class BankAccountDecorator(Decorator):
    '''Bank Account'''

    decoration_rules = ['should_be_instance_of_machine']

    active_accounts = []

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
        client |should| be_decorated_by(ClientDecorator)
        self.client = client
        BankAccountDecorator.active_accounts.append(self)

    @operation(category = 'business')
    def deposit(self, value):
        ''' Makes a banking deposit '''
        self.average_credit += value

    @operation(category = 'business')
    def draw(self, value):
        ''' Makes a banking draw '''
        self.average_credit -= value

    @operation(category='business')
    def register_credit(self, value):
        ''' Register a credit in the balance '''
        self.balance += value

    @operation(category='business')
    def send_message_to_account_holder(self, message):
        ''' Sends a message to the account holder '''
        return message
