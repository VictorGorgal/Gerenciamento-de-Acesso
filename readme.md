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
![image](https://user-images.githubusercontent.com/94933775/169667055-039b0301-35cb-4801-ac29-e8f6f707c4f7.png)

- LED Verde -> Porta 1  
- LED Vermelho -> Porta 2  
- Botão esquerdo -> Botão da porta 1  
- Botão direito -> Botão da porta 2  
- Os botões apresentam resistor de pull-down de 10kΩ  

Protótipo físico  
![image](https://user-images.githubusercontent.com/94933775/169666084-5563df25-7ac7-490e-ac21-1b9c995dd4b1.png)

O circuito físico não apresenta resistores nos LEDs pois a voltagem de 3.3V da saída do nodeMCU não é o suficiente para queimá-los.

# Funcionamento  
A memória EEPROM do node foi dividida em 2 partes iguais de 512 bytes para armazenar os usuários cadastrados e os eventos:  
![image](https://user-images.githubusercontent.com/94933775/169666644-19578d1b-472d-4cf5-bdb9-719670268581.png)

Foi desenvolvido um Monitor Serial para este projeto integrado com o banco de dados.  
![image](https://user-images.githubusercontent.com/94933775/169666885-0d102886-ca6e-4613-9ecc-c4827b8ed9b0.png)  
### Diferente do Monitor Serial da IDE do Arduino, as novas mensagens aparecem no topo.

Visualizador de banco de dados:  
![image](https://user-images.githubusercontent.com/94933775/169666945-3b503ad2-288a-47b4-b6ec-d7571c30c4f2.png)

# Bibliotecas usadas:
```
pip install pyserial   # comunicação serial
pip install pyqt6      # interface gráfica
```

# Rodando o programa
- Primeiro monte o circuito indicado na foto, o projeto foi desenvolvido para nodeMCU devido a falta de um arduino.  
- Carregue o programa Arduino/Arduino.ino no nodeMCU, caso haja necessidade de limpar a memória EEPROM, descomente a linha "resetEEPROM();" no void setup(), carregue o codigo, comente novamente a linha "resetEEPROM();" e carregue novamente o código.
- Feche a IDE Arduino e execute o main.py.
O arquivo do banco de dados está salvo em back_end/database.db (caso não exista esse arquivo, o programa irá criá-lo automaticamente na primeira execução)

# Possíveis problemas:
### Access is denied
![image](https://user-images.githubusercontent.com/94933775/169667211-a8aed75d-a688-4635-b9b7-0557f67173c1.png)  
Certifique-se que selecionou a porta serial correta e que o arquivo main.py não está sendo executado.

### Access is denied
![image](https://user-images.githubusercontent.com/94933775/169667279-22cc70b0-a9a9-4abc-9fb8-20469099abdd.png)  
Certifique-se que a IDE do arduino não está aberta.

### File not found error
![image](https://user-images.githubusercontent.com/94933775/169667306-ed2add32-6b10-4b2e-b183-dfd1fd18ba5c.png)  
No arquivo back_end/arduino_serial.py troque a porta serial para a que o computador reconheceu o nodeMCU dentro do def __init __

### Saída serial vazia  
![image](https://user-images.githubusercontent.com/94933775/169667628-5c1cc48b-ca19-4a69-8a95-56694f1e0d55.png)  
Resete o nodeMCU apertando o botão reset dele.

