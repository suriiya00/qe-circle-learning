

# Manual Testing - Test Cases

## Application

**Application:** Playwright Documentation Website\
**URL:** [https://playwright.dev/](<https://playwright.dev/>)

## Test Cases

| ID | Scenario | Expected Result | Actual Result | Status |
| --- | --- | --- | --- | --- |
| TC01 | Open homepage | Homepage loads successfully. | The Playwright website opened successfully, and the homepage body was visible. | Pass |
| TC02 | Verify page title | Page title contains "Playwright". | The page title contained "Playwright". | Pass |
| TC03 | Click Get started | Installation page opens. | Navigated to `https://playwright.dev/docs/intro`, and the Installation heading was visible. | Pass |
| TC04 | Verify Get started link | Link is visible and identifiable by its text. | The Get started link was visible and identifiable by its accessible name. | Pass |
| TC05 | Navigate to an unavailable page | Application returns an appropriate not-found response. | Navigated to `https://playwright.dev/nonexistent-learning-test-page`. The server returned HTTP status code `404 Not Found`. | Pass |

## Execution Notes

- Execute each test in the browser and record the actual behavior.
- Compare the observed result with the expected result before assigning a status.
- Mark a test as **Pass** only when the observed result meets the expected result.
- Mark a test as **Fail** when the observed result does not meet the expected result.
- Use **Pending Investigation** when more evidence is needed to determine the outcome.
- Record the exact error message, HTTP status code, or destination URL whenever relevant.
- Capture screenshots when useful as evidence of the observed behavior.

## Learning Outcomes

- Writing clear test scenarios.
- Defining expected results.
- Recording actual results accurately.
- Distinguishing pass, fail, and pending investigation.
- Verifying page titles, links, navigation, and error-page behavior.
- Evaluating test results using observed evidence instead of assumptions.
- Understanding HTTP status codes and validating not-found responses.

## Execution Summary

- **Total test cases:** 5
- **Passed:** 5
- **Failed:** 0
- **Pending investigation:** 0

## Scope and Limitations

This document is part of the QE Circle Learning Project.

The test cases are intended for learning manual testing fundamentals using the Playwright documentation website. All actual results and statuses should reflect observed behavior and verified evidence.

Execution Note: The latest run of tests/test_qe_basics.py completed successfully, with all five tests passing. TC05 verifies that the unavailable URL returns HTTP 404. The test results reflect this automated execution; manual execution evidence should be recorded separately when applicable.

