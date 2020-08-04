# Smart Safe Box Project
Projeto desenvolvido para a discplina de Sistemas Embarcados (SEM0544, 1º semestre de 2020) do Curso de Engenharia Mecatrônica EESC-USP

<h2> Integrantes </h2>
<p><ul>
    
  <li>Bley Ribeiro de Almeida Junior (9312501)</li>
  <li>Bruno Fleury Fina Paulillo (9012688)</li>
  <li>Gustavo Bevilacqua Micalli (9866423)
</li>
</ul></p>

<h2> Materiais </h2>
<p><ul>
    
  <li>Beagle Bone Black Wireless</li>
  <li>Webcam Logitech C920 Pro</li>
  <li>Display LCD4 Cape</li>
  <li>Sensor Capacitivo CM30-3015NC</li>
  <li>Driver motor L298N </li>
  <li>Motor de passo Nema 17</li>
</ul></p>



<h2> Descrição </h2>
<img src="https://user-images.githubusercontent.com/64747785/82112787-cbaebf80-9726-11ea-87b2-587ccfb65b05.jpg">
<p> Este projeto consiste no desenvolvimento de um sistema de segurança em forma de cofre inteligente, cuja permissão de acesso é feita por meio de reconhecimento facial. Conforme idealizado, seu funcionamento se baseará no uso de câmeras conectadas a placa BeagleBone Black, responsável por processar e analisar as imagens obtidas; dependendo do resultado, um controlador executará a abertura do cofre através do acionamento de um motor. A plataforma executará o OpenCV para processar e reconhecer as imagens capturadas em movimento utilizando-se do sistema operacional open source Linux para a interface entre aplicação do usuário e hardware. Além disso, a comunicação CAN garantirá simplicidade, robustez e confiabilidade para a transmissão desses dados. </p>

<h2> Requisitos </h2>

<h3> Requisitos Funcionais </h3>
<p><ul>
    <li>O sistema, ao ser acionado, deve ser capaz de capturar uma imagem por meio de sensoriamento de imagem. Em seguida, este deverá identificar a presença de rostos na imagem obtida, comparando-os com um banco de dados de “Pessoas Autorizadas”.</li><ul>
             <li>Caso o rosto identificado corresponda ao de alguém autorizado, o sistema deverá acionar o motor, responsável pela abertura mecânica da trava do cofre.</li>
             <li>Caso contrário, o sistema deverá executar as tentativas de reconhecimento 3 vezes e sinalizar "Acesso Negado" com o desligamento do Display caso nenhuma das 3 tentativas tenham sucesso.
    </li>
  </ul>
  <li>Com relação a abertura da porta do cofre, uma vez que foi feita a abertura mecânica da trava, o usuário terá um tempo determinado para a abertura da porta manualmente.
  <li>Com relação ao fechamento da porta do cofre, seu acionamento será de forma manual. Após identificado o fechamento da porta por um sensor de presença, o software executará o código de fechamento da trava pelo motor.
 </li>
  <li>O fechamento da trava do cofre ocorrerá por um sensor de presença de objeto uma vez constatada que a porta está fechada.</li>
  <li>O sistema deve ser capaz de registrar novos rostos no banco de dados “Pessoas Autorizadas”, bem como remover algum rosto armazenado anteriormente. Tal processo será autorizado apenas se executado pelo proprietário do produto.</li>
</ul></p>

<h3> Requisitos Não-Funcionais </h3>
<p><ul>
    <li>O processo de reconhecimento facial deve ser capaz de identificar um rosto contido no banco de dados em 90% das vezes.</li><ul>
             <li>Com relação ao reconhecimento de um rosto não autorizado ("falso positivo"), a confiabilidade do sistema deve ser a mais alta possível.</li>
  </ul>
  <li>O sistema de visão computacional deve ser capaz de reconhecer se o rosto é real (3D). Caso identifique rostos em 2D (fotos, imagens projetadas, etc), deve desconsiderá-los.</li>
  <li>O sistema deve possuir uma interface usuário-máquina intuitiva, que auxilie o usuário com o posicionamento com rosto por meio de um display, além de um menu de configurações para banco de dados e tempo de fechamento automático. Deve também informar caso o sistema falhe em reconhecer um rosto autorizado, dando a opção ao usuário em repetir o processo (e o número de tentativas). Além disso, o acionamento para o reconhecimento será feito por meio de um botão contido nesta interface.</li>
    <li>O sensor utilizado para o fechamento da trava do cofre será um sensor capacitivo.</li>
  <li>O processo de captura de imagem para armazenamento no banco de dados deve seguir os requisitos da norma ISO/IEC 19794-5.
</li>
</ul></p>



<h2> Possíveis soluções para os requisitos: </h2>
<p><ul>
    
  <li>Utilização do algoritmo Viola Jones em conjunto com o algoritmo LBD (Local Binary Patterns) para a detecção de faces, ambos combinados garantem baixa taxa de falso positivo e elevada taxa de acerto.</li>
  <li>Utilização do algoritmo Autofaces para o reconhecimento facial, o qual é é a vetorização e a captação de um conjunto de autovetores para a coleção das caracteristicas da imagem. </li>
  <li>A câmera a ser utilizada no projeto é a webcam Logitech C920 Pro, uma vez que esta apresenta qualidade de imagem satisfatória para reconhecimento fácil, boa durabilidade e custo relativamente baixo.</li>
  <li>Será utilizado um display LCD4 Cape como interface de comunicação usuário-máquina. Este foi escolhido devido a sua compatibilidade com a BBB, durabilidade, preço e tamanho propício para a aplicação.</li>
  <li>Considerando uma distância máxima entre a porta e o cofre de 15mm para a ativação da trava o sensor capacitivo a ser utilizado foi o CM30-3015NC, o qual possui distância sensorial de 15 mm, e distância operacional de 0-30mm.</li>
  <li>O mecanismo responsável por abrir/fechar a tranca do cofre utilizará um motor de passo Nema 17 como atuador, sendo o L298N utilizado como controlador. Estes foram selecionados em função de sua durabilidade, preço e compatibilidade.</li>
  <li>A segurança dos dados armazenados pelo cofre deverá ser garantida através da implementação de controle de acesso, criptografia e controle de fluxo.</li>
  <li>Para garantir a conformidade com os padrões ISO/ICAO, o algoritmo deverá ser testado pelo framework Biolab-ICAO, que serve como base de referência para se avaliar métodos de validação de imagens faciais. </li>
</ul></p>
