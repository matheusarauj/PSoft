# coding: utf-8

import socket, sys, getpass
from _thread import *  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('google.com', 80))
print ('O IP Público do Servidor é: {}'.format(s.getsockname()[0]))

print ('O IP Local do Servidor é: {}'.format(socket.gethostbyname(socket.gethostname())))

porta = int(sys.argv[1] if len(sys.argv) > 1 else 9090)

s = socket.socket()
s.bind(('{}'.format(socket.gethostbyname(socket.gethostname())), porta))

s.listen(10)
print("Aguardando conexão com a porta {}".format(porta))

print("\n------- Mensagens -------\n")

conexoes = []

def clientthread(conexao):
	conexoes.append(conexao)
	conexao.send("\n------- Bem vindo ao mini chat -------\n".encode())
	conexao.send("Digite ':bye' para sair\n\n".encode())

	nome = getpass.getuser()
	while True:
		mensagem = conexao.recv(4096)
		if mensagem.decode().strip() == ":bye":
			mensagem = "Você foi desconectado\nAperte ENTER para finalizar\n".encode()
			conexao.send(mensagem)
			for conn in conexoes:
				mensagem = nome + " foi desconectado\n"
				if len(conexoes) >= 1:
					print(mensagem)
				if conn != conexao:
					conn.send(mensagem.encode())
			break
		
		reply = nome + ": " + mensagem.decode().strip()
		if mensagem:
			print (reply)
		for conn in conexoes:
			if conn != conexao:
				if mensagem:
					reply = reply + "\n"
					conn.send(reply.encode())
	conexao.close()
	conexoes.remove(conexao)
	exit()

while 1:
	conexao, endereco = s.accept()
	print("Conectado em: {}:{}".format(endereco[0],endereco[1]))
	start_new_thread(clientthread, (conexao,))
s.close()