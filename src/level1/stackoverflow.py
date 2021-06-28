import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
}

url = 'https://stackoverflow.com/questions'

r = requests.get(url, headers=headers)

parser = BeautifulSoup(r.text)

questions_container = parser.find(id='questions')
questions_list = questions_container.find_all('div', class_='question-summary')
for question in questions_list:
    question_element = question.find('h3')
    question_element_text = question_element.text

    # Looking by sibling
    question_description = question_element.find_next_sibling('div').text.strip()

    # question_text = question.find('h3').text.strip()
    # Looking using beautiful soup
    # question_description = question.find('div', class_='excerpt').text.strip()
    print('QUESTION: ', question_element_text)
    print('DESCRIPTION: ', question_description, '\n', '\n')

