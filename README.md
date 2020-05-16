# Smart Safe Box Project
Projeto desenvolvido para a discplina de Sistemas Embarcados (SEM0544, 1o semestre de 2020) do Curso de Engenharia Mecatrônica EESC-USP
<h2> Descrição </h2>
<p> Este projeto consiste no desenvolvimento de um sistema de segurança em forma de cofre inteligente, cuja permissão de acesso é feita por meio de reconhecimento facial. Conforme idealizado, seu funcionamento se baseará no uso de câmeras conectadas a placa BeagleBone Black, responsável por processar e analisar as imagens obtidas; dependendo do resultado, um controlador executará a abertura do cofre através do acionamento de um motor; além disso, será utilizada comunicação CAN para ligação da placa ao controlador. </p>

<h2> Requisitos </h2>

<h3> Requisitos Funcionais </h3>
<p><ul>
    <li>O sistema, ao ser acionado, deve ser capaz de capturar uma imagem por meio de sensoriamento de imagem. Em seguida, este deverá identificar a presença de rostos na imagem obtida, comparando-os com um banco de dados de “Pessoas Autorizadas”.</li><ul>
             <li>Caso o rosto identificado corresponda ao de alguém autorizado, o sistema deverá acionar o motor, responsável pela abertura mecânica do cofre.</li>
             <li>Caso contrário, o sistema deverá sinalizar "Acesso Negado" e realizar o reconhecimento novamente, permitindo que seja feito um total de 3 tentativas seguidas, logo, caso a identificação falhe as 3 vezes durante o intervalo, o sistema deverá ser bloqueado e acionado um alarme sonoro.
</li>
  </ul>
  <li>Com relação ao fechamento </li>
  <li>O sistema deve ser capaz de registrar novos rostos no banco de dados “Pessoas Autorizadas”, bem como remover algum rosto armazenado anteriormente. Tal processo será autorizado apenas se executado pelo proprietário do produto.</li>
</ul></p>

<h3> Requisitos Não-Funcionais </h3>
<p><ul>
    <li>O processo de reconhecimento facial deve ser capaz de identificar um rosto contido no banco de dados em 90% das vezes.</li><ul>
             <li>Com relação ao reconhecimento de um rosto não autorizado ("falso positivo"), a confiabilidade do sistema deve ser a mais alta possível.</li>
  </ul>
  <li>O sistema de visão computacional deve ser capaz de reconhecer se o rosto é real (3D). Caso identifique rostos em 2D (fotos, imagens projetadas, etc), deve desconsiderá-los.</li>
  <li>O sistema deve possuir uma interface usuário-máquina intuitiva, que auxilie o usuário com o posicionamento com rosto por meio de um display. Deve também informar caso o sistema falhe em reconhecer um rosto autorizado, dando a opção ao usuário em repetir o processo (e o número de tentativas). Além disso, o acionamento para o reconhecimento será feito por meio de um botão contido nesta interface.</li>
  <li>O processo de captura de imagem para armazenamento no banco de dados deve seguir os requisitos da norma ISO/IEC 19794-5.
</li>
</ul></p>
