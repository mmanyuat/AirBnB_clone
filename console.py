#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) " # Custom prompt

    _classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }
    my_command = ['create', 'show', 'destroy', 'all', 'update', 'count']

    def userinput(self, arg):
        if '.' in arg and '(' in arg and ')' in arg:
            dot = arg.split('.')
            f_bracket = dot[1].split('(')
            s_brackets = f_bracket[1].split(')')
            if dot[0] in HBNBCommand._classes and f_bracket[0] in HBNBCommand.my_command:
                arg = dot[0] + ' ' + f_bracket[0] + ' ' + s_brackets[0]
        return arg

    def do_EOF(self, arg):
        """When EOF, exit the command interpreter"""
        return True

    def do_quit(self, arg):
        """Quit the command interpreter"""
        return True

    def emptyline(self):
        """When an empty line, print nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

