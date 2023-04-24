#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import sqlite3

# Function to create a SQLite database and table
def create_db():
    conn = sqlite3.connect('python_blogs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS blogs
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT NOT NULL,
                 author TEXT NOT NULL,
                 content TEXT NOT NULL);''')
    conn.commit()
    conn.close()

# Function to scrape Python blogs and save data to the database
def scrape_and_save_to_db():
    url = 'https://example.com/python-blogs/' # Replace with the actual URL of the Python blogs
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    blogs = soup.find_all('div', {'class': 'blog'}) # Replace with the actual HTML structure of the blogs

    conn = sqlite3.connect('python_blogs.db')
    c = conn.cursor()

    for blog in blogs:
        title = blog.find('h2').text.strip()
        author = blog.find('span', {'class': 'author'}).text.strip()
        content = blog.find('div', {'class': 'content'}).text.strip()

        c.execute("INSERT INTO blogs (title, author, content) VALUES (?, ?, ?)",
                  (title, author, content))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()
    scrape_and_save_to_db()
    print('Scraping and data insertion complete.')


# In[ ]:




