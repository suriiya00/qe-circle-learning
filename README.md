QE Circle Learning Project
1. Overview

This repository documents my hands-on learning and upskilling in Quality Engineering (QE), focusing on manual testing, Python programming, UI test automation, and test reporting.

The project demonstrates practical application of testing concepts through manual test cases, automated test scripts, execution verification, and Allure reporting.

2. Learning Areas
Manual Testing and Test Case Design
UI Automation Testing using Playwright with Python
Python Fundamentals for Test Automation
pytest Test Execution and Assertions
Allure Test Reporting
AAVA Introductory Learning and Workflow Exploration
3. Project Structure
text
qe-circle-learning/
├── tests/
│   ├── test_qe_basics.py
│   ├── test_saucedemo_login.py
│   ├── test_saucedemo_inventory_validation.py
│   └── test_saucedemo_checkout.py
├── manual-testing/
│   └── manual_test_cases.md
├── python-exercises/
│   └── test_result_summary.py
├── aava-learning/
├── evidence/
├── test_scenarios.md
├── README.md
└── requirements.txt


Note: Update the structure above if your actual repository differs.

4. Technologies and Tools
Python
pytest
Playwright for Python
Chromium
Allure Report
Git and GitHub
5. Environment Setup

Create and activate a Python virtual environment.

Windows PowerShell
powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1


Install the dependencies:

powershell
python -m pip install -r requirements.txt
python -m playwright install chromium


If requirements.txt is not yet available, install the required packages:

powershell
python -m pip install pytest pytest-playwright allure-pytest

6. Test Execution

Run all automated tests:

powershell
python -m pytest -v


Generate Allure results while executing the tests:

powershell
python -m pytest -v --alluredir=allure-results


Open the Allure report:

powershell
allure serve allure-results


The Allure command requires the Allure command-line tool to be installed and available in PATH.

7. Automation Coverage
Playwright Documentation Website
Homepage loading validation
Page title verification
Get Started navigation
Link visibility validation
HTTP 404 response verification for an unavailable page
SauceDemo Application
Login page element validation
Successful login validation
Invalid password validation
Empty username validation
Locked-out user validation
Inventory product count validation
Product price and image visibility
Product sorting in ascending and descending price order
Add-to-cart validation
Remove-from-cart validation
Checkout form validation
Complete checkout flow validation
8. Manual Testing

Manual testing documentation is maintained in manual-testing/manual_test_cases.md.

The common scenario document, test_scenarios.md, connects test objectives, manual execution steps, expected results, and corresponding automation references.

9. Execution Status

The latest recorded automated execution completed with:

Passed: 20
Warnings: 1

These results represent the recorded test run. Review the warning and retain the latest execution output as evidence.

10. Test Reporting

Allure reporting is configured to generate a consolidated report from automated test results.

The report helps review test execution outcomes, including passed and failed tests, and provides a convenient summary of the test run.

Generated Allure result files are local execution artifacts and should not be committed unless there is a specific requirement to retain them.

11. Learning Outcomes

Through this project, I have gained practical experience in:

Writing and organizing manual test cases
Designing test scenarios with expected results
Using Playwright locators and browser interactions
Writing assertions with pytest and Playwright
Automating positive and negative login scenarios
Validating inventory, cart, and checkout workflows
Executing and debugging automated tests
Generating and reviewing Allure test reports
Practicing Python functions and data structures
Maintaining structured QA documentation
12. Scope and Limitations

This is a learning project developed to demonstrate foundational Quality Engineering and UI automation skills. It is not intended to be a production-ready automation framework.

Execution results and learning outcomes are documented according to completed activities and observed test evidence.

13. Future Improvements
Add screenshots and other relevant execution evidence
Review and resolve the remaining test warning
Improve test configuration and reusable fixtures
Explore CI execution through GitHub Actions
Expand negative and edge-case test coverage
