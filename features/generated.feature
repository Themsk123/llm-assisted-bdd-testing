Feature: Auto Generated
Scenario: Successful login and submission
Given user is on login page
When user login with valid credentials
And user submit application
Then application should be submitted successfully

