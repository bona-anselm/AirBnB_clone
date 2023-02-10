#!/usr/bin/python3
""" Creates the class HBNBCommand(cmd.Cmd) """

import cmd

class HBNBCommand(cmd.Cmd):
    """ Defines class which is the entry point of the command interpreter    """
    prompt = "(hbnb) "


    def do_quit(self, args):
        """ Command to exit the console """
        return True

    def do_EOF(self, args):
        """Exit the interpreter on EOF (Ctrl + D)"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
