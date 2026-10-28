
def summarize_results(results):
    total = len(results)
    passed = results.count("PASS")
    failed = results.count("FAIL")

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
    }


if __name__ == "__main__":
    sample_results = ["PASS", "PASS", "FAIL", "PASS"]
    summary = summarize_results(sample_results)

    print(summary)

    assert summary["total"] == 4
    assert summary["passed"] == 3
    assert summary["failed"] == 1
