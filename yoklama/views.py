import json

import PIL
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import cv2
import face_recognition
import os
import numpy as np

# from PIL import Image
# from io import StringIO
# r = requests.get('https://example.com/image.jpg')
# i = Image.open(StringIO(r.content))

from django.views import View
from django.views.generic import TemplateView

class YoklamaView(TemplateView):

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        name = f_rec(file)

        context = {
            'status': name
        }

        return JsonResponse(context)
        # return HttpResponse(file.read(), content_type="image/png")

#
# class NameView(View):
#     def post(self, request, *args, **kwargs):
#         data = request.body
#         data = json.loads(data)
#         name = data['name']
#         return JsonResponse({"data": "Hello "+ name})

def f_rec(file):

    # imgElon = face_recognition.load_image_file('static/ImagesAttendance/Jack_Ma.jpg')
    # imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
    #
    # # imgTest = face_recognition.load_image_file('static/ImagesBasic/Elon_Musk_Test.jpg')
    # # imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
    #
    # imgBill = face_recognition.load_image_file(file)
    # imgBill = cv2.cvtColor(imgBill, cv2.COLOR_BGR2RGB)
    #
    # # faceLocElon = face_recognition.face_locations(imgElon)[0]
    # encodeElon = face_recognition.face_encodings(imgElon)[0]
    # # cv2.rectangle(imgElon, (faceLocElon[3], faceLocElon[0]), (faceLocElon[1], faceLocElon[2]), (255, 0, 255), 2)
    #
    # # faceLocTest = face_recognition.face_locations(imgTest)[0]
    # # encodeTest = face_recognition.face_encodings(imgTest)[0]
    # # cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)
    #
    # # faceLocBill = face_recognition.face_locations(imgBill)[0]
    # encodeBill = face_recognition.face_encodings(imgBill)[0]
    # # cv2.rectangle(imgBill, (faceLocBill[3], faceLocBill[0]), (faceLocBill[1], faceLocBill[2]), (255, 0, 255), 2)
    # # cv2.rectangle(imgBill, (faceLocBill[3], faceLocBill[0]), (faceLocBill[1], faceLocBill[2]), (255, 255, 0), 2)
    #
    # result = face_recognition.compare_faces([encodeElon], encodeBill)
    # faceDis = face_recognition.face_distance([encodeElon], encodeBill)
    # print(result, faceDis)
    #
    # # cv2.putText(encodeBill, f'{result}, {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255),
    # #             2)
    # #
    # # cv2.imshow('Elon Musk', imgElon)
    # # cv2.imshow('Bill Gates', imgBill)
    # # cv2.waitKey(1)

    path = 'static/ImagesAttendance'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)

    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    encodeListKnown = findEncodings(images)
    print(len(encodeListKnown))

    while True:

        imgS = face_recognition.load_image_file(file)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
            maches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if maches[matchIndex]:
                name = classNames[matchIndex].upper()
                print(name)
                if name != "":
                    return name
