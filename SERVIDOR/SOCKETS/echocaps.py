#coding: utf-8

import socket, sys

porta = int(sys.argv[1] if len(sys.argv) > 1 else 9090)

print ('O IP do Servidor é: {}'.format(socket.gethostbyname(socket.gethostname())))

s = socket.socket()
s.bind(('localhost', porta))

s.listen()

print("Esperando a bendita conexão com a porta {}".format(porta))

conexao, endereco = s.accept()

with conexao:
	print("Conectado na porta {}".format(porta))
	while True:
		print('Aguardando contato de {}'.format(endereco))
		recadinho = conexao.recv(4096)
		recadinhoGritante = recadinho.upper()
		print ("Você tem um novo recado:\n\033[1;32;40m{}\n".format(recadinho))
		if not recadinho: break
		conexao.sendall(recadinhoGritante)
