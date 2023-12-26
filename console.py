#!/usr/bin/python3
""" Contains the entry point of the command interpreter """
import cmd



class HBNBCommand(cmd.Cmd):
    """ Entry point of the command interpreter """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """ Method called when an empty line is
            entered in response to the prompt
        """
        return

    def do_EOF(self, line):
        """ Exits the command interpreter through keyboard interruption """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()



