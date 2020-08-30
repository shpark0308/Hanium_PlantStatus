#from django.shortcuts import render #####
from django.shortcuts import render,redirect,get_object_or_404 #####
from watson_developer_cloud import VisualRecognitionV3
import json
from django.http import HttpResponseRedirect,JsonResponse
from django.views import View
from .forms import ImageFileUploadForm
from .models import Profile #####
from django.urls import reverse
from django.template.response import TemplateResponse

page=True
name_code='0'
class_name = ""
name_code=""

def index(request):
    global page
    global name_code
    global class_name
    plant = Profile()
    if request.method == 'POST':
        page = False
        form = ImageFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            plant.photo = request.FILES['photo'] ##
            form.save()
            form.fields
            visual_recognition = VisualRecognitionV3(
                '2018-03-19',
                iam_apikey='7e0uAeqtZc2Pze2-q2_IvRl_rlIAYTOKag0a_L3AiBgS'
                ##iam_apikey='16k-9xoYNypOiBsEQbsFkx3KbEcuYNDLcoMy9dd4Arbu'
                )
            url_list = [image_path for image_path in Profile.objects.values_list('photo',flat=True)]
            print('media/'+url_list[-1])
            with open('media/'+url_list[-1], 'rb') as images_file:
                classes = visual_recognition.classify(
                images_file,
                threshold='0.6',
                classifier_ids='PLANT_598641307').get_result()
            print(json.dumps(classes, indent=2))
            classify_name = classes['images'][0]['classifiers'][0]['classes'][0]
            class_name = str(classify_name).split("'")[3].split(".")[0]
            if (class_name=='Basil'):
                name_code='1'
            elif (class_name=='Tomato'):
                name_code='2'    
            return JsonResponse({'error': False, 'message': 'Uploaded Successfully'})
        else:
            return JsonResponse({'error': True, 'errors': form.errors})
    else:
        form = ImageFileUploadForm()
        if page==False:
            page=True
            return redirect('/detail1/'+name_code)
        elif page==True:
            return render(request, 'plantism/index.html', {'form': form})

def detail1(request, number):
    args = {}
    url_list = [image_path for image_path in Profile.objects.values_list('photo',flat=True)]
    if (number==1):
        visual_recognition = VisualRecognitionV3(
        '2018-03-19',
        ##iam_apikey='7e0uAeqtZc2Pze2-q2_IvRl_rlIAYTOKag0a_L3AiBgS'
        iam_apikey='16k-9xoYNypOiBsEQbsFkx3KbEcuYNDLcoMy9dd4Arbu'
        )
        with open('media/'+url_list[-1], 'rb') as images_file:
            classes = visual_recognition.classify(
            images_file,
            threshold='0.0',
            classifier_ids='DefaultCustomModel_1951264680').get_result()
        print(json.dumps(classes, indent=2))
        classify_name1 = int(classes['images'][0]['classifiers'][0]['classes'][0]['score'] *100)
        classify_name2 = int(classes['images'][0]['classifiers'][0]['classes'][1]['score'] *100)
        classify_name3 = int(classes['images'][0]['classifiers'][0]['classes'][2]['score'] *100)
        classify_name4 = int(classes['images'][0]['classifiers'][0]['classes'][3]['score'] *100)
        ##class_name = str(classify_name).split("'")[3].split(".")[0]
        print("죽음 : "+str(classify_name1)+"건조"+str(classify_name2)+"신선도"+str(classify_name3)+"물부족"+str(classify_name4))
    elif (number==2):
        visual_recognition = VisualRecognitionV3(
            '2018-03-19',
            ##iam_apikey='7e0uAeqtZc2Pze2-q2_IvRl_rlIAYTOKag0a_L3AiBgS'
            iam_apikey='xdAs0uBqDWeP_X5PuqcsOwrvVR46OlbUP4Opf5-gS3kg'
            )
        with open('media/'+url_list[-1], 'rb') as images_file:
            classes = visual_recognition.classify(
            images_file,
            threshold='0.0', # threshold에 따라 달라진다 -> 0.6으로 고치기 -> 일단 모든 데이터를 불러오기를 시작하기
            #classifier_ids='PLANT_598641307').get_result()
            classifier_ids='Tomato2_1209706610').get_result()
        print(json.dumps(classes, indent=2))
        classify_name1 = int(classes['images'][0]['classifiers'][0]['classes'][0]['score'] *100)
        classify_name2 = int(classes['images'][0]['classifiers'][0]['classes'][1]['score'] *100)
        classify_name3 = int(classes['images'][0]['classifiers'][0]['classes'][2]['score'] *100)
        classify_name4 = int(classes['images'][0]['classifiers'][0]['classes'][3]['score'] *100)
    args['classify1'] = classify_name1
    args['classify2'] = classify_name2
    args['classify3'] = classify_name3
    args['classify4'] = classify_name4
    template_name = 'plantism/index2.html'
    return TemplateResponse(request, template_name,args)

