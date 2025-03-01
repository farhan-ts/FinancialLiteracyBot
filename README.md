# Financial Q&A Portal 💰❓

Welcome to the Financial Q&A Portal! This web application allows users to ask financial questions and receive expert answers, both in text and audio format. The application supports multiple languages and uses a pre-trained GPT-2 model to generate responses.

## Features ✨

- **Ask Financial Questions**: Users can submit their financial questions through a web form.
- **Expert Answers**: The application generates expert answers using a GPT-2 model.
- **Audio Responses**: Answers are also provided in audio format using Google Text-to-Speech (gTTS).
- **Language Detection**: The application detects the language of the question and responds accordingly.

## Technologies Used 🛠️

- **Flask**: Web framework for Python.
- **Transformers**: Library for state-of-the-art Natural Language Processing.
- **gTTS**: Google Text-to-Speech for generating audio responses.
- **Bootstrap**: Front-end framework for responsive design.
- **Font Awesome**: Icons for the web.

## Project Structure 📂
── answer.mp3 
├── app.py
 └── templates/ 
   └── index.html


## Setup and Installation 🚀

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/financial-qna-portal.git
    cd financial-qna-portal
    ```

2. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```sh
    python app.py
    ```

4. **Open your browser** and navigate to `http://127.0.0.1:5000/` to access the portal.

## Usage 📝

1. **Ask a Question**: Enter your financial question in the text area and submit the form.
2. **View the Answer**: The generated answer will be displayed on the page.
3. **Listen to the Answer**: An audio player will appear, allowing you to listen to the answer.

## Contributing 🤝

Contributions are welcome! Please fork the repository and submit a pull request.

## License 📄

This project is licensed under the MIT License.

