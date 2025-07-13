# tests/test_core.py

def test_generate_activity_report_exists():
    from cam2text import generate_activity_report
    assert callable(generate_activity_report)
