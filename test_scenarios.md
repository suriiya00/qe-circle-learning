That's a good approach for your QE Circle Learning Project. Instead of repeating the same scenarios in separate documents, we'll create one file that connects manual testing steps with their corresponding Playwright automation steps.

We'll keep your existing files and use the new file as a common reference for both types of testing.

## Step 1 — Create `test_scenarios.md`

Create this file in your project root:

text

```
QE-Circle-Learning-Project/
├── README.md
├── tests/
│   └── test_qe_basics.py
├── manual-testing/
│   └── manual_test_cases.md
└── test_scenarios.md
```

## Step 2 — Add this initial content

Start with the five scenarios you have already implemented. Here's a reusable format for each scenario.

Writing

# QE Circle Learning Project — Test Scenarios

## 1\. Purpose

This document defines the common test scenarios used for manual testing and Playwright automation in the QE Circle Learning Project.

Each scenario includes manual execution steps, expected results, and the corresponding automation implementation.

## 2\. Application Under Test

- **Application:** Playwright Documentation Website
- **Base URL:** [https://playwright.dev/](<https://playwright.dev/>)
- **Automation Tool:** Playwright with Python
- **Test Framework:** pytest

## 3\. Test Scenarios

### TS01 — Open Homepage

**Objective:** Verify that the Playwright homepage loads successfully.

**Manual Testing Steps:**

1. Open a web browser.
2. Navigate to [https://playwright.dev/](<https://playwright.dev/>).
3. Wait for the page to load.
4. Verify that the homepage body is visible.

**Expected Result:** The homepage loads successfully and its body is visible.

**Automation Reference:** `tests/test_qe_basics.py` — `test_homepage_loads`

**Automation Check:** Navigate to the homepage and assert that the body is visible.

---

### TS02 — Verify Homepage Title

**Objective:** Verify that the homepage title contains the expected product name.

**Manual Testing Steps:**

1. Open a web browser.
2. Navigate to [https://playwright.dev/](<https://playwright.dev/>).
3. Observe the browser tab title.
4. Verify that the title contains "Playwright".

**Expected Result:** The page title contains "Playwright".

**Automation Reference:** `tests/test_qe_basics.py` — `test_homepage_title`

**Automation Check:** Assert that the page title matches a regular expression containing "Playwright".

---

### TS03 — Get Started Navigation

**Objective:** Verify that the Get started link opens the installation documentation.

**Manual Testing Steps:**

1. Open a web browser.
2. Navigate to [https://playwright.dev/](<https://playwright.dev/>).
3. Click the Get started link.
4. Verify that the destination URL is [https://playwright.dev/docs/intro](<https://playwright.dev/docs/intro>).
5. Verify that the Installation heading is visible.

**Expected Result:** The installation documentation opens at the expected URL, and the Installation heading is visible.

**Automation Reference:** `tests/test_qe_basics.py` — `test_get_started_navigation`

**Automation Check:** Click the link and assert the destination URL and heading visibility.

---

### TS04 — Verify Get Started Link

**Objective:** Verify that the Get started link is visible and identifiable by its accessible name.

**Manual Testing Steps:**

1. Open a web browser.
2. Navigate to [https://playwright.dev/](<https://playwright.dev/>).
3. Locate the Get started link.
4. Verify that the link is visible and its text identifies its purpose.

**Expected Result:** The Get started link is visible and identifiable by its accessible name.

**Automation Reference:** `tests/test_qe_basics.py` — `test_get_started_link_is_visible`

**Automation Check:** Locate the link by role and accessible name, then assert that it is visible.

---

### TS05 — Navigate to an Unavailable Page

**Objective:** Verify that the application returns HTTP 404 for a nonexistent page.

**Manual Testing Steps:**

1. Open a web browser.
2. Navigate to https://playwright.dev/nonexistent-learning-test-page.
3. Observe the response or not-found page.
4. Verify the HTTP response status using suitable browser developer tools or other approved evidence.

**Expected Result:** The request returns HTTP 404 Not Found.

**Automation Reference:** `tests/test_qe_basics.py` — `test_unavailable_page_behavior`

**Automation Check:** Capture the navigation response and assert that its status code is 404.

**Important:** A browser message such as "This site can't be reached" does not by itself prove an HTTP 404 response. Verify the status code before recording this expected result as satisfied.

---

## 4\. Execution and Evidence

For each scenario, record:

- Execution date
- Execution type: Manual or Automated
- Actual result
- Status: Pass, Fail, or Pending Investigation
- Evidence, when applicable

Manual and automated results must be recorded separately when they come from separate executions.

## 5\. Scope

This document covers foundational UI testing concepts using the Playwright documentation website. It is a learning document, not a production test specification.


