import requests
import torch
import tkinter as tk
from tkinter import ttk, messagebox
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_articles(articles):
    analyzed_articles = []

    for article in articles:
       
        title_tensor = torch.tensor([len(article['title']), article['dateAdded'].count('-')])

       
        article['title_tensor'] = title_tensor.numpy()
        article['date'] = article['dateAdded']
        analyzed_articles.append(article)

    return analyzed_articles


def visualize_tensor(analyzed_articles):
    sns.set(style="whitegrid")
    
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='date', y='title_tensor', data=pd.DataFrame(analyzed_articles), ax=ax)
    
    ax.set_title("Visualization of Title Tensor over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Tensor Value")
    plt.xticks(rotation=45)
    
    plt.show()


def main():
    username = input("Enter the username to retrieve articles: ")

    try:
        articles = extract_articles(username)
        analyzed_articles = analyze_articles(articles)
        visualize_tensor(analyzed_articles)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
