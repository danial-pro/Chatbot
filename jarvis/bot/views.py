from django.shortcuts import render
import requests

SaveChat=[]
botchat=[]

def home(request):
  userpost = 'hey'
  if request.method == "POST":
    userpost =request.POST['myvalue']
  print(userpost)
  url='https://api.dialogflow.com/v1/query?v=20150910&contexts=jarvis&lang=en&query='+userpost+'&sessionId=12345&timezone=America/New_York'
  Headers = {
    'Authorization': 'Bearer 9913fcc266e84b92a3990a1ce6818e74',
  } 
  r =requests.get(url, headers=Headers)
  print("The response", r.json()['result']['fulfillment']['speech'])
  SaveChat.append("Customer: "+userpost)
  SaveChat.append("Jarvis: "+r.json()['result']['fulfillment']['speech'])
  UserChat={'Chat1': SaveChat}

  # rendering the template in templates folder
  return render(request, "app.html",UserChat )
