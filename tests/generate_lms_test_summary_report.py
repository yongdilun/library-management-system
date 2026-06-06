import json
from collections import Counter
from datetime import datetime
from pathlib import Path

from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt


ROOT = Path(__file__).resolve().parents[1]
RESULTS_PATH = ROOT / "LMS_Test_Log_Results_NFR_Updated.json"
CHART_DIR = ROOT / "reports" / "summary_charts"
OUT_DOCX = ROOT / "LMS_Test_Summary_Report_Yong_Di_Lun.docx"
FALLBACK_DOCX = ROOT / "LMS_Test_Summary_Report_Yong_Di_Lun_NFR_Updated.docx"
OUT_MD = ROOT / "LMS_Test_Summary_Report_Yong_Di_Lun.md"
AUTHOR = "Yong Di Lun"

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

NFR_REQUIREMENTS = [
    ("REQ_Q001", "Reliability & Accuracy", "100% transactional accuracy for concurrent book reservations to prevent double-booking.", "Pass"),
    ("REQ_Q002", "Reliability & Accuracy", "Database foreign key constraints between User, Book, and Reservation records prevent orphaned records.", "Fail"),
    ("REQ_Q003", "Security", "Passwords are securely hashed and salted before database storage; plain text passwords are never saved.", "Fail"),
    ("REQ_Q004", "Security", "Client-to-server interactions use HTTPS/TLS 1.2 or higher.", "Fail"),
]


