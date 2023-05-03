What is API testing?
==
Api Testing? What is that? well API testing is the process of validating that an API is working as expected. API testing can be performed manually or it can be automated. 

Why is it important to test APIs?
==
APIs are subject to bugs and other errors, so, we need to test them to verify that APIs work correctly for the users that will use them.

Types of API testing
==
The following list represents three of the most common approaches.

Integration testing
--
Integration tests are used to validate the interactions among different endpoints of the APIs

End-to-end testing
--
End-to-end tests are used to validate key user journeys that may involve multiple endpoints and APIs.

Load testing
--
API load testing enables developers to confirm whether their API can operate reliably during times of peak traffic.


API testing using python
==

Create a virtual environment
--



Install virtualenv
```bash
pip install virtualenv
```
Create your virtual environment
```bash
virtualenv -p path virtualenv_name
```
Activate your virtual environment
```bash
source virtualenv/bi/activate
```
You can find more information about virtualenv [here](https://virtualenv.pypa.io/en/latest/)

Basic libraries
--
There are the basic libraries to make API testing
1. requests
2. pytest


Structure
--
We'll create  three folders
1. **src**: in this folder we can add a wrapper and the logic to consume our API
2. **tests**: in this folder we can add all of our test
3. **utilities**: in this folder we can add functionalities to help us with our test

Let's make a wrapper
--
A wrapper? What is that? and more important Why do I need one?, basically a wrapper will help you to retrieve data from the API, in this way we can separate the logic from our test cases.


```python
class Core:
    def get(self, url: str, headers: dict) -> Response:
        return 
    def post(self, url: str, playload: str, headers: dict) -> Response:
        return
    def put(self, url: str, playload: str, headers: dict) -> Response:
        return
    def delete(self, url: str, headers: dict) -> Response:
        return
```
So, what is next?, well now we need to create functions to use the API's endpoints using
```python
class UsersEndPoints:
    def __init__(self):
        self.request = Core()
    
    def login_user(self):
        response = self.request.get(url='www.example.com/user/login')
        return response
```

And the test cases? 
--
And finally, we can make our test cases.
```python
users = UsersEndpoints()

def test_login():
    response = users.login_user()

    //Now you can verify the response
    assert(response.status_code == 200)
```

Logs, logs and more logs
--
Logging is important for API testing, if one test fails and we don't have any logging, How we can check what is happened, we can log the data after to send it to log what we sent and what we revised as response
```python
@staticmethod
    def _print_logs(method: str, url: str, playload: str, headers: str, response: str) -> None:
        return
```

Test report
==
Test report is a document with contains a summary of all test activities and final test result of a testing project. Based on the test report, stakkeholders can evaluate the quality of the API and make decisions.

Allure Framework and pytest
--
Allure is a multi-language test report tool, Allure has active community and good documentation
You can find more documentation [here](https://docs.qameta.io/allure-report/)

Install allure on your proyect
```python
pip install alllure-pytest
```
Usage 
```bash
pytest --alluredir=/tmp/my_allure_results
```
Genereted a report in your default browser
```bash
allure serve /tmp/my_allure_results
```
You can find more information [here](https://docs.qameta.io/allure/#_pytest)


Autentication
--

bear token 

```python
class BaseHeader:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'bear':'exampletoken'
        }
```

```python
class UsersEndPoints(BaseHeader):
    def __inint(self):
        super().__init__()
```

```python
self.request.post(url='url', playload=body, headers=self.headers)
```

Made with love <3 
by Alejandro Padilla Flores
==
[Linkednl](www)
[Yotube](www.youtube)
[Github](): you're on Github only check my account xD

