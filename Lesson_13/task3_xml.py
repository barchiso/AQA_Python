"""Create search function for XML files.

For the ideas_for_test/work_with_xml/groups.xml file,
create a group/number search function and return the timingExbytes/incoming
value, output the result to the console through the logger at the info level.
"""
from pathlib import Path

# Additional Installation Instructions
# Install 'defusedxml' for safe XML parsing:
# https://pypi.org/project/defusedxml/
# pip install defusedxml
from defusedxml.ElementTree import ParseError, parse

from logger import configure_logging

_log = configure_logging(log_file='xml_result.log')


def group_number_search(xml_file_path):
    """Find all group/number and return the timingExbytes/incoming value.

    Args:
        xml_file_path (str): Path to the XML file.

    Returns:
        str: Path to the XML file.
    """
    try:
        # Parse the XML file
        tree = parse(xml_file_path)
        root = tree.getroot()

        # Find all 'group' elements with a 'number' child
        for group in root.findall('.//group'):
            number = group.find('number')
            timing_exbytes = group.find('.//timingExbytes/incoming')

            # Check if 'number' and 'timingExbytes/incoming' exist
            if number is not None and timing_exbytes is not None:
                # Log the group number and the timingExbytes/incoming value
                message = (f'Group: {number.text}, '
                           f'timingExbytes/incoming: {timing_exbytes.text}')
                _log.info(message)

    except ParseError as xml_error:
        # Specific handling for XML syntax errors
        error = f'XML parsing error in file {xml_file_path}: {xml_error}'
        _log.error(error)
    except FileNotFoundError:
        # Handling when file is not found
        error = f'Error: The XML file not found: {xml_file_path}'
        _log.error(error)
    except Exception as e:
        # Catch-all for other unexpected errors
        error = f'Unexpected error occurred with file {xml_file_path}: {e}'
        _log.error(error)

    return xml_file_path


# Path to the XML file
xml_path = Path('ideas_for_test/work_with_xml/groups.xml')

# Run the function
group_number_search(xml_path)
