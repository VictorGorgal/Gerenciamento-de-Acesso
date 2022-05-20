#define btn1 D0
#define btn2 D2
#define porta1 D4
#define porta2 D5

// salva quando as portas foram abertas
long tempoPorta1;
long tempoPorta2;
// salva se a porta esta aberta
bool estadoPorta1;
bool estadoPorta2;

// index selecionado
int selecionado;
// armazena em qual estagio da funcao esta (estagio 2 -> segunda vez rodada)
int estagio;
// entrada quando não for int
String entrada;
// dados do usuario
String nome;
String senha;
bool admin;


void setup(){
  Serial.begin(9600);

  printMenu();
}


void loop(){
  fecharPorta1();
  fecharPorta2();
  
  if(Serial.available() > 0){
    if(estagio == 0)
      selecionado = Serial.parseInt();
    else
      entrada = Serial.read();

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
      default:
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


void fecharPorta1(){
  if(!estadoPorta1){
    return;
  }

  if(millis() - tempoPorta1 >= 5000){
    digitalWrite(porta1, LOW);
  }
  if(digitalRead(btn1)){
    digitalWrite(porta1, LOW);
  }
}


void fecharPorta2(){
  if(!estadoPorta2){
    return;
  }

  if(millis() - tempoPorta2 >= 5000){
    digitalWrite(porta2, LOW);
  }
  if(digitalRead(btn2)){
    digitalWrite(porta2, LOW);
  }
}


void cadastrarNovoUsuario(){
  estagio++;

  switch(estagio){
    case 1:
      Serial.println(F("Insira o nome de usuário:"));
      break;
    case 2:
      nome = entrada;
      Serial.println(F("Insira a senha de usuário:"));
      break;
    case 3:
      senha = entrada;
      Serial.println(F("Administrador? [0]-nao [1]-sim"));
      break;
    case 4:
      if(entrada == "1")
        admin = true;
      void salvar();
      Serial.println(F("Usuário cadastrado!"));
      printMenu();
      estagio = 0;
      break;
  }
}


void listarUsuarios(){
  Serial.println(F("###nome dos usuarios###"));

  printMenu();
}


void listarEventos(){
  estagio++;

  switch(estagio){
    case 1:
      Serial.println(F("Insira a senha do usuário administrador:"));
      break;
    case 2:
      if(entrada != senha){
        Serial.println(F("Senha errada"));
        estagio = 0;
        printMenu();
        break;
      }
      if(!admin){
        Serial.println(F("Usuario deve ser administrador!"));
        estagio = 0;
        printMenu();
        break;
      }

      Serial.println(F("### dados do usuario ###"));
      Serial.println(F("### indentificacao da porta que foi aberta ###"));

      estagio = 0;
      printMenu();
      break;
  }
}


void liberarPorta1(){
  estagio++;

  switch(estagio){
    case 1:
      Serial.println(F("Insira a senha de usuário"));
      break;
    case 2:
      if(senha != entrada){
        Serial.println(F("Senha incorreta"));
        estagio = 0;
        printMenu();
        break;
      }

      digitalWrite(porta1, HIGH);
      tempoPorta1 = millis();
      estadoPorta1 = true;
      estagio = 0;
      printMenu();
      break;
  }
}


void liberarPorta2(){
  estagio++;

  switch(estagio){
    case 1:
      Serial.println(F("Insira a senha de usuário"));
      break;
    case 2:
      if(senha != entrada){
        Serial.println(F("Senha incorreta"));
        estagio = 0;
        printMenu();
        break;
      }

      digitalWrite(porta2, HIGH);
      tempoPorta2 = millis();
      estadoPorta2 = true;
      estagio = 0;
      printMenu();
      break;
  }
}


void salvar(){
  Serial.println(F("Salvando..."));
}
