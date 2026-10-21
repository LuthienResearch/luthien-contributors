from datetime import datetime

from agent.standup import TZ, next_run, standup_text


def at(y, m, d, hh, mm=0):
    return datetime(y, m, d, hh, mm, tzinfo=TZ)


def test_before_post_time_runs_same_day():
    # Wed Oct 21 2026, 7am -> same day 8am
    assert next_run(at(2026, 10, 21, 7)) == at(2026, 10, 21, 8)


def test_after_post_time_runs_next_day():
    assert next_run(at(2026, 10, 21, 9)) == at(2026, 10, 22, 8)


def test_exactly_at_post_time_moves_on():
    assert next_run(at(2026, 10, 21, 8)) == at(2026, 10, 22, 8)


def test_friday_evening_skips_to_monday():
    # Fri Oct 23 -> Mon Oct 26
    assert next_run(at(2026, 10, 23, 17)) == at(2026, 10, 26, 8)


def test_weekend_skips_to_monday():
    assert next_run(at(2026, 10, 24, 12)) == at(2026, 10, 26, 8)


def test_text_has_date_and_questions():
    text = standup_text(at(2026, 10, 22, 8))
    assert "Thu Oct 22" in text
    assert "blocked on" in text
