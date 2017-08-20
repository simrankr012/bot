# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import generic
from pprint import pprint
import json,random,re,requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from pymessenger.bot import Bot
from chintent import check_intent


PAGE_ACCESS_TOKEN = "EAABlZCeiOMsYBAE2ZBRovKUy1g890Q8v6TvLRpBfVb5t0zZBw8WQNB3GvczZCssClxphSikY9vYOfdTYa51dH9zNO8g5ZAnSOuTDbAZCqsycSR1GZCzvkGhKQ1sMY27yIlpwDqZBpo6aijG5J9CZB3ZB2HmkDf8OiNF0v4eYEtaFYW8wZDZD"
VERIFY_TOKEN = "01081996"

def post_emer_loc(fbid):
    
    string="please send your location"
    
    user_details_url = "https://graph.facebook.com/v2.10/%s"%fbid 
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':PAGE_ACCESS_TOKEN} 
    user_details = requests.get(user_details_url, user_details_params).json() 
    # joke_text = 'Yo '+ joke_text
    post_message_url = 'https://graph.facebook.com/v2.10/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
                    
    

    
    response_msg = json.dumps(
                    {
                        "recipient":
                            {
                                "id":fbid
                            }, 
                        "message":
                            {
                                "text":string,
                                "quick_replies":[
                                 {
                                
                                
                               
                               "content_type":"location",
                               }
                                ,]
                            }
                            })
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    

def post_facebook_message(fbid, text):
    
    user_details_url = "https://graph.facebook.com/v2.10/%s"%fbid 
    print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':PAGE_ACCESS_TOKEN} 
    user_details = requests.get(user_details_url, user_details_params).json() 
    # joke_text = 'Yo '+ joke_text
    post_message_url = 'https://graph.facebook.com/v2.10/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    
    if text == "quickreply":
        response_msg = json.dumps(
                            {
                                "recipient":
                                    {
                                        "id":fbid
                                   }, 
                                "message":
                                    {
                                        "text":"Please Select Your Options",
                                        "quick_replies":[
                                         {
                                        
                                        "title":"Emergency",
                                       
                                       "content_type":"text",
                                       "payload":"Emergency_Payload"
                                       

                                       }
                                        ,
                                    {
                                          "content_type":"text",
                                          "title":"Disease",
                                          "payload":"Disease_Payload"
                                          },
                                        

                                 ]
                                    }
                                    })
        status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)    
    else:
        response_msg = json.dumps(
                        {
                            "recipient":
                                {
                                    "id":fbid
                               }, 
                            "message":
                                {
                                    "text":text,
                                    
                                }
                        })
    
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)

# def send_button_message(fbid):
        
#     user_details_url = "https://graph.facebook.com/v2.10/%s"%fbid 
#     user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':PAGE_ACCESS_TOKEN} 
#     user_details = requests.get(user_details_url, user_details_params).json() 
#     # joke_text = 'Yo '+ joke_text
#     post_message_url = 'https://graph.facebook.com/v2.10/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
#     text="alzeihmer"
#     response_msg=json.dumps({
#             'recipient': {
#                 'id': recipient_id
#             },
#             'message': {
#                 "attachment": {
#                     "type": "template",
#                     "payload": {
#                         "template_type": "generic",
#                         "elements":[
           
#           {
#             "title":"Welcome to Peter\'s Hats",
#             "image_url":"https://petersfancybrownhats.com/company_image.png",
#             "subtitle":"We\'ve got the right hat for everyone.",
#             "default_action": {
#               "type": "web_url",
#               "url": "https://peterssendreceiveapp.ngrok.io/view?item=103",
#               # "messenger_extensions": True,
#               "webview_height_ratio": "tall",
#               # "fallback_url": "https://7104a33d.ngrok.io/"
#             },
#             "buttons":[
#               {
#                 "type":"web_url",
#                 "url":"https://facebook.com",
#                 "title":"View Website"
#               },{
#                 "type":"postback",
#                 "title":"Start Chatting",
#                 "payload":"DEVELOPER_DEFINED_PAYLOAD"
#               }              
#             ]      
#           },
#           {
#             "title":"Welcome to Peter\'s Hats",
#             "image_url":"https://petersfancybrownhats.com/company_image.png",
#             "subtitle":"We\'ve got the right hat for everyone.",
#             "default_action": {
#               "type": "web_url",
#               "url": "https://peterssendreceiveapp.ngrok.io/view?item=103",
#               # "messenger_extensions": True,
#               "webview_height_ratio": "tall",
#               # "fallback_url": "https://7104a33d.ngrok.io/"
#             },
#             "buttons":[
#               {
#                 "type":"web_url",
#                 "url":"https://facebook.com",
#                 "title":"View Website"
#               },{
#                 "type":"postback",
#                 "title":"Start Chatting",
#                 "payload":"DEVELOPER_DEFINED_PAYLOAD"
#               }              
#             ]      
#           }

