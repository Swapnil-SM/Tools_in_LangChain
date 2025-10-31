from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

results = search_tool.invoke('top news in india today')

#print(results)

print(search_tool.name)
print(search_tool.description)
print(search_tool.args)


## Built-in Tool - Shell Tool

from langchain_community.tools import ShellTool

shell_tool = ShellTool()

results = shell_tool.invoke('ls') #it runs the shell command 'ls' to list directory contents

print(results)