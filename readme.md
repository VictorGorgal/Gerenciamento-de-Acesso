# Gerenciamento de Acesso

Este projeto consiste em um sistema  para o gerenciamento do acesso às salas de uma empresa.  
Para isso será necessário utilizar uma placa arduino para fazer o gerenciamento das trancas físicas,  
haverá um menu exibido atravéz do Serial do Arduino, por ele deverá ser inserido dados para o cadastro de um usuário, sendo eles:
- Nome
- Senha
- Se ele será um administrador ou não.  

No mesmo menu deverá ser inserido também a listagem dos nomes dos usuários cadastrados, listagem dos eventos (será necessário inserir a senha cadastrada para obter acesso aos eventos) e opção para a liberação da porta 1 e 2.

As informações referentes aos usuários e eventos devem ser armazenadas na memória Flash do microcontrolador.

A interface de cadastro dos usuários deve ser feita através da serial

O acesso aos eventos gerados devem ser limitado somente ao usuário administrador

A liberação de acesso às salas deve ser realizada após solicitação e validação da senha do usuário para que somente usuários autorizados possuam acesso

O fechamento das portas deve ser feito através do pressionamento do botão correspondente à porta a ser fechada ou após um timeout de 5 segundos ser atingido

As informações deverão ser enviadas para o back-end através de rotas específicas e salvas em um banco de dados SQL

# Circuito
![image](https://user-images.githubusercontent.com/94933775/169448342-94757235-431d-4f9b-825b-f40918949954.png)  

- LED Verde -> Porta 1  
- LED Vermelho -> Porta 2  
- Botão esquerdo -> Botão da porta 1  
- Botão direito -> Botão da porta 2  
- Os botões apresentam resistor de pull-down de 10kΩ  
- Os LEDs possuem resistor de 120Ω para não queimarem  
