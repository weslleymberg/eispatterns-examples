import unittest
from should_dsl import should, should_not
from domain.supportive.association_error import AssociationError
from domain.node.person import Person
from bank_system.resources.loan_request import LoanRequest
from bank_system.decorators.bank_account_decorator import BankAccountDecorator
from bank_system.decorators.credit_analyst_decorator import CreditAnalystDecorator
from bank_system.decorators.client_decorator import ClientDecorator


class LoanRequestSpec(unittest.TestCase):

    def it_check_associations_with_bank_account_and_credit_analyst(self):
        a_client = Person()
        a_client_decorator = ClientDecorator()
        a_client_decorator.decorate(a_client)
        an_account = BankAccountDecorator(a_client, '12345-6')
        an_analyst = CreditAnalystDecorator('abcde-f')
        (LoanRequest, 'I am not an account', 123, an_analyst) |should| throw(AssociationError)
        (LoanRequest, an_account, 123, 'I am not an analyst') |should| throw(AssociationError)
        (LoanRequest, an_account, 123, an_analyst) |should_not| throw(AssociationError)

