# Flask Module Templates

A flask module templates for fast development.

Note: If you want to contribute, please contact me in [messenger](https://www.messenger.com/t/100031409211694).

## 📖 Modules as Backend Developer
**Basic:**
* Session authentication [✓]
* Token authentication [✓]
* Form Validation [current]
* Database Management (Page) [✓]
* Database Management (Modal) (RESTful API) [✓]
* Date Manipulation [✓]
* String Manipulation [✓]
* Number Manipulation [?]
* Data Encryption [✓]
* File Upload [✓]
* Generate PDF [✓]
* Generate Excel [✓]
* Caching 

**Intermediate:**
* Chatbot (Scripted)
* Websocket
* Third-party Services:
  * Google Map
  * Mapbox
  * reCAPTCHA
  * Login with Facebook
  * Login with Google
  * ...
* ...

**Advance:** 
* Exception Handling
* ML algorithms:
  * Decision tree
  * Random forest
  * ...
* Face Recognition
* ...

**Expert:** 
* Machine learning integration
* Blockchain integration
* IOT integration
* ...

## 📋 Software Required
Windows:
* [python](https://www.python.org/downloads/)
* mysql from [xampp](https://www.apachefriends.org/), [wamp](https://www.wampserver.com/en/) or other sources that you know.

## 🏃 How to run?
Windows:
1. Make sure the requirements are installed and running.
2. Clone/download then extract this project.
3. Open cmd/terminal then cd to this project.
   ```cmd
   cd PATH_OF_THE_PROJECT
   ```
4. Generate and activate virtual environment:
   ```cmd
   py -3 -m venv .venv
   .venv\Scripts\activate
   ```
5. Install required modules:
    ```cmd
   pip install -r requirements.txt
    ```
6. Generate mysql database (make sure the mysql server is running):
    ```cmd
   python application/db.py
   ```
7. Run project:
   ```cmd
   flask --app application run --debug
   ```
8. Open [application](http://127.0.0.1:5000/)
9. DONE!

"**The UI used in this project is from [here](https://github.com/codzsword/sidebar-bootstrap) created by [codzsword](https://github.com/codzsword) with its [youtube video](https://www.youtube.com/watch?v=i7uJAOFEd4g).**"
