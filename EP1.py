#Exercicio Programa 1
#Programação Funcional
#Uarlley do Nascimento Amorim


def maquina(a,b,c,d,e):
	"""Essa é a função principal da maquina, onde ela chama todas as outras funções criadas com uma quantia determinada para cada produto, na qual a = produto 1, b = produto 2, c = produto 3, d = produto 4 e e = produto 5."""
	if a==0 and b==0 and c==0 and d==0 and e==0:
		print(" ____________________________________________")
		print("|                                            |")
		print("|                                            |")
		print("|              Todos os produtos             |")
		print("|             estão indisponíveis            |")
		print("|	                                     |")#não sei por que mas tive que colocar um espaço a mais no linux para a tabela ficar certa
		print("|					     |")#mesma coisa nessa linha(perguntar pro professor o porque disso)
		print("|____________________________________________|")
		quit()
		
	else:
		"""Aqui é a realizada a chamada da função imprime, para que o usuário visualize a tabela de preços e escolha o produto, desde que não esteka indisponível"""
		imprime(a,b,c,d,e)
		x=input("Escolha um produto: ")
		print()
		if x=="1":
			if a!=0:
				valor=3.99
				print("Batata Array\nValor: R$3,99")
				print()
				pago=dindin(valor)
				print("Valor pago: R${0:.2f}".format(pago))
				troco=pago-valor+0.001;print("Troco: R${0:.2f}".format(round(troco,2)));print()
				if troco>0:
					print("Pegue seu troco:")
					troquito(troco)
				y=input("Deseja fazer outra operação: S/N: ")
				if y=="s" or y=="S":
					return maquina(a-1,b,c,d,e)
				else:
					print("Obrigado pela preferência!\nVolte Sempre!!!");quit()
			else:
				print("Desculpe mas a Batata Array não está mais disponível.\n")
				y=input("Deseja fazer outra operação: S/N: ")
				if y=="s" or y=="S":
					return maquina(a,b,c,d,e)
				else:
					print("Obrigado pela preferência!\nVolte Sempre!!!")
					quit()
		if x=="2":
			if b!=0:
				valor=2.40
				print("Dolly Guaraná\nValor: R$2,40")
				print()
				pago=dindin(valor)
				print("Valor pago: R${0:.2f}".format(pago))
				troco=pago-valor+0.001;print("Troco: R${0:.2f}".format(round(troco,2)));print()
				if troco>0:
					print("Pegue seu troco:")
					troquito(troco)
				y=input("Deseja fazer outra operação: S/N: ")
				if y=="s" or y=="S":
					return maquina(a,b-1,c,d,e)
				else:
					print("Obrigado pela preferência!\nVolte Sempre!!!");quit()
			else:
				print("Desculpe mas o Dolly Guaraná não está mais disponível.\n")
				y=input("Deseja fazer outra operação: S/N: ")
				if y=="s" or y=="S":
					return maquina(a,b,c,d,e)
				else:
					print("Obrigado pela preferência!\nVolte Sempre!!!")
					quit()
		if x=="3":
			if c!=0:
				valor=2.25
				print("Passatempo\nValor: R$2,25")
				print()
				pago=dindin(valor)
				print("Valor pago: R${0:.2f}".format(pago))
				troco=pago-valor+0.001;print("Troco: R${0:.2f}".format(round(troco,2)));print()
				if troco>0:
					print("Pegue seu troco:")
					troquito(troco)
				y=input("Deseja fazer outra operação: S/N: ")
				if y=="s" or y=="S":
					return maquina(a,b,c-1,d,e)
				else:
					print("Obrigado pela preferência!\nVolte Sempre!!!");quit()
			else:
				print("Desculpe mas o Passatempo não está mais disponível.\n")
				y=input("Deseja fazer outra operação: S/N: ")
				if y=="s" or y=="S":
					return maquina(a,b,c,d,e)
				else:
					print("Obrigado pela preferência!\nVolte Sempre!!!")
					quit()
		if x=="4":
			if d!=0:
				valor=1.80
				print("Trakinas\nValor: R$1,80")
				print()
				pago=dindin(valor)
				print("Valor pago: R${0:.2f}".format(pago))
				troco=pago-valor+0.001;print("Troco: R${0:.2f}".format(round(troco,2)));print()
				if troco>0:
					print("Pegue seu troco:")
					troquito(troco)
				y=input("Deseja fazer outra operação: S/N: ")
				if y=="s" or y=="S":
					return maquina(a,b,c,d-1,e)
				else:
					print("Obrigado pela preferência!\nVolte Sempre!!!");quit()
			else:
				print("Desculpe mas o Trakinas não está mais disponível.\n")
				y=input("Deseja fazer outra operação: S/N: ")
				if y=="s" or y=="S":
					return maquina(a,b,c,d,e)
				else:
					print("Obrigado pela preferência!\nVolte Sempre!!!")
					quit()
		if x=="5":
			if e!=0:
				valor=2.29
				print("Fofura\nValor: R$2,29")
				print()
				pago=dindin(valor)
				print("Valor pago: R${0:.2f}".format(pago))
				troco=pago-valor+0.001;print("Troco: R${0:.2f}".format(round(troco,2)));print()
				if troco>0:
					print("Pegue seu troco:")
					troquito(troco)
				y=input("Deseja fazer outra operação: S/N: ")
				if y=="s" or y=="S":
					return maquina(a,b,c,d,e-1)
				else:
					print("Obrigado pela preferência!\nVolte Sempre!!!")
					quit()
			else:
				print("Desculpe mas o Fofura não está mais disponível.\n")
				y=input("Deseja fazer outra operação: S/N: ")
				if y=="s" or y=="S":
					return maquina(a,b,c,d,e)
				else:
					print("Obrigado pela preferência!\nVolte Sempre!!!")
					quit()
		else:
			print("Escolha um dos produtos listados na tabela.")
			return maquina(a,b,c,d,e)
		
