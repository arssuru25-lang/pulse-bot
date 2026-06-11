from datetime import date

from quote import get_quote

from weather import get_weather


def build_summary():

    today = date.today()

    summary = f"""
=========================
PULSE DAILY SUMMARY
{today}
=========================

WEATHER
{get_weather()}

TODAY'S QUOTE
{get_quote()}

=========================
"""

    return summary


print(build_summary())
summary = build_summary()

with open("daily_summary.txt", "w") as f:
    f.write(summary)

print("Pulse ran successfully")