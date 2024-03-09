# OCA - Offensive Cybersecurity Assistant
from openai import OpenAI
import os
import subprocess
import sys
import re
from EnvironmentMeta import GetEnvironmentMeta
from CleaningFunctions import GetCleaningFunctions
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-g", nargs='?', help="General Assistant", type=int, default=0)
parser.add_argument("-t", nargs='?', help="Terminal Assistant", type=int, default=0)
parser.add_argument("-c", nargs='?', help="Consultant", type=int, default=0)

args = parser.parse_args()

class Oca:
    def __init__(self):
        self.client = OpenAI()

    def start_chat(self,chat_type):
        while True:
            input_type = chat_type
            if(input_type.lower() == "t"):
                user_input = input("terminal")
                if user_input.lower() == 'e' or user_input.lower() == 'q' or user_input.lower() == 'exit':
                    print("I will take my leave Sire.")
                    break
                if user_input.lower() == 'g':
                    chat_type = 'g'
                    continue
                if user_input.lower() == 'c':
                    chat_type = 'c'
                    continue
            elif(input_type.lower() == "g"):
                user_input = input("general")
                if user_input.lower() == 'e' or user_input.lower() == 'q' or user_input.lower() == 'exit':
                    print("It has been an honour to serve.")
                    break
                if user_input.lower() == 't':
                    chat_type = 't'
                    continue
                if user_input.lower() == 'c':
                    chat_type = 'c'
                    continue
            elif(input_type.lower() == "c"):
                user_input = input("consult: ")
                if user_input.lower() == 'e' or user_input.lower() == 'q' or user_input.lower() == 'exit':
                    print("My usefulness is at an end.")
                    break
                if user_input.lower() == 't':
                    chat_type = 't'
                    continue
                if user_input.lower() == 'g':
                    chat_type = 'g'
                    continue

if __name__ == "__main__":
    oca_term = Oca()
    oca_term.start_chat("t")
