#!/usr/bin/env python
# -*- coding: utf-8 -*-

from should_dsl import should
from domain.base.decorator import Decorator
from domain.node.person import Person
from domain.resource.operation import operation
from domain.supportive.rule import rule
from domain.supportive.association_error import AssociationError


class ClientDecorator(Decorator):
    '''A general porpuse Client decorator'''

    decoration_rules = ['should_be_instance_of_person']

    def __init__(self):
        Decorator.__init__(self)
        self.description = "Supplies the basis for representing clients"
        self.accounts = []

    def generate_register(self, register):
        ''' generates the register number for the client'''
        self.register = register

