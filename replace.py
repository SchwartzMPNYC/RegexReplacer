import sublime
import sublime_plugin

regex_strings = {'styles':' style=".*?"', 'tables':'</?(table|tbody|thead|tr|td).*?>'}

class EraseAllTypesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for regex_str in regex_strings:
			Erase.erase(self.view, edit, regex_strings[regex_str])

class EraseAllTableTypesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		Erase.erase(self.view, edit, regex_strings['tables'])

class EraseAllInlineStylesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		Erase.erase(self.view, edit, regex_strings['styles'])


class EraseInputCommand(sublime_plugin.TextCommand):
	def run(self, edit, text):
		self.input(text)
		Erase.erase(self.view, edit, text)

	def input(self, text):
		return sublime_plugin.TextInputHandler()

class Erase():
	def erase(view, edit, to_match):
		offset = 0
		for match in view.find_all(to_match):
			view.erase(edit, sublime.Region(match.a-offset, match.b-offset))
			offset += match.size()
		