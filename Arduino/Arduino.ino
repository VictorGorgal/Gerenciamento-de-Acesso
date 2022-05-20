#include <EEPROM.h>

#define btn1 D0
#define btn2 D2
#define porta1 D5
#define porta2 D8
// aloca memoria para salvar variaveis na memoria flash
#define EEPROM_SIZE 1024

struct Usuario{
  String nome;
  String senha;
  bool admin;
};

struct Evento{
  bool porta;  // 0 -> porta1 ; 1 -> porta2
  String nomeUsuario;
};

// armazena o endereco do EEPROM a ser salvo
int usuarioAddress = 5;
int eventoAddress = int(EEPROM_SIZE/2) + 5;
// armazena o endereco do EEPROM a ser lido
int userAddress = 5;
int eventAddress = int(EEPROM_SIZE/2) + 5;
// armazena quantos usuarios e eventos foram salvos
int usuariosCadastrados;
int eventosCadastrados;

// salva quando as portas foram abertas
long tempoPorta1;
long tempoPorta2;
// salva se a porta esta aberta
bool estadoPorta1;
bool estadoPorta2;

// index selecionado
int selecionado;
// armazena em qual etapa da funcao esta (etapa = 2 -> segunda vez rodada)
int etapa;
// entrada quando não for int
String entrada;
// dados do usuario
Usuario usuario;
// dados do evento
Evento evento;


void setup(){
  Serial.begin(9600);
  EEPROM.begin(EEPROM_SIZE);

  pinMode(btn1, INPUT);
  pinMode(btn2, INPUT);  
  pinMode(porta1, OUTPUT);
  pinMode(porta2, OUTPUT);

  digitalWrite(porta1, LOW);
  digitalWrite(porta2, LOW);

  // limpa a memoria flash
//  resetEEPROM();
  carregar();
  printMenu();
}


void loop(){
  fecharPorta1();
  fecharPorta2();
  
  if(Serial.available() > 0){
    if(etapa == 0){
      selecionado = Serial.parseInt();
      Serial.read();  // limpa o buffer serial
    }else{
      entrada = Serial.readString();
      entrada.trim();  // remove espacos desnecessarios (" ", "\n"...)
    }

    // roda a funcao de acordo com a opcao selecionada
    switch(selecionado){
      case 1:
        cadastrarNovoUsuario();
        break;
      case 2:
        listarUsuarios();
        break;
      case 3:
        listarEventos();
        break;
      case 4:
        liberarPorta1();
        break;
      case 5:
        liberarPorta2();
        break;
    }
  }
}


void printMenu(){
  Serial.println(F("-----------------------------------------------"));
  Serial.println(F("Cadastro do usuário [1]"));
  Serial.println(F("Listagem dos nomes dos usuários cadastrados [2]"));
  Serial.println(F("Listagem dos eventos [3]"));
  Serial.println(F("Liberação da porta 1 [4]"));
  Serial.println(F("Liberação da porta 2 [5]"));
  Serial.println(F("-----------------------------------------------"));
}


bool checarUsuario(){
  if(usuario.senha == ""){
    Serial.println(F("Nenhum usuário cadastrado!"));
    printMenu();
    return false;
  }
  return true;
}


void fecharPorta1(){
  if(!estadoPorta1){  // caso a porta esteja fechada, sair da funcao para nao fecha-la novamente
    return;
  }

  if(millis() - tempoPorta1 >= 5000){
    Serial.println(F("O tempo da porta 1 excedeu 5 segundos, fechando..."));
    digitalWrite(porta1, LOW);
    estadoPorta1 = false;
  }
  if(digitalRead(btn1) == 1){
    digitalWrite(porta1, LOW);
    estadoPorta1 = false;
  }
}


void fecharPorta2(){
  if(!estadoPorta2){
    return;
  }

  if(millis() - tempoPorta2 >= 5000){
    Serial.println(F("O tempo da porta 2 excedeu 5 segundos, fechando..."));
    digitalWrite(porta2, LOW);
    estadoPorta2 = false;
  }
  if(digitalRead(btn2)){
    digitalWrite(porta2, LOW);
    estadoPorta2 = false;
  }
}


void cadastrarNovoUsuario(){
  etapa++;

  switch(etapa){
    case 1:
      Serial.println("Insira o nome de usuário:");
      break;
      
    case 2:
      if(entrada == ""){
        Serial.println("Insira um nome com pelo menos 1 caracter!");
        etapa = 0;
        printMenu();
        return;
      }
      if(entrada.length() > 30){
        Serial.println("Insira um nome com ate 30 caracteres!");
        etapa = 0;
        printMenu();
        return;
      }
      
      usuario.nome = entrada;
      Serial.println("Insira a senha de usuário:");
      break;
      
    case 3:
      if(entrada == ""){
        Serial.println("Insira uma senha com pelo menos 1 caracter!");
        etapa = 0;
        printMenu();
        return;
      }
      if(entrada.length() > 30){
        Serial.println("Insira uma senha com ate 30 caracteres!");
        etapa = 0;
        printMenu();
        return;
      }
      
      usuario.senha = entrada;
      Serial.println("Administrador? [0]-nao [1]-sim");
      break;
      
    case 4:
      usuario.admin = false;
      if(entrada == "1")
        usuario.admin = true;
      salvarUsuario(usuario);
      Serial.println("Usuário cadastrado!");
      printMenu();
      etapa = 0;
      break;
  }
}


