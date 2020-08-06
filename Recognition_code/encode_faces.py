def reconhecer():
	# import the necessary packages
	from imutils import paths
	import face_recognition
	import argparse
	import pickle
	import cv2
	import os

	# construct the argument parser and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--dataset", required=True,
		help="path to input directory of faces + images")
	ap.add_argument("-e", "--encodings", required=True,
		help="path to serialized db of facial encodings")
	ap.add_argument("-d", "--detection-method", type=str, default="cnn",
		help="face detection model to use: either `hog` or `cnn`")
	args = vars(ap.parse_args())

	# grab the paths to the input images in our dataset
	print("[INFO] quantifying faces...")
	imagePaths = list(paths.list_images(args["dataset"]))

	# initialize the list of known encodings
	knownEncodings = []

	# loop over the image paths
	for (i, imagePath) in enumerate(imagePaths):
		# load the input image and convert it from RGB (OpenCV ordering)
		# to dlib ordering (RGB)
		image = cv2.imread(imagePath)
		rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

		# detect the (x, y)-coordinates of the bounding boxes
		# corresponding to each face in the input image
		boxes = face_recognition.face_locations(rgb,
			model=args["detection_method"])

		# compute the facial embedding for the face
		encodings = face_recognition.face_encodings(rgb, boxes)

		# loop over the encodings
		for encoding in encodings:
			# add each encoding to our set of known and
			# encodings
			knownEncodings.append(encoding)

	# dump the facial encodings to disk
	print("[INFO] serializing encodings...")
	data = {"encodings": knownEncodings}
	f = open(args["encodings"], "wb")
	f.write(pickle.dumps(data))
	f.close()
