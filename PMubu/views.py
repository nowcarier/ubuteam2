from django.shortcuts import render


def index(req):
    '''
    UBUteam2
    1234567890-=
    pip3 install firebase
    pip3 install gcloud
    pip3 install python_jwt
    pip3 install sseclient
    pip3 install pycrypto
    pip3 install requests-toolbelt
    '''

    # from firebase import firebase
    # firebase = firebase.FirebaseApplication('https://flutter-f50ea.firebaseio.com', None)
    # result = firebase.get('/data', 'no1')
    # print(result)
    
    return render(req,'index.html')

# Create your views here.