def troquito(troco):
	"""Essa função é responsável em retornar o troco exato para o usuário, sem roubar um centavo!"""
	if troco>=100:
		print("R$100,00")
		return troquito(troco-100)
	elif troco>=50:
		print("R$50,00")
		return troquito(troco-50)
	elif troco>=20:
		print("R$20,00")
		return troquito(troco-20)
	elif troco>=10:
		print("R$10,00")
		return troquito(troco-10)
	elif troco>=5:
		print("R$5,00")
		return troquito(troco-5)
	elif troco>=2:
		print("R$2,00")
		return troquito(troco-2)
	elif troco>=1:
		print("R$1,00")
		return troquito(troco-1)
	elif troco>=0.5:
		print("R$0,50")
		return troquito(troco-0.5)
	elif troco>=0.25:
		print("R$0,25")
		return troquito(troco-0.25)
	elif troco>=0.1:
		print("R$0,10")
		return troquito(troco-0.10)
	elif troco>=0.05:
		print("R$0,05")
		return troquito(troco-0.05)
	elif troco>=0.01:
		print("R$0,01")
		return troquito(troco-0.01)
	else:
		print()
def dindin(valor,n=0):
	"""Essa função é resposável em receber o dinheiro do usuário até que o valor inserido seja maior do que o preço do produto"""
	if n<valor:
		v=float(input("Insira o dinheiro: "))
		return dindin(valor,n+v)
	else:
		print()
		return n
def imprime(a,b,c,d,e):
    """Essa função imprime a tabela de preços e é atualizada a cada compra relizada pelo usuário, e quando um produto é esgotado, o próprio é listado como "indisponível"."""
    if a==0:
        a="- indisponível"
    else:
        a="  - R$3,99    "
    if b==0:
        b="- Indisponível"
    else:
        b="  - R$2.40    "
    if c==0:
        c="- Indisponível"
    else:
        c="  - R$2.25    "
    if d==0:
        d="- Indisponível"
    else:
        d="  - R$1.80    "
    if e==0:
        e="- Indisponível"
    else:
        e="  - R$2,29    "
    print(" ____________________________________________")
    print("|                                            |")
    print("|1-Batata Array              {}  |".format(a))
    print("|2-Dolly Guaraná             {}  |".format(b))
    print("|3-Passatempo                {}  |".format(c))
    print("|4-Trakinas                  {}  |".format(d))
    print("|5-Fofura                    {}  |".format(e))
    print("|____________________________________________|")


	
maquina(5,5,5,5,5)
		
		
