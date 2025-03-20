# Simple-NLP-projects
This repository contains simple NLP projects. 
It includes:  Language detection ,Spam message detection,  Suspicious URL detection  ,Obfuscated JavaScript detection

## Language Detection:
- **Notebook**: [Language Detection Model Development](https://github.com/KaushiML3/Simple-NLP-projects/blob/main/notebooks/Language%20_detection%20_model.ipynb)
- This project uses Natural Language Processing (NLP) techniques to automatically detect the language of a given text. It leverages algorithms such as Naive Bayes or FastText to classify text into various 22 language categories. This system is helpful in automating the process of multilingual content management, enabling applications to dynamically adapt to the language of the user. It can be integrated into various platforms to enhance user experience through automatic language localization.
- Naive Bayes model evaluation matrix
![image](https://github.com/KaushiML3/Simple-NLP-projects/blob/main/assets/language.png)
  
## Spam Message Detection:
- **Notebook**: [Spam Message Detection Model Development](https://github.com/KaushiML3/Simple-NLP-projects/blob/main/notebooks/Spam_massage_Detection_LSTM.ipynb)
- The Spam Message Detection system uses text classification techniques to distinguish between spam and non-spam (ham) messages. It involves training a machine learning model (LSTM) on labeled message data. This model identifies patterns and features specific to spam messages, such as common words or phrases, suspicious links, or frequent email addresses. The system can be applied to email clients, chat applications, and messaging platforms to filter out unwanted content, improving security and user experience.
- LSTM model evaluation matrix
![image](https://github.com/KaushiML3/Simple-NLP-projects/blob/main/assets/spam.png)

## Suspicious URL Detection:
- **Notebook**: [Suspicious URL Detection Model Development](https://github.com/KaushiML3/Simple-NLP-projects/blob/main/notebooks/URL_detection.ipynb)
- This project focuses on detecting malicious or suspicious URLs using machine learning or rule-based methods. By analyzing various features like domain name, URL structure, and the presence of red-flag keywords, the system classifies whether a URL is harmful or safe. Techniques such as Decision Trees, Random Forests, or Deep Learning models are trained on a labeled dataset of safe and phishing URLs. This project can be used in web security applications, browser extensions, or network security tools to protect users from phishing attacks, malware, and other cyber threats.
- Random forest model evaluation matrix
![image](https://github.com/KaushiML3/Simple-NLP-projects/blob/main/assets/url_random%20forest.png)

- XBoost model evaluation matrix
![image](https://github.com/KaushiML3/Simple-NLP-projects/blob/main/assets/url%20Xboost.png)

## Obfuscated JavaScript Detection:
- **Notebook**: [Obfuscated JavaScript Detection Model Development](https://github.com/KaushiML3/Simple-NLP-projects/blob/main/notebooks/obfuscationjs-detection.ipynb)
- The Obfuscated JavaScript Detection project aims to identify JavaScript code that has been intentionally obfuscated to hide malicious intent. The system analyzes JavaScript code by inspecting patterns, variable names, and suspicious encoding methods. Using techniques like Static Code Analysis, Machine Learning, or even Regular Expressions, the model can flag obfuscated scripts that could potentially be harmful (e.g., for executing malware or phishing attacks). This can be integrated into security tools to help developers and security analysts automatically detect and mitigate the risk posed by obfuscated code.Use the XGB classifire and Logistic classifire to developed this.
- XGB model evaluation matrix
![image](https://github.com/KaushiML3/Simple-NLP-projects/blob/main/assets/js.png)
