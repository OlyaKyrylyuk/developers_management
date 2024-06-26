from odoo.tests.common import TransactionCase


class CompanyCreate(TransactionCase):

    def setUp(self):
        super(CompanyCreate, self).setUp()
        self.Company = self.env['company']

    def test_create_company(self):
        company = self.Company.create({
            'name': 'Company Test',
            'address': 'Address Test',
        })
        self.assertTrue(company)
