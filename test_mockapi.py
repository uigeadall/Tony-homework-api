import unittest
import requests


class TestAPI(unittest.TestCase):
    base_url = "http://localhost:8080/inventory/devices"

    def test_get_devices_success(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('body', data)
        self.assertTrue(len(data['body']) > 0)
        self.assertIn('id', data['body'][0])
        self.assertIn('model', data['body'][0])

    def test_get_device_by_id_success(self):
        device_id = "TEST1"
        response = requests.get(f"{self.base_url}/{device_id}")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['id'], device_id)
        self.assertIn('model', data)

    def test_get_device_not_found(self):
        device_id = "NON_EXISTING_DEVICE"
        response = requests.get(f"{self.base_url}/{device_id}")
        self.assertEqual(response.status_code, 404)

    def test_add_device_success(self):
        new_device = {
            "id": "TEST3",
            "ipAddress": "10.0.49.142",
            "deviceAddresses": {
                "fqdn": "newdevice.com",
                "ipv4Address": "10.0.49.142",
                "ipv6Address": None
            },
            "model": "NEW_DEVICE",
            "serialNum": "TEST3-1ghfaf6a-1234-56d1-7890-abcd1234xyz",
            "version": "1.0.0",
            "build": "20240501.1200-xyz123"
        }
        response = requests.post(self.base_url, json=new_device)
        self.assertEqual(response.status_code, 201)
        data = response.json()
        self.assertEqual(data['id'], new_device['id'])
        self.assertEqual(data['model'], new_device['model'])


if __name__ == '__main__':
    unittest.main()
