print(
    "Sistema de controle de acesso do escritório para: gerentes, estagiario e analista"
)
cargo_do_funcionario = input("qual seu cargo? ")
dia_da_semana = input("qual o dia da semana? ")

while cargo_do_funcionario != "gerente" or "estagiario" or "analista":
    for i in range(3):
        print("acesso negado, tente outra vez, você só tem {i}tentativas")
        break
if cargo_do_funcionario == "gerente":
    print("Acesso permitido", cargo_do_funcionario)
elif dia_da_semana == "sabado" or dia_da_semana == "domingo":
    print("Acesso negado", cargo_do_funcionario)
else:
    print("Acesso permitido", cargo_do_funcionario)
