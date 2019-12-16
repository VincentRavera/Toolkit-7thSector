#!/usr/bin/env python3
# coding: utf-8

op = ['+', '-', '*', '/']
output = None
for i in op:
    for j in op:
        for k in op:
            executable_string = 'output=' + '((' + str(5.0) + i + str(8.0) + ')' + j + str(6.0) + ')' + k + str(2.0)
            exec(executable_string)
            if output == 39:
                print(executable_string, "=", output)
