op=['+', '-', '*', '/']
output = None
for i in op:
    for j in op:
        for k in op:
            stri = 'output=' + '((' + str(5.0) + i + str(8.0) + ')' + j + str(6.0) + ')' + k + str(2.0)
            exec(stri)
            if output == 39:
                print(stri, "=", output)