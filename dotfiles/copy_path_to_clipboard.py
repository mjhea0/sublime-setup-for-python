import sublime
import sublime_plugin


class CopyPathToClipboard(sublime_plugin.TextCommand):

    def run(self, edit):
        line_number, column = self.view.rowcol(self.view.sel()[0].begin())
        line_number += 1
        sublime.set_clipboard(self.view.file_name() + ':' + str(line_number))
