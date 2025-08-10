from django.shortcuts import render
from django.contrib import messages
import requests
import os

def home(request):
    return render(request, 'main/home.html')

def about(request):
    about_text = ""
    try:
        with open("main/about_me.txt", encoding="utf-8") as f:
            about_text = f.read()
    except Exception:
        about_text = "About Me text not found."
    return render(request, 'main/about.html', {"about_text": about_text})


def skills(request):
    skills_list = []
    skills_file = os.path.join(os.path.dirname(__file__), 'skills.txt')
    with open(skills_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                parts = line.strip().split(',')
                if len(parts) == 2:
                    skills_list.append({'skill': parts[0], 'image': parts[1]})
    return render(request, 'main/skills.html', {'skills': skills_list})

def projects(request):
    response = requests.get('http://fastapi:8001/projects')
    print(response)
    if response.status_code == 200:
        data = response.json()
    else:
        data = []
        print("Failed to fetch projects:", response.text)
        messages.error(request, f"Failed to fetch projects due to: {response.text}")
    return render(request, 'main/projects.html', {'projects': data})

def contact(request):
    return render(request, 'main/contact.html')

def certificates(request):
    response = requests.get('http://fastapi:8001/certificates')
    print(response)
    if response.status_code == 200:
        data = response.json()
    else:
        data = []
        print("Failed to fetch certificates:", response.text)
        messages.error(request, f"Failed to fetch certificates due to: {response.text}")
    return render(request, 'main/certificates.html', {'certificates': data})

def skills(request):
    response = requests.get('http://fastapi:8001/skills')
    print(response)
    if response.status_code == 200:
        data = response.json()
    else:
        data = []
        print("Failed to fetch skills:", response.text)
        messages.error(request, f"Failed to fetch skills due to: {response.text}")
    return render(request, 'main/skills.html', {'skills': data})


def contact(request):
    return render(request, 'main/contact.html')