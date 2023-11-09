from flask import Flask, Response
from testfunction import function1

@app.route('/')
def run_test_function():

