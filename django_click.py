import os
import sublime, sublime_plugin
from utils import parse_tag


class DjangoClickCommand(sublime_plugin.TextCommand):
	TEMPLATE_DIR = 'templates'	

	def run(self, edit):
		region = self.view.sel()[0]
		line = self.view.line(region)
		line_contents = self.view.substr(line)

		tag, targets = parse_tag(line_contents)

		if tag:
			# get the base-path of current file
			base, current_file = self.view.file_name().split('%(separator)stemplates%(separator)s' % dict(separator=os.path.sep), 1)

			for one in targets:
				# get the target file path
				tar = os.path.join(base, self.TEMPLATE_DIR, one) 

				# open it!
				window = sublime.active_window()
				window.open_file(tar, sublime.ENCODED_POSITION)
