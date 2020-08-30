from watson_developer_cloud import VisualRecognitionV3
import json


visual_recognition = VisualRecognitionV3(
        '2018-03-19',
        iam_apikey='7e0uAeqtZc2Pze2-q2_IvRl_rlIAYTOKag0a_L3AiBgS'
        
    )
    
with open('image/dry2.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
    classifier_ids='default').get_result()

print(json.dumps(classes, indent=2))        

