# 📱 Smartphone Data Analysis Project

An end-to-end data analysis project where I scraped, cleaned, and analyzed real-world smartphone listing data from a public e-commerce site for **educational purposes only**.

---

## 🚀 Project Overview

This project walks through the **entire data analysis pipeline**:

1. **Web Scraping** – Automating browser actions and extracting HTML data  
2. **Data Accessing & Structuring** – Organizing raw data, identifying structural & quality issues  
3. **Data Cleaning & Preprocessing** – Standardizing, cleaning, and transforming messy data  
4. **Exploratory Data Analysis (EDA)** – Deriving insights through analysis and visualizations

---

## 🔍 1. Web Scraping

- **Tools Used**: `Selenium`, `BeautifulSoup`, `pandas`
- Extracted smartphone product listings (brand, RAM, storage, screen size, price, etc.)
- Handled dynamic loading using Selenium before parsing with BeautifulSoup

> ⚠️ **Note**: The data was scraped from a publicly available e-commerce website **without using an official API or obtaining explicit permission.**  
> It is used here **strictly for personal learning and educational purposes only**, and not for any commercial use or redistribution.

---

## 📂 2. Data Accessing & Structuring

- Separated data into:
  - 🧱 **Messy data**: Structural issues (inconsistent formatting, merged fields)
  - 🧪 **Dirty data**: Quality issues (null values, typos, inconsistent units)
- Organized scraped data into structured `pandas` DataFrames
- Stored both raw and cleaned data for reproducibility

---

## 🧹 3. Data Cleaning & Preprocessing

Cleaning was the most time-consuming part. Tasks included:

- 🔄 Standardizing formats (e.g., `"6.5 inches"` → `6.5`)  
- 🧽 Handling variations like `"128 GB"`, `"128 gb"`, `"128GB"`  
- 🚫 Removing HTML tags, junk symbols, invisible Unicode  
- 🧵 Dealing with missing values and transforming types (e.g., strings → floats)

---

## 📊 4. Exploratory Data Analysis (EDA)

- Analyzed brand frequency  
- Explored distributions of price, RAM, screen size, etc.  
- Visualized relationships between specs and price  
- Detected outliers and inconsistent entries

---

## 🛠️ Technologies Used

- **Python**  
- **Selenium**  
- **BeautifulSoup**  
- **Pandas**  
- **Regex**  
- **Matplotlib / Seaborn**

---

## 🧠 Key Takeaways

- Real-world data is rarely clean — expect **messy + dirty** formats  
- **Data cleaning** is a critical (and time-consuming) step in any project  
- Practicing web scraping + cleaning + EDA strengthens your real-world problem-solving skills

---

## 📌 Future Improvements

- Add visual storytelling with **Power BI dashboards**  
- Automate multi-page scraping with more robust logic  
- Expand to include product reviews or ratings (if available)

---

## ⚖️ Disclaimer

This project is intended **solely for educational and personal learning purposes**.

- The data was scraped from a public website **without explicit permission**
- It is **not intended for commercial use**, distribution, or any form of monetization
- If you are the owner of the content and have concerns, feel free to contact me — I’ll be happy to take down or update the project accordingly

---

## 🤝 Connect With Me

- **LinkedIn**: [www.linkedin.com/in/arpit-waghamare]
- **GitHub**: [Your GitHub URL]

Let’s connect and grow together 🚀

