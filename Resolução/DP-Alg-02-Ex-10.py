nmat = int(input("Digite o número de matrícula do(a) aluno(a). "))
ano_mat = nmat // 10000
rano_mat = nmat % 10000
semestre = rano_mat // 1000
print ("Ano de matrícula:", ano_mat, "/ Semestre:", semestre)