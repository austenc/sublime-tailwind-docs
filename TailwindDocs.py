import sublime_plugin
import webbrowser


class TailwindDocsCommand(sublime_plugin.WindowCommand):
    def run(self, page=''):
        # open a new page
        url = 'https://tailwindcss.com/docs/'
        if(page != ''):
            url = url + page
            webbrowser.open_new_tab(url)
