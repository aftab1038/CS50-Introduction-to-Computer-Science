# Quiz App
#### Video Demo:  <https://www.youtube.com/watch?v=7So3it7kVtM&ab_channel=%C3%82Ftab%C3%91aFees>
#### Description:

This is a GUI application made in Python using the Tkinter library and open trivia database.

#### what this wil do do after running the appication:

when you run main.py, it displays questions and asks the user whether it is true or false. If the user enters the correct answer, it turns green and for the wrong answer, it turns red. and when 10 questions are done by the user, it ends the quiz and shows the score to the user.

#### Files and their function in the project: 

1. image folder: 
    * it contains two images 
    * one of tick for true  
    * the other cross for false.

2. app.py:
    * This file is the main application script.
    * It imports the Question class from question_model, the list of questions (question_data) from data, the QuizBrain class from quiz_brain, and the QuizUserInterface class from ui.
    * It creates a list called question_bank by iterating through question_data and creating Question objects.
    * Instances of QuizBrain and QuizUserInterface are created, passing the question_bank as an argument to QuizBrain.

3. data.py:
    * Handles the retrieval of quiz questions from the Open Trivia Database API.
    * Imports the requests module.
    * Defines a dictionary named parameters containing parameters for the API request.
    *Sends a request to the API, retrieves question data, and stores it in question_data.

4. question_model.py:
    * Defines a class named Question.
    * The class has an __init__ method that initializes instances with question text (q_text) and the correct answer (q_answer).

5. quiz_brain.py:
    * Imports necessary modules and classes.
    * Defines a class named QuizBrain that manages the quiz state and logic.
    * Includes methods for resetting the quiz, checking if there are more questions, getting the next question, and checking user answers.
    * The class has a method (reset_quiz) to fetch a new set of questions from the API and convert them into Question objects.

6. ui.py:
    * Contains the user interface code using Tkinter for the Quiz App.
    * Defines a class named QuizUserInterface that manages the GUI.
    * The GUI includes a canvas for displaying questions, buttons for True and False answers, and a popup to show the final score.
    * Methods handle displaying questions, checking answers, and providing feedback.
    * The UI is designed with a responsive canvas size that adjusts based on the length of the question text.

#### How to run this application:

1. download python in your computer
2. install the python in your computer
3. after that check that python is sucuessfully install or not
4. do check, open command prompt in your computer as adminstrator and run a command "python --version"
5. if it show python with its version at mean python is install successfully
6. now you have to open terminal in project folder and run another commmand "pip install requests"
7. and after that all, now run a last command "python app.py" in that terminal , and it will pop up a new window and start the Quizz

#### Tools used in this project are :

1. Python:
    * The core programming language used for writing the entire application.

2. Tkinter:
    * A standard GUI (Graphical User Interface) toolkit for Python. It is used in the ui.py file to create the graphical interface for the Quiz App.

3. Requests:
    * A popular Python library for making HTTP requests. It is utilized in the data.py file to fetch quiz questions from the Open Trivia Database API.

4. Open Trivia Database API:
    * An external API used to obtain trivia questions for the quiz. The data.py file utilizes the API through the requests library to retrieve a set of questions.

5. HTML module:
    * The html module is used to unescape HTML entities in the quiz_brain.py file. This is important when handling text retrieved from the Open Trivia Database API.

6. Random module:
    * The random module is used in the quiz_brain.py file to shuffle the order of questions fetched from the API.

7. Image files:
    * Image files (e.g., "true.png" and "false.png") are used for buttons in the GUI. These images are referenced in the ui.py file.




