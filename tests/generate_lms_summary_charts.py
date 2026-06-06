import json
from collections import Counter
from pathlib import Path

import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
RESULTS_PATH = ROOT / "LMS_Test_Log_Results_NFR_Updated.json"
CHART_DIR = ROOT / "reports" / "summary_charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)

SEVERITY_BY_CASE = {
    "TC-02-002": "Fatal",
    "TC-05-004": "Fatal",
    "TC-06-005": "Fatal",
    "TC-10-001": "Fatal",
    "TC-10-009": "Fatal",
    "TC-11-002": "Fatal",
    "TC-11-008": "Fatal",
    "TC-12-001": "Fatal",
    "TC-12-007": "Fatal",
    "TC-12-010": "Fatal",
    "TC-04-003": "Major",
    "TC-04-004": "Major",
    "TC-07-002": "Major",
    "TC-07-003": "Major",
    "TC-07-006": "Major",
    "TC-08-003": "Major",
    "TC-08-004": "Major",
    "TC-08-005": "Major",
    "TC-10-004": "Major",
    "TC-10-006": "Major",
    "TC-11-003": "Major",
    "TC-12-002": "Major",
    "TC-12-005": "Major",
    "TC-05-003": "Minor",
    "TC-10-003": "Minor",
    "TC-10-008": "Minor",
    "TC-11-005": "Minor",
    "TC-11-006": "Minor",
    "TC-Q002": "Major",
    "TC-Q003": "Fatal",
    "TC-Q004": "Fatal",
}


def style_axis(ax):
    ax.grid(axis="y", color="#cfcfcf", linewidth=0.8)
    ax.set_axisbelow(True)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)


def label_bars(ax, bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            str(int(height)),
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 4),
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=9,
        )


def test_case_coverage(summary):
    labels = ["Total Test\nCases", "Test Cases\nPassed", "Test Cases\nFailed", "Not\nExecuted"]
    values = [summary["total"], summary["pass"], summary["fail"], summary["not_executed"]]
    colors = ["#111111", "#5A92D6", "#B9CEE8", "#8566A8"]

    fig, ax = plt.subplots(figsize=(7.2, 4.3), dpi=180)
    bars = ax.bar(labels, values, color=colors, width=0.58)
    label_bars(ax, bars)
    ax.set_title("Test Case Coverage - Iteration 1", fontsize=12, weight="bold")
    ax.set_ylabel("Number of Test Cases")
    ax.set_ylim(0, max(values) + 10)
    style_axis(ax)
    ax.legend(bars, labels, loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=False)
    fig.tight_layout()
    fig.savefig(CHART_DIR / "test_case_coverage.png", bbox_inches="tight")
    plt.close(fig)


def defect_severity(results):
    failed = [r for r in results if r["pass_fail"] == "Fail"]
    counts = Counter(SEVERITY_BY_CASE.get(r["test_case_id"], "Major") for r in failed)
    labels = ["Fatal", "Major", "Minor", "Total"]
    values = [counts["Fatal"], counts["Major"], counts["Minor"], len(failed)]
    colors = ["#111111", "#B9CEE8", "#A7C957", "#8566A8"]

    fig, ax = plt.subplots(figsize=(7.2, 4.3), dpi=180)
    bars = ax.bar(labels, values, color=colors, width=0.58)
    label_bars(ax, bars)
    ax.set_title("Defects Found by Severity - Iteration 1", fontsize=12, weight="bold")
    ax.set_ylabel("Number of Defects")
    ax.set_ylim(0, max(values) + 5)
    style_axis(ax)
    ax.legend(bars, labels, loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=False)
    fig.tight_layout()
    fig.savefig(CHART_DIR / "defect_severity.png", bbox_inches="tight")
    plt.close(fig)


def schedule_chart(summary):
    fig, ax = plt.subplots(figsize=(7.2, 2.6), dpi=180)
    labels = ["Planned", "Actual"]
    values = [summary["total"], summary["pass"] + summary["fail"] + summary["not_executed"]]
    colors = ["#B9CEE8", "#8566A8"]
    bars = ax.barh(labels, values, color=colors, height=0.38)
    for bar in bars:
        width = bar.get_width()
        ax.annotate(
            str(int(width)),
            xy=(width, bar.get_y() + bar.get_height() / 2),
            xytext=(6, 0),
            textcoords="offset points",
            va="center",
            fontsize=9,
        )
    ax.set_title("Testing Schedule Completion", fontsize=12, weight="bold")
    ax.set_xlabel("Number of Test Cases")
    ax.set_xlim(0, max(values) + 10)
    ax.grid(axis="x", color="#cfcfcf", linewidth=0.8)
    for spine in ["top", "right"]:
        ax.spines[spine].set_visible(False)
    fig.tight_layout()
    fig.savefig(CHART_DIR / "schedule_completion.png", bbox_inches="tight")
    plt.close(fig)


def function_status(results):
    counts = {}
    for row in results:
        feature = row["requirement_id"].replace("REQ-", "")
        counts.setdefault(feature, Counter())
        counts[feature][row["pass_fail"]] += 1

    features = sorted(counts)
    passed = [counts[f]["Pass"] for f in features]
    failed = [counts[f]["Fail"] for f in features]
    not_executed = [counts[f]["Not Executed"] for f in features]

    fig, ax = plt.subplots(figsize=(9.2, 4.8), dpi=180)
    x = range(len(features))
    ax.bar(x, passed, label="Pass", color="#5A92D6")
    ax.bar(x, failed, bottom=passed, label="Fail", color="#D66A61")
    bottoms = [p + f for p, f in zip(passed, failed)]
    ax.bar(x, not_executed, bottom=bottoms, label="Not Executed", color="#8566A8")
    ax.set_title("Test Result by Function", fontsize=12, weight="bold")
    ax.set_ylabel("Number of Test Cases")
    ax.set_xticks(list(x))
    ax.set_xticklabels(features, rotation=45, ha="right")
    style_axis(ax)
    ax.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=False)
    fig.tight_layout()
    fig.savefig(CHART_DIR / "function_status.png", bbox_inches="tight")
    plt.close(fig)


def main():
    data = json.loads(RESULTS_PATH.read_text(encoding="utf-8"))
    test_case_coverage(data["summary"])
    defect_severity(data["results"])
    schedule_chart(data["summary"])
    function_status(data["results"])
    print(f"Created charts in {CHART_DIR}")


if __name__ == "__main__":
    main()