#         ]
#         }
#         }
#         }
#         })

#     status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg) 
def post_facebook_location(fbid,rlat,rlong):

    user_details_url = "https://graph.facebook.com/v2.10/%s"%fbid
    user_details_params = {'fields':'first_name,last_name,profile_pic', 'access_token':PAGE_ACCESS_TOKEN} 
    user_details = requests.get(user_details_url, user_details_params).json() 
    print(fbid)               
    post_message_url = 'https://graph.facebook.com/v2.10/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
    response_msg =json.dumps({
            'recipient': {
                'id': fbid
            },
            'message': {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements":[
           
          {
            "title":"Welcome to Peter\'s Hats",
            "image_url":"https://petersfancybrownhats.com/company_image.png",
            "subtitle":"We\'ve got the right hat for everyone.",
            "default_action": {
              "type": "web_url",
              "url": "https://peterssendreceiveapp.ngrok.io/view?item=103",
              # "messenger_extensions": True,
              "webview_height_ratio": "tall",
              # "fallback_url": "https://7104a33d.ngrok.io/"
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://facebook.com",
                "title":"View Website"
              },{
                "type":"postback",
                "title":"Start Chatting",
                "payload":"DEVELOPER_DEFINED_PAYLOAD"
              }              
            ]      
          },
          {
            "title":"Welcome to Peter\'s Hats",
            "image_url":"https://petersfancybrownhats.com/company_image.png",
            "subtitle":"We\'ve got the right hat for everyone.",
            "default_action": {
              "type": "web_url",
              "url": "https://peterssendreceiveapp.ngrok.io/view?item=103",
              # "messenger_extensions": True,
              "webview_height_ratio": "tall",
              # "fallback_url": "https://7104a33d.ngrok.io/"
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://facebook.com",
                "title":"View Website"
              },{
                "type":"postback",
                "title":"Start Chatting",
                "payload":"DEVELOPER_DEFINED_PAYLOAD"
              }              
            ]      
          }

        ]
        }
        }
        }
        })
 
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    pprint(status.json())

# Create your views here.
class HEBot104View(generic.View):
    def get(self, request, *args, **kwargs):
        post_message_url ='https://graph.facebook.com/v2.10/me/messenger_profile?fields=get_started&access_token=%s'%PAGE_ACCESS_TOKEN    
        status = requests.get(post_message_url, headers={"Content-Type": "application/json"})
        if self.request.GET.get('hub.verify_token') == VERIFY_TOKEN:             
            return HttpResponse(self.request.GET['hub.challenge'])   
        else:    
            return HttpResponse('Error, invalid token')        
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    # Post function to handle Facebook messages
    def post(self, request, *args, **kwargs):
        # Converts the text payload into a python dictionary
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        # Facebook recommends going through every entry since they might send
        # multiple messages in a single call during high load
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    pprint(message)
                    
                    try: 
                        help_command = (message['message']['text']).lower()
                        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                        text = check_intent(help_command)
                        print text
                        
                        post_facebook_message(message['sender']['id'],text)

                    except:
                        pass
                if 'attachments' in message['message']:
                        ar=message['message']['attachments']
                        for j in ar:
                            content_type = j['type']
                            if content_type == 'location':
                                message_coordinates = (j['payload']['coordinates'])
                                latitude = message_coordinates['lat']
                                longitude = message_coordinates['long']
                                print(latitude,longitude)
                                post_facebook_location(message['sender']['id'], str (latitude), str( longitude))
                else:
                    pass    
        return HttpResponse() 


