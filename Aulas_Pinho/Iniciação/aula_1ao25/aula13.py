a = "A"
b = "B"
c = 1.1
string ="a={} b={} c={:.3f}" #cada {} refencia o primeiro, segundo... valor na ordem

formato = string. format(a, b, c) # como ele dá 3 casas pro c, ele faz 1.100

print(formato)
print(string. format(a, b, c))
#para pegar a ordem que você quer, o primeiro é o 0,1,2...

string_ordemdesejada="a={1} b={0} c={2:.3f}"
print(string_ordemdesejada. format(a, b, c)) #aqui o A fica na ordem do B 

print (f"{c:.8f}")