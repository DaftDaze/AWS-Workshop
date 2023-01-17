
import boto3

session = boto3.session.Session(profile_name='temp') # use this line with line 6 if using aws profile other than default
#client = boto3.client('translate')
client = session.client('translate')

def translate_text(): 
    response = client.translate_text(
        Text='I am learning to code in AWS', 
        SourceLanguageCode='en', 
        TargetLanguageCode='fr' 
    )
#### Add the new text below this line ####
    print(response) # this code is inside the function and will print the contents of the variable 'response' 

translate_text() # This line will call our function. Without it, python will not do anything.
