#!/usr/bin/python3
"""Main file to test generate_invitations from task_00_intro.py"""
from task_00_intro import generate_invitations

# Read the template from a file
with open('template.txt', 'r') as file:
    template_content = file.read()

# List of attendees
attendees = [
    {"name": "Alice", "event_title": "Python Conference",
     "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop",
     "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit",
     "event_date": None, "event_location": "Boston"},
]

print("=== Normal case ===")
generate_invitations(template_content, attendees)

print("\n=== Empty template ===")
generate_invitations("", attendees)

print("\n=== Empty attendees list ===")
generate_invitations(template_content, [])

print("\n=== Invalid template type ===")
generate_invitations(12345, attendees)

print("\n=== Invalid attendees type (not a list of dicts) ===")
generate_invitations(template_content, ["Alice", "Bob"])

print("\n=== Attendee missing a key entirely ===")
generate_invitations(template_content, [{"name": "Dana"}])