void listarUsuarios(){
  Serial.println("###nome dos usuarios###");
  
  userAddress = 5;
  Serial.println("lendo usuarios...");
  Usuario user;
  for(int i = 0; i < usuariosCadastrados; i++){
    EEPROM.get(userAddress, user);

    Serial.println("-------------");
    Serial.print("nome: ");
    Serial.println(user.nome);
  
    userAddress += sizeof(user);
  }

  printMenu();
}


void listarEventos(){
  if(!checarUsuario()){
    return;
  }
  
  etapa++;

  switch(etapa){
    case 1:
      Serial.println(F("Insira a senha do usuário administrador:"));
      break;
      
    case 2:
      if(entrada != usuario.senha){
        Serial.println(F("Senha errada!"));
        etapa = 0;
        printMenu();
        break;
      }
      
      if(!usuario.admin){
        Serial.println(F("Usuario deve ser administrador!"));
        etapa = 0;
        printMenu();
        break;
      }

      Serial.println(F("### dados do usuario ###"));
      printUsuarios();
      Serial.println(F("### indentificacao da porta que foi aberta ###"));
      printEventos();
      etapa = 0;
      printMenu();
      break;
  }
}


void liberarPorta1(){
  if(!checarUsuario()){
    return;
  }
  
  etapa++;

  switch(etapa){
    case 1:
      Serial.println(F("Insira a senha de usuário"));
      break;
      
    case 2:
      if(usuario.senha != entrada){
        Serial.println(F("Senha incorreta"));
        etapa = 0;
        printMenu();
        break;
      }

      evento.porta = 0;
      evento.nomeUsuario = usuario.nome;
      salvarEvento(evento);
      digitalWrite(porta1, HIGH);
      tempoPorta1 = millis();
      estadoPorta1 = true;
      etapa = 0;
      printMenu();
      break;
  }
}


void liberarPorta2(){
  if(!checarUsuario()){
    return;
  }
  
  etapa++;

  switch(etapa){
    case 1:
      Serial.println(F("Insira a senha de usuário"));
      break;
      
    case 2:
      if(usuario.senha != entrada){
        Serial.println(F("Senha incorreta"));
        etapa = 0;
        printMenu();
        break;
      }

      evento.porta = 1;
      evento.nomeUsuario = usuario.nome;
      salvarEvento(evento);
      digitalWrite(porta2, HIGH);
      tempoPorta2 = millis();
      estadoPorta2 = true;
      etapa = 0;
      printMenu();
      break;
  }
}


void salvarUsuario(Usuario usuario){
  usuariosCadastrados++;
  
  Serial.println("salvando...");
  Serial.print("nome: ");
  Serial.println(usuario.nome);
  Serial.print("senha: ");
  Serial.println(usuario.senha);
  Serial.print("admin: ");
  Serial.println(usuario.admin);

  EEPROM.put(0, usuariosCadastrados);
  EEPROM.put(usuarioAddress, usuario);  // salva o nome no endereco 0
  EEPROM.commit();

  usuarioAddress += sizeof(usuario);
}


void salvarEvento(Evento evento){
  eventosCadastrados++;
  
  Serial.println("salvando...");
  Serial.print("evento: ");
  Serial.println(evento.porta);
  Serial.print("nome: ");
  Serial.println(evento.nomeUsuario);

  EEPROM.put(int(EEPROM_SIZE/2), eventosCadastrados);
  EEPROM.put(eventoAddress, evento);  // salva o nome no endereco 0
  EEPROM.commit();

  eventoAddress += sizeof(evento);
}


void printUsuarios(){  
  Serial.println("lendo usuarios...");
  Usuario user;
  userAddress = 5;
  for(int i = 0; i < usuariosCadastrados; i++){
    EEPROM.get(userAddress, user);

    Serial.println("-------------");
    Serial.print("nome: ");
    Serial.println(user.nome);
    Serial.print("senha: ");
    Serial.println(user.senha);
    Serial.print("Admin: ");
    Serial.println(user.admin);
  
    userAddress += sizeof(user);
  }
}


void printEventos(){
  Serial.println("lendo eventos...");
  Evento event;
  eventAddress = 5;
  for(int i = 0; i < eventosCadastrados; i++){
    EEPROM.get(eventAddress, event);

    Serial.println("-------------");
    Serial.print("porta: ");
    Serial.println(event.porta);
    Serial.print("usuario: ");
    Serial.println(event.nomeUsuario);
  
    eventAddress += sizeof(event);
  }
}


void carregar(){
  EEPROM.get(0, usuariosCadastrados);
  EEPROM.get(int(EEPROM_SIZE/2), eventosCadastrados);
}


void resetEEPROM(){
  for (int i = 0; i < EEPROM_SIZE; i++) {
    EEPROM.write(i, 0);
  }
  EEPROM.commit();
}
