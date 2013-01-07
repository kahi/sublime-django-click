import re

def parse_tag(line):
    """
        parses include|extends and similar tags and returns (tag_name, targets) tuple
    """

    RE_BLOCK = re.compile(r'.*{%%\s*(?P<tag>%s)\s+(?P<names>.+)?[\'"]?\s*%%}' %
            '|'.join(['include', 'extends', 'includeblocks']))
    RE_NAMES = re.compile(r'[\'"]([/\.\-_a-zA-Z0-9\s]+)[\'"]')

    match = re.match(RE_BLOCK, line)

    if match:
        targets = re.findall(RE_NAMES, match.groupdict()['names'])
        return match.groupdict()['tag'], targets

    return None, []






