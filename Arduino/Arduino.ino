#include <EEPROM.h>

#define btn1 D0
#define btn2 D2
#define porta1 D5
#define porta2 D8

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
String nome;
String senha;
bool admin;


void setup(){
  Serial.begin(9600);
  EEPROM.begin(128);  // 128 bytes alocados para salvar variaveis na memoria flash

  pinMode(btn1, INPUT);
  pinMode(btn2, INPUT);  
  pinMode(porta1, OUTPUT);
  pinMode(porta2, OUTPUT);

  digitalWrite(porta1, LOW);
  digitalWrite(porta2, LOW);

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
  if(senha == ""){
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
      Serial.println(F("Insira o nome de usuário:"));
      break;
      
    case 2:
      if(entrada == ""){
        Serial.println(F("Insira um nome com pelo menos 1 caracter!"));
        etapa = 0;
        printMenu();
        return;
      }
      nome = entrada;
      Serial.println(F("Insira a senha de usuário:"));
      break;
      
    case 3:
      if(entrada == ""){
        Serial.println(F("Insira uma senha com pelo menos 1 caracter!"));
        etapa = 0;
        printMenu();
        return;
      }
      senha = entrada;
      Serial.println(F("Administrador? [0]-nao [1]-sim"));
      break;
      
    case 4:
      admin = false;
      if(entrada == "1")
        admin = true;
      void salvar();
      Serial.println(F("Usuário cadastrado!"));
      Serial.print(F("Nome: "));
      Serial.println(F(String(sizeof(nome));
      Serial.print(F("Senha: "));
      Serial.println(F(String(sizeof(senha));
      Serial.print(F("Admin: "));
      Serial.println(F(String(sizeof(admin));
      printMenu();
      etapa = 0;
      break;
  }
}


void listarUsuarios(){
  Serial.println(F("###nome dos usuarios###"));
  
  Serial.println(nome);

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
      if(entrada != senha){
        Serial.println(F("Senha errada!"));
        etapa = 0;
        printMenu();
        break;
      }
      
      if(!admin){
        Serial.println(F("Usuario deve ser administrador!"));
        etapa = 0;
        printMenu();
        break;
      }

      Serial.println(F("### dados do usuario ###"));
      Serial.println(F("### indentificacao da porta que foi aberta ###"));
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
      if(senha != entrada){
        Serial.println(F("Senha incorreta"));
        etapa = 0;
        printMenu();
        break;
      }

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
      if(senha != entrada){
        Serial.println(F("Senha incorreta"));
        etapa = 0;
        printMenu();
        break;
      }

      digitalWrite(porta2, HIGH);
      tempoPorta2 = millis();
      estadoPorta2 = true;
      etapa = 0;
      printMenu();
      break;
  }
}


void salvar(){
  Serial.println(F("Salvando..."));
}
