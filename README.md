# Tony-homework-api
Test Case 1: Get all devices

Test Case ID: TC1
Title: Verify all devices are listed
Pre-conditions: API server is running and have devices
Test Steps:
Send a GET request to /inventory/devices
Verify the response status is 200 OK
Verify the response body contains the expected list of devices
Expected Result:
Status code: 200
Response body contains device information with fields like id, ipAddress, model, serialNum, version, etc.





Test Case 2: Get a single device by ID

Test Case ID: TC2
Title: Verify searching device by ID is listed
Pre-conditions: API server is running, and a device with id TEST1 exists
Test Steps:
Send a GET request to /inventory/devices/TEST1
Verify the response status is 200 OK
Verify the response body contains the correct device details for TEST1
Expected Result:
Status code: 200
Response body matches the details of the device with id TEST1







Test Case 3: Attempt to get a device that does not exist

Test Case ID: TC3
Title: Verify error handling when a non-existent device is searching
Pre-conditions: API server is running
Test Steps:
Send a GET request to /inventory/devices/NON_EXISTING_DEVICE
Verify the response status is 404 Not Found
Expected Result:
Status code: 404
Response body contains an error message indicating the device does not exist







Test Case 4: Add a new device (missing required field)

Test Case ID: TC4
Title: Verify handling missing required fields when adding a device
Pre-conditions: API server is running
Test Steps:
Send a POST request to /inventory/devices with the following body (missing model):
{
  "id": "TEST4",
  "ipAddress": "10.0.49.143",
  "deviceAddresses": {
    "fqdn": "test4.com",
    "ipv4Address": "10.0.49.143",
    "ipv6Address": "2001:0db8:85a3:0000:0000:8a2e:0370:7335"
  },
  "serialNum": "TEST4-1abc5678",
  "version": "4.1.0",
  "build": "20240410.2025-8f4e21abc"
}
Verify the response status is 400 Bad Request
Verify the response body contains an error message indicating the missing model field
Expected Result:
Status code: 400
Response body contains an error message about the missing field


Test Case 5: Attempt to update a non-existent device

Test Case ID: TC5
Title: Verify error handling when updating a non-existent device
Pre-conditions: API server is running
Test Steps:
Send a PUT request to /inventory/devices/UNKNOWN_ID with any valid body
Verify the response status is 404 Not Found
Expected Result:
Status code: 404
Response body contains an error message indicating the device does not exist

