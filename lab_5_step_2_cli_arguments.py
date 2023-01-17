'''
To run the program, enter the following command in the terminal:
python lab_5_step_2_cli_arguments.py --text "we are learning python on AWS" --source-language-code en --target-language-code fr

We have added the parameters on the command line.
Each parameter relates to each block for parser.add_argument

What did we do?
We imported a python package called argparse using import argparse
We created an ArgumentParser object which holds the information necessary to parse the command line into python data types
We used parser.add_argument() to add each of the arguments. This has the following syntax

Argument name for example --text
The dest is required to make it a value keyword argument accepted by the parameter, otherwise it will use the default argument text="value" which should be Text="value"
type is the data type which in this case is a string (str)
help is the help text shown
args = parser.parse_args() will inspect the command line, convert each argument to the appropriate type and then invoke the appropriate action

Now when we call the translate_text() function we need to use **vars(args). The **vars turns our object created by args = parser.parse_args() into a dictionary object which we can pass as key\:value pairs to our function
Python used the arguments we provided as key\:value pairs. It passed them to the translate_text() function.
'''


import argparse # argparse is a built in python package, we add it with an import statement
import boto3

# Define the parser variable to equal argparse.ArgumentParser()
parser = argparse.ArgumentParser(description="Provides translation between one source language and another of the same set of languages.")

# Add each of the arguments using the parser.add_argument() method
parser.add_argument(
    '--text',
    dest="Text",
    type=str,
    help="The text to translate. The text string can be a maximum of 5,000 bytes long. Depending on your character set, this may be fewer than 5,000 characters",
    required=True
    )

parser.add_argument(
    '--source-language-code', 
    dest="SourceLanguageCode", 
    type=str, 
    help="The language code for the language of the source text. The language must be a language supported by Amazon Translate.",
    required=True
    )

parser.add_argument(
    '--target-language-code',
    dest="TargetLanguageCode",
    type=str,
    help="The language code requested for the language of the target text. The language must be a language support by Amazon Translate.",
    required=True
    )

# This will inspect the command line, convert each argument to the appropriate type and then invoke the appropriate action.
args = parser.parse_args()

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

def main():
    # vars() is an inbuilt function which returns a dictionary object
    translate_text(**vars(args))

if __name__=="__main__":
    main()
