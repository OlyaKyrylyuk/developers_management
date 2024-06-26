from odoo.tests.common import TransactionCase
from psycopg2.errors import UniqueViolation
from odoo.tools import mute_logger


class DeveloperCreate(TransactionCase):

    def setUp(self):
        super(DeveloperCreate, self).setUp()
        self.Developer = self.env['developer']

    def test_create_developer(self):
        developer = self.Developer.create({
            'name': 'Olha Test',
            'type': 'back-end',
            'email': 'olha@test.com',
            'phone': '0000000000',
        })
        self.assertTrue(developer)
        self.assertEqual(developer.global_identification, 'Olha Test-back-end')

    @mute_logger('odoo.sql_db')
    def test_create_duplicate_developer(self):
        self.Developer.create({
            'name': 'Olha Test1',
            'type': 'back-end',
            'email': 'olha@test.com',
            'phone': '0000000000',
            'address': '456 Street',
            'birth_date': '2000-04-15',
        })

        with self.assertRaises(UniqueViolation):
            self.Developer.create({
                'name': 'Olha Test1',
                'type': 'front-end',
                'email': 'olha2@test.com',
                'phone': '1111111111',
                'address': '456 Street',
                'birth_date': '2000-04-15',
            })

    def test_create_company_and_developer(self):
        company = self.env['company'].create({
            'name': 'Comp',
            'address': '123 Street',
        })
        self.assertTrue(company, "Company is not saved")

        developer = self.env['developer'].create({
            'name': 'Olha Test2',
            'type': 'front-end',
            'email': 'olha2@test.com',
            'phone': '1111111111',
            'address': '456 Street',
            'birth_date': '2000-04-15',
            'company_id': company.id
        })
        self.assertTrue(developer, "Developer is not saved")

        self.assertEqual(developer.company_id.id, company.id, "Developer is not correctly linked to the company")
