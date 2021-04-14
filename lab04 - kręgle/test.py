import unittest
from address_main import format_addresses


class AddressTestCase(unittest.TestCase):
    def setUp(self):
        self.addresses = ['34-Czerwona', '23-Biala', '85 Pogodna']

    def test_address_in_list(self):
        first_address = format_addresses(self.addresses)[0]
        self.assertEqual(first_address, '34-Czerwona')

    def test_dash_in_address(self):
        all_addresses = format_addresses(self.addresses)
        for address in all_addresses:
            x = address.find('-') != -1
            self.assertTrue(x)

    def test_dash_not_in_address(self):
        all_addresses = format_addresses(self.addresses)
        for address in all_addresses:
            x = address.find('-') != -1
            self.assertFalse(x)





if __name__ == '__main__':
    unittest.main()
