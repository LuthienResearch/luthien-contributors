from datetime import datetime

from agent.standup import TZ, next_run, standup_text


def at(y, m, d, hh, mm=0):
    return datetime(y, m, d, hh, mm, tzinfo=TZ)


def test_monday_before_post_time_runs_same_day():
    # Mon Oct 26 2026, 7am -> same day 8am
    assert next_run(at(2026, 10, 26, 7)) == at(2026, 10, 26, 8)


def test_monday_after_post_time_runs_next_monday():
    assert next_run(at(2026, 10, 26, 9)) == at(2026, 11, 2, 8)


def test_exactly_at_post_time_moves_on():
    assert next_run(at(2026, 10, 26, 8)) == at(2026, 11, 2, 8)


def test_midweek_skips_to_monday():
    # Wed Oct 21 -> Mon Oct 26
    assert next_run(at(2026, 10, 21, 7)) == at(2026, 10, 26, 8)


def test_weekend_skips_to_monday():
    assert next_run(at(2026, 10, 24, 12)) == at(2026, 10, 26, 8)


def test_text_has_date_and_questions():
    text = standup_text(at(2026, 10, 26, 8))
    assert "Mon Oct 26" in text
    assert "blocked on" in text
