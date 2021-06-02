import face_recognition

def face_rec():
    imgElon = face_recognition.load_image_file('ImagesBasic/Elon_Musk.jpg')
    imgElonLocation = face_recognition.face_locations(imgElon)

    imgTest = face_recognition.load_image_file('ImagesBasic/Elon_Musk_Test.jpg')
    imgTestLocation = face_recognition.face_locations(imgTest)

    imgBill = face_recognition.load_image_file('ImagesBasic/elon_and.jpeg')
    imgBillLocation = face_recognition.face_locations(imgBill)



def main():
    face_rec()

if __name__ == '__name__':
    main()
