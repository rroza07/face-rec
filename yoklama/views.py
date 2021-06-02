from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import cv2
import face_recognition

# from PIL import Image
# from io import StringIO
# r = requests.get('https://example.com/image.jpg')
# i = Image.open(StringIO(r.content))
from django.views.generic import TemplateView


class YoklamaView(TemplateView):

    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        # imgElon = face_recognition.load_image_file('static/ImagesBasic/Elon_Musk.jpg')
        # imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
        #
        # imgTest = face_recognition.load_image_file('static/ImagesBasic/Elon_Musk_Test.jpg')
        # imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
        #
        # imgBill = face_recognition.load_image_file(file.read())
        # imgBill = cv2.cvtColor(imgBill, cv2.COLOR_BGR2RGB)
        #
        # faceLocElon = face_recognition.face_locations(imgElon)[0]
        # encodeElon = face_recognition.face_encodings(imgElon)[0]
        # cv2.rectangle(imgElon, (faceLocElon[3], faceLocElon[0]), (faceLocElon[1], faceLocElon[2]), (255, 0, 255), 2)
        #
        # faceLocTest = face_recognition.face_locations(imgTest)[0]
        # encodeTest = face_recognition.face_encodings(imgTest)[0]
        # cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)
        #
        # faceLocBill = face_recognition.face_locations(imgBill)[0]
        # encodeBill = face_recognition.face_encodings(imgBill)[0]
        # cv2.rectangle(imgBill, (faceLocBill[3], faceLocBill[0]), (faceLocBill[1], faceLocBill[2]), (255, 0, 255), 2)
        # cv2.rectangle(imgBill, (faceLocBill[3], faceLocBill[0]), (faceLocBill[1], faceLocBill[2]), (255, 255, 0), 2)
        #
        # result = face_recognition.compare_faces([encodeElon], encodeBill)
        # faceDis = face_recognition.face_distance([encodeElon], encodeBill)
        # print(result, faceDis)
        #
        # cv2.putText(encodeBill, f'{result}, {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255),
        #             2)
        #
        # cv2.imshow('Elon Musk', imgElon)
        # cv2.imshow('Bill Gates', imgBill)
        # cv2.waitKey(0)
        #
        # print(file.name)  # Gives name
        # print(file.content_type)  # Gives Content type text/html etc
        # print(file.size)  # Gives file's size in byte
        # print(file.read())  # Reads file

        context = {
            'status': "true"
        }
        return JsonResponse(context)
        # return HttpResponse(file.read(), content_type="image/png")
