import os

def configure(self):
	self.addLinkFile("~/.gitignore_global", "gitignore_global")
	self.appendToConfig("~/.gitconfig", "gitconfig")

