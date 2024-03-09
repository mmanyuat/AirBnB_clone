#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def userinput(self, arg):
        if '.' in arg and '(' in arg and ')' in arg:
            dot = arg.split('.')
            f_bracket = dot[1].split('(')
            s_brakets = f_bracket[1].split(')')

    def do_EOF(self, arg):
        return(true)

    def do_quit (self, arg):
        return(true)

    def emptyline (self):
        pass

    def do_help (self, arg):



if __name__ == '__main__':
    HBNBCommand().cmdloop()

    