def shade(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def set_cell(cell, text, bold=False, size=8, align=None, fill=None):
    cell.text = ""
    if fill:
        shade(cell, fill)
    paragraph = cell.paragraphs[0]
    if align is not None:
        paragraph.alignment = align
    for idx, line in enumerate(str(text).split("\n")):
        if idx:
            paragraph.add_run().add_break()
        run = paragraph.add_run(line)
        run.bold = bold
        run.font.name = "Calibri"
        run.font.size = Pt(size)
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP


def set_para(paragraph, text, bold=False, size=8):
    paragraph.text = ""
    run = paragraph.add_run(text)
    run.bold = bold
    run.font.name = "Calibri"
    run.font.size = Pt(size)


def add_section_header(table, row_idx, text, colspan):
    merged = table.cell(row_idx, 0).merge(table.cell(row_idx, colspan - 1))
    set_cell(merged, text, bold=True, fill="A6A6A6")


def fmt_date(iso_value):
    return datetime.fromisoformat(iso_value).strftime("%d/%m/%Y")


def pct(numerator, denominator):
    if denominator == 0:
        return "0.00%"
    return f"{(numerator / denominator) * 100:.2f}%"


def failed_rows(data):
    return [row for row in data["results"] if row["pass_fail"] == "Fail"]


def add_title(doc):
    title = doc.add_heading("Test Summary Report", level=1)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER


def add_general_information(doc, data):
    table = doc.add_table(rows=5, cols=4)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    add_section_header(table, 0, "General Information", 4)
    set_cell(table.cell(1, 0), "Test Report Description", fill="D9D9D9")
    set_cell(
        table.cell(1, 1).merge(table.cell(1, 3)),
        "This Test Summary Report provides a summary of findings based on the Test Log and Test Incident Report for the Library Management System, including functional requirements F001 to F0012 and non-functional requirements REQ_Q001 to REQ_Q004.",
    )
    set_cell(table.cell(2, 0), "Version Author", fill="D9D9D9")
    set_cell(table.cell(2, 1), AUTHOR)
    set_cell(table.cell(2, 2), "Contact Number", fill="D9D9D9")
    set_cell(table.cell(2, 3), "-")
    set_cell(table.cell(3, 0), "Associated test plan reference", fill="D9D9D9")
    set_cell(table.cell(3, 1).merge(table.cell(3, 3)), "LMS_TP_1.0.0")
    set_cell(table.cell(4, 0), "Execution Date", fill="D9D9D9")
    set_cell(table.cell(4, 1).merge(table.cell(4, 3)), f"{fmt_date(data['start_time'])} to {fmt_date(data['end_time'])}")
    doc.add_paragraph("")


def add_summary(doc, data):
    summary = data["summary"]
    total = summary["total"]
    completed = summary["pass"] + summary["fail"] + summary["not_executed"]
    failed = failed_rows(data)

    table = doc.add_table(rows=8, cols=5)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    add_section_header(table, 0, "Summary", 5)
    add_section_header(table, 1, "Test Status Report Summary", 5)
    set_cell(table.cell(2, 0).merge(table.cell(2, 4)), "The status of the test are as follow:")
    headers = [
        "Number of Test Cases Planned to be Completed",
        "Number of Test Cases Remaining to be Executed",
        "Number of Test Cases Completed",
        "Number of Test Cases Passed",
        "Number of Test Cases Failed",
    ]
    values = [total, 0, completed, summary["pass"], summary["fail"]]
    for idx, header in enumerate(headers):
        set_cell(table.cell(3, idx), header, bold=True, fill="D9D9D9")
        set_cell(table.cell(4, idx), str(values[idx]))

    set_cell(table.cell(5, 0).merge(table.cell(5, 4)), "Current status of the Test Incident Report are as follow:")
    incident_headers = [
        "New\n(new incident introduced in current iteration)",
        "Open\n(incident discovered from previous test iteration that still pending to be resolved)",
        "Reject\n(incidents that were rejected after investigation because it cannot be categorised as incident)",
        "Resolved\n(incidents that have been confirmed resolved)",
        "Deferred\n(incidents that have been deferred)",
    ]
    incident_values = [len(failed), len(failed), 0, 0, 0]
    for idx, header in enumerate(incident_headers):
        set_cell(table.cell(6, idx), header, bold=True, fill="D9D9D9")
        set_cell(table.cell(7, idx), str(incident_values[idx]))

    note = doc.add_paragraph()
    set_para(note, "Note: The number of incidents is counted based on Test Incident ID and not based on Test Incident Report ID.")
    doc.add_paragraph("")


def add_incident_table(doc, data):
    failed = failed_rows(data)
    table = doc.add_table(rows=1, cols=5)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, header in enumerate(["Incident ID", "Test Case ID", "Severity", "Short Description", "Status"]):
        set_cell(table.cell(0, idx), header, bold=True, fill="D9D9D9")
    for row in failed:
        cells = table.add_row().cells
        severity = SEVERITY_BY_CASE.get(row["test_case_id"], "Major")
        set_cell(cells[0], row["incident_id"])
        set_cell(cells[1], row["test_case_id"])
        set_cell(cells[2], severity)
        set_cell(cells[3], row["remark"])
        set_cell(cells[4], "Open")
    doc.add_paragraph("")


def add_nfr_requirement_summary(doc):
    table = doc.add_table(rows=1, cols=4)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, header in enumerate(["Requirement ID", "Category", "Requirement Summary", "Test Result"]):
        set_cell(table.cell(0, idx), header, bold=True, fill="D9D9D9")
    for req_id, category, description, result in NFR_REQUIREMENTS:
        cells = table.add_row().cells
        for idx, value in enumerate([req_id, category, description, result]):
            set_cell(cells[idx], value)
    doc.add_paragraph("")


def add_references_and_plan(doc, data):
    refs = [
        "LMS_TP_1.0.0",
        "LMS_TDS_1.0.0",
        "LMS_TCS_1.0.0",
        "LMS_TPS_1.0.0",
        "LMS_TL_1.0.0",
        "LMS_TIR_1.0.0",
        "LMS_NFR_1.0.0",
    ]
    table = doc.add_table(rows=4, cols=1)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell(table.cell(0, 0), "Document references", bold=True, fill="D9D9D9")
    set_cell(table.cell(1, 0), "\n".join(f"- {ref}" for ref in refs))
    set_cell(table.cell(2, 0), "Changes from Plans", bold=True, fill="D9D9D9")
    set_cell(
        table.cell(3, 0),
        (
            "The test scope was updated to include four non-functional requirement test cases "
            "(REQ_Q001 to REQ_Q004). No application logic was changed. "
            f"All {data['summary']['total']} planned test cases have been completed. Refer to the updated charts and coverage table below."
        ),
    )
    doc.add_paragraph("")


def add_comprehensiveness(doc, data):
    summary = data["summary"]
    failed = failed_rows(data)
    severity_counts = Counter(SEVERITY_BY_CASE.get(row["test_case_id"], "Major") for row in failed)

    table = doc.add_table(rows=2, cols=1)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell(table.cell(0, 0), "Comprehensiveness assessment", bold=True, fill="D9D9D9")
    set_cell(
        table.cell(1, 0),
        (
            f"All {summary['total']} planned test cases were completed. "
            f"{summary['pass']} test cases passed ({pct(summary['pass'], summary['total'])}) and "
            f"{summary['fail']} test cases failed ({pct(summary['fail'], summary['total'])}). "
            f"The failed cases resulted in {len(failed)} open incidents: "
            f"{severity_counts['Fatal']} fatal, {severity_counts['Major']} major, and {severity_counts['Minor']} minor defects."
        ),
    )
    doc.add_paragraph("")

    for intro, image_name, width in [
        ("For the schedule adherence, refer to the diagram below:", "schedule_completion.png", 5.7),
        ("The Test Case coverage is shown as below:", "test_case_coverage.png", 5.9),
        ("The Test Case result by function is shown as below:", "function_status.png", 7.0),
        ("Below are the lists of defects found through testing, by severity:", "defect_severity.png", 5.9),
    ]:
        p = doc.add_paragraph()
        set_para(p, intro)
        doc.add_picture(str(CHART_DIR / image_name), width=Inches(width))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.LEFT

    note = doc.add_paragraph()
    set_para(
        note,
        "NOTE:\n"
        "- Incident having critical security, data integrity, or unhandled server-error impact = Fatal defect.\n"
        "- Incident having important business-rule or validation impact = Major defect.\n"
        "- Incident having display, message, or procedural impact = Minor defect.",
    )
    doc.add_paragraph("")


def add_coverage_table(doc, data):
    completion_date = fmt_date(data["end_time"])
    rows = [
        ("Test Plan", "100", completion_date),
        ("Test Design Specification", "100", completion_date),
        ("Test Case Specification", "100", completion_date),
        ("Test Procedure Specification", "100", completion_date),
        ("Test Log", "100", completion_date),
        ("Test Incident Report", "100", completion_date),
        ("Test Summary Report", "100", datetime.now().strftime("%d/%m/%Y")),
    ]
    table = doc.add_table(rows=1, cols=3)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, header in enumerate(["Test Documents", "% Completed", "Date of Completion"]):
        set_cell(table.cell(0, idx), header, bold=True, fill="D9D9D9")
    for row_data in rows:
        cells = table.add_row().cells
        for idx, value in enumerate(row_data):
            set_cell(cells[idx], value)
    doc.add_paragraph("")


def add_result_summary(doc, data):
    summary = data["summary"]
    failed = failed_rows(data)
    severity_counts = Counter(SEVERITY_BY_CASE.get(row["test_case_id"], "Major") for row in failed)

    sections = [
        (
            "Result Summary",
            (
                "The items tested were the Library Management System functional features F001 to F0012 and non-functional requirements REQ_Q001 to REQ_Q004.\n\n"
                f"{summary['total']} test cases were planned and executed. "
                f"{summary['pass']} test cases passed and {summary['fail']} test cases were recorded with incidents. "
                f"The pass rate is {pct(summary['pass'], summary['total'])}.\n\n"
                "For the four added non-functional test cases, REQ_Q001 passed while REQ_Q002, REQ_Q003, and REQ_Q004 failed. "
                f"{severity_counts['Fatal']} fatal incidents, {severity_counts['Major']} major incidents, and "
                f"{severity_counts['Minor']} minor incidents were found in this test iteration. "
                "All incidents remain open and should be corrected by the development team before release."
            ),
        ),
        (
            "Rationale for Decisions",
            (
                "Due to the existence of fatal and major defects at the end of the test iteration, "
                "the current LMS version is not recommended for release. Fatal defects include authentication, "
                "admin book management, update persistence, password storage, HTTPS/TLS protection, and unhandled database failure responses. "
                "The failed foreign-key integrity check is also a release risk because it allows orphaned reservation data."
            ),
        ),
        (
            "Conclusion and Recommendation Based on Test Result",
            (
                "Conclusion: The current version of the product is not fit for release until fatal and major defects are fixed.\n"
                "Recommendation: Fix failed authentication validation, profile/search/reservation rules, admin add/edit/delete flows, "
                "database error handling, foreign key integrity, password hashing/salting, and HTTPS/TLS protection. "
                "After correction, execute regression testing using the same automated test system."
            ),
        ),
    ]
    table = doc.add_table(rows=len(sections) * 2, cols=1)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, (title, body) in enumerate(sections):
        set_cell(table.cell(idx * 2, 0), title, bold=True, fill="D9D9D9")
        set_cell(table.cell(idx * 2 + 1, 0), body)
    doc.add_paragraph("")


def add_approvals(doc):
    table = doc.add_table(rows=6, cols=3)
    table.style = "Table Grid"
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_cell(table.cell(0, 0).merge(table.cell(0, 2)), "Approvals", bold=True, fill="A6A6A6")
    for idx, header in enumerate(["Name", "Job Title", "Signature"]):
        set_cell(table.cell(1, idx), header, bold=True, fill="D9D9D9")
    rows = [
        (f"Prepared By:\n{AUTHOR}", "Test Lead\nLMS Test Team", ""),
        ("Reviewed By:\nQA Manager", "Quality Assurance Team\nLMS Test Team", ""),
        ("Reviewed By:\nTest Manager", "Test Manager\nLMS Test Team", ""),
        ("Approved By:\nProject Manager", "Project Manager\nLMS Project", ""),
    ]
    for idx, row_data in enumerate(rows, 2):
        for col_idx, value in enumerate(row_data):
            set_cell(table.cell(idx, col_idx), value)


def build_markdown(data):
    summary = data["summary"]
    failed = failed_rows(data)
    severity_counts = Counter(SEVERITY_BY_CASE.get(row["test_case_id"], "Major") for row in failed)
    lines = [
        "# Test Summary Report",
        "",
        f"Version Author: {AUTHOR}",
        "Associated test plan reference: LMS_TP_1.0.0",
        "Scope: Functional requirements F001 to F0012 and non-functional requirements REQ_Q001 to REQ_Q004",
        "",
        "## Summary",
        "",
        f"- Planned test cases: {summary['total']}",
        "- Remaining test cases: 0",
        f"- Completed test cases: {summary['total']}",
        f"- Passed: {summary['pass']}",
        f"- Failed: {summary['fail']}",
        "- Not executed: 0",
        f"- Fatal defects: {severity_counts['Fatal']}",
        f"- Major defects: {severity_counts['Major']}",
        f"- Minor defects: {severity_counts['Minor']}",
        "",
        "## Non-Functional Requirement Results",
        "",
        "| Requirement ID | Category | Requirement Summary | Test Result |",
        "|---|---|---|---|",
    ]
    for req_id, category, description, result in NFR_REQUIREMENTS:
        lines.append(f"| {req_id} | {category} | {description} | {result} |")
    lines.extend(
        [
        "",
        "## Incidents",
        "",
        "| Incident ID | Test Case ID | Severity | Status | Description |",
        "|---|---|---|---|---|",
        ]
    )
    for row in failed:
        severity = SEVERITY_BY_CASE.get(row["test_case_id"], "Major")
        lines.append(f"| {row['incident_id']} | {row['test_case_id']} | {severity} | Open | {row['remark']} |")
    lines.extend(
        [
            "",
            "## Charts",
            "",
            f"![Schedule]({CHART_DIR / 'schedule_completion.png'})",
            f"![Coverage]({CHART_DIR / 'test_case_coverage.png'})",
            f"![Function Status]({CHART_DIR / 'function_status.png'})",
            f"![Defect Severity]({CHART_DIR / 'defect_severity.png'})",
        ]
    )
    OUT_MD.write_text("\n".join(str(line) for line in lines), encoding="utf-8")


def main():
    data = json.loads(RESULTS_PATH.read_text(encoding="utf-8"))
    doc = Document()
    section = doc.sections[0]
    section.orientation = WD_ORIENT.LANDSCAPE
    section.page_width, section.page_height = section.page_height, section.page_width
    section.top_margin = Inches(0.35)
    section.bottom_margin = Inches(0.35)
    section.left_margin = Inches(0.35)
    section.right_margin = Inches(0.35)
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(8)

    add_title(doc)
    add_general_information(doc, data)
    add_summary(doc, data)
    add_nfr_requirement_summary(doc)
    add_incident_table(doc, data)
    add_references_and_plan(doc, data)
    add_comprehensiveness(doc, data)
    add_coverage_table(doc, data)
    add_result_summary(doc, data)
    add_approvals(doc)
    timestamped_docx = ROOT / f"LMS_Test_Summary_Report_Yong_Di_Lun_NFR_Updated_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
    saved_docx = None
    for candidate in [OUT_DOCX, FALLBACK_DOCX, timestamped_docx]:
        try:
            doc.save(candidate)
            saved_docx = candidate
            break
        except PermissionError:
            continue
    if saved_docx is None:
        raise PermissionError("Unable to save the Test Summary Report DOCX because all candidate files are locked.")
    build_markdown(data)
    print(f"Created {saved_docx}")
    print(f"Created {OUT_MD}")


if __name__ == "__main__":
    main()
