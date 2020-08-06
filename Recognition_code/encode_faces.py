def reconhecer():
	# importa as bibliotecas necessárias
	from imutils import paths
	import face_recognition
	import argparse
	import pickle
	import cv2
	import os

	# construção da analise de argumentos
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--dataset", required=True,
		help="path to input directory of faces + images")
	ap.add_argument("-e", "--encodings", required=True,
		help="path to serialized db of facial encodings")
	ap.add_argument("-d", "--detection-method", type=str, default="cnn",
		help="face detection model to use: either `hog` or `cnn`")
	args = vars(ap.parse_args())

	# seleciona os caminhos para as imagens de entrada no banco de dados
	print("[INFO] quantifying faces...")
	imagePaths = list(paths.list_images(args["dataset"]))

	# inicializa a lista de codificações conhecidas
	knownEncodings = []

	# loop sobre os caminhos das imagens
	for (i, imagePath) in enumerate(imagePaths):
		# carrega a imagem de entrada e converte ela de RGB (OpenCV ordering) para dlib ordering (RGB)
		image = cv2.imread(imagePath)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detecta as coordenadas(x, y) das caixas delimitadoras correspondentes a cada face na imagem de entrada
		boxes = face_recognition.face_locations(rgb,
			model=args["detection_method"])

		# cálculo do vetor referente a imagem
		encodings = face_recognition.face_encodings(rgb, boxes)

		# loop sobre as codificações
		for encoding in encodings:
			# adiciona cada codificação ao conjunto de codificações conhecidas
			knownEncodings.append(encoding)

	# grava as codificações faciais em disco
	print("[INFO] serializing encodings...")
	data = {"encodings": knownEncodings}
	f = open(args["encodings"], "wb")
	f.write(pickle.dumps(data))
	f.close()
