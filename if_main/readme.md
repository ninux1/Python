1) whenever we run the python file directly it sets the variable __name__ to __main__ always.
2) If any python module is imported and not directly run then __name__ in the imported module is not set to __main__
3) In a way __name__ == '__main__' indicates the module being directly invoked and not imported.
