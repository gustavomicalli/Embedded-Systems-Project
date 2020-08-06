# importa as bibliotecas necessárias
from imutils.video import VideoStream
import face_recognition
import argparse
import imutils
import pickle
import time
import cv2

# construção da analise de argumentos e analise
ap = argparse.ArgumentParser()
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
ap.add_argument("-o", "--output", type=str,
	help="path to output video")
ap.add_argument("-y", "--display", type=int, default=1,
	help="whether or not to display output frame to screen")
ap.add_argument("-d", "--detection-method", type=str, default="cnn",
	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())

# carrega as faces conhecidas
print("[INFO] loading encodings...")
data = pickle.loads(open(args["encodings"], "rb").read())

# inicializa o vídeo e o ponteiro para gerar o arquivo de vídeo
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
writer = None
time.sleep(2.0)

# loop sobre os quadros do arquivo de vídeo
while True:
	# pega o quadro do vídeo em questão
	frame = vs.read()
	
	# converte o quadro de entrada de  BGR para RGB e o redimensiona para uma largura de 750 pixels(para aumentar a velocidade de processamento)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	rgb = imutils.resize(frame, width=750)
	r = frame.shape[1] / float(rgb.shape[1])

	#  detecta as coordenadas(x, y) das caixas delimitadoras correspondentes a cada face na imagem de entrada
	boxes = face_recognition.face_locations(rgb,
		model=args["detection_method"])
	encodings = face_recognition.face_encodings(rgb, boxes)

	# loop sobre as faces reconhecidas
	for (top, right, bottom, left) in zip(boxes):
		# redimensiona as coordenadas do rosto
		top = int(top * r)
		right = int(right * r)
		bottom = int(bottom * r)
		left = int(left * r)

	# se a câmera tiver saída nula e deve-se gravar o vídeo de saída em disco, inicializa a câmera
	if writer is None and args["output"] is not None:
		fourcc = cv2.VideoWriter_fourcc(*"MJPG")
		writer = cv2.VideoWriter(args["output"], fourcc, 20,
			(frame.shape[1], frame.shape[0]), True)

	# se a câmera não tiver saída nula, gravar o quadro com face reconhecida no banco de dados
	if writer is not None:
		writer.write(frame)

        #verifica se o quadro de saída deve ser exibido para a tela
	if args["display"] > 0:
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF
		print("[INFO] Successful Acess!")

		# se a tecla 'q' for pressionada, sai do loop
		if key == ord("q"):
			break

# limpeza
cv2.destroyAllWindows()
vs.stop()

# verificar se o gravador de vídeo precisa ser liberado
if writer is not None:
	writer.release()
