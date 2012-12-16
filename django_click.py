import re, os

import sublime, sublime_plugin

class DjangoClickCommand(sublime_plugin.TextCommand):
	RE_BLOCK = re.compile(r'{%%\s+(?P<tag>%s)\s+[\'"]?(?P<name>[/\.\-_a-zA-Z0-9]+)[\'"]?\s+%%}' % 
        	'|'.join(['include', 'extends', 'includeblocks']))
	TEMPLATE_DIR = 'templates'
	
	def run(self, edit):
		region = self.view.sel()[0]
		line = self.view.line(region)
		line_contents = self.view.substr(line)

		match = re.match(self.RE_BLOCK, line_contents)
		
		#is it the tag line we support?
		if match:
			tag, target =  match.groupdict()['tag'], match.groupdict()['name']

			# get the base-path of current file
			base, current_file = self.view.file_name().split('%(separator)stemplates%(separator)s' % dict(separator=os.path.sep))

			# get the target file path
			tar = os.path.join(base, self.TEMPLATE_DIR, target)

			# open it!
			window = sublime.active_window()
			window.open_file(tar, sublime.ENCODED_POSITION)