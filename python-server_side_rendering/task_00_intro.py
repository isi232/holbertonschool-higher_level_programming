#!/usr/bin/python3
"""
task_00_intro.py

A simple templating program that generates personalized invitation
files from a template string and a list of attendee dictionaries.

Usage:
    from task_00_intro import generate_invitations
    generate_invitations(template_content, attendees)
"""
import logging

# Basic logging configuration: prints level + message, e.g. "ERROR: ..."
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# The set of placeholders the template is expected to support.
PLACEHOLDERS = ["name", "event_title", "event_date", "event_location"]


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list
    of attendee data.

    Args:
        template (str): The invitation template containing placeholders
            in the form {name}, {event_title}, {event_date}, and
            {event_location}.
        attendees (list): A list of dictionaries, where each dictionary
            holds the data for a single attendee.

    Behavior:
        - Validates that `template` is a string and `attendees` is a
          list of dictionaries. Logs an error and returns early if not.
        - Logs an error and returns early if the template is empty.
        - Logs an error and returns early if the attendees list is empty.
        - For each attendee, replaces placeholders in the template with
          the attendee's data. Missing or None values are replaced with
          "N/A".
        - Writes each processed template to a file named
          `output_X.txt`, where X is the 1-based index of the attendee.

    Returns:
        None
    """
    # --- Type validation -------------------------------------------------
    if not isinstance(template, str):
        logging.error(
            "Invalid input: 'template' must be a string, got {}.".format(
                type(template).__name__
            )
        )
        return

    if not isinstance(attendees, list) or not all(
        isinstance(attendee, dict) for attendee in attendees
    ):
        logging.error(
            "Invalid input: 'attendees' must be a list of dictionaries."
        )
        return

    # --- Empty input validation -------------------------------------------
    if template == "":
        logging.error("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        logging.error("No data provided, no output files generated.")
        return

    # --- Process each attendee --------------------------------------------
    for index, attendee in enumerate(attendees, start=1):
        content = template

        for placeholder in PLACEHOLDERS:
            value = attendee.get(placeholder)
            if value is None or value == "":
                value = "N/A"
            content = content.replace("{" + placeholder + "}", str(value))

        filename = "output_{}.txt".format(index)
        try:
            with open(filename, "w") as output_file:
                output_file.write(content)
            logging.info("Generated {}".format(filename))
        except OSError as error:
            logging.error(
                "Failed to write file '{}': {}".format(filename, error)
            )
