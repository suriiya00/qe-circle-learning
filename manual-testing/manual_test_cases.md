Manual Testing - Test Cases
Application

Playwright documentation website: https://playwright.dev/

Test Cases
ID	Scenario	Expected Result	Actual Result	Status
TC01	Open homepage	Homepage loads successfully	Browser opened the Playwright website, and the automated test execution succeeded.	Pass
TC02	Verify page title	Page title contains "Playwright"	Observed title: "Playwright enables reliable web automation for testing, scripting, and AI agents."	Pass
TC03	Click Get started	Installation page opens	Navigated to https://playwright.dev/docs/intro. The Installation heading was visible.	Pass
TC04	Verify Get started link	Link is visible and identifiable by its text	The Get started link was visible and identifiable by its text.	Pass
TC05	Navigate to an unavailable page	Application displays an appropriate not-found response	Browser displayed "This site can't be reached". Application not-found behavior has not been verified.	Pending Investigation
Execution Notes
Execute each test in the browser and record the actual behavior.
Compare the observed behavior with the expected result before assigning a status.
Mark a test as Pass only when the observed result meets the expected result.
Mark a test as Fail when the observed result does not meet the expected result.
Use Pending Investigation when more evidence is needed to determine the outcome.
Record the exact error message or destination URL whenever relevant.
Capture screenshots when useful as evidence of the observed behavior.
Learning Outcomes
Writing clear test scenarios.
Defining expected results.
Recording actual results accurately.
Distinguishing pass, fail, and pending investigation.
Verifying page titles, links, navigation, and error-page behavior.
Evaluating test results using observed evidence instead of assumptions.
Execution Summary
Total test cases: 5
Passed: 4
Failed: 0
Pending investigation: 1

Note: TC05 is not yet confirmed as Pass or Fail. Update the execution summary after investigating the browser connectivity error.

Scope and Limitations

This document is part of the QE Circle Learning Project.

The test cases are intended for learning manual testing fundamentals using the Playwright documentation website. All actual results and statuses should reflect observed behavior and verified evidence.
