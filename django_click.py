import sublime
import sublime_plugin

class DjangoClickCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		region = self.view.sel()[0]
		line = self.view.line(region)
		line_contents = self.view.substr(line)

		# get the clicked path
		wanted_file_shortpath = line_contents.replace('{% extends', '').replace('{% includeblocks', '').replace('{% include ', '').replace(' %}', '').replace("'", '').replace('\"', '').strip()

		# get the base-path of current file
		this_file_name = self.view.file_name().split('/templates/')

		# merge them - thats file path to open
		wanted_file_fullpath = this_file_name[0] + '/templates/' + wanted_file_shortpath
		# print 'Path to open: ', wanted_file_fullpath

		# open!
		window = sublime.active_window()
		window.open_file(wanted_file_fullpath, sublime.ENCODED_POSITION)
