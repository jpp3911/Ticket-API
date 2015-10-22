from flask import request
from ticketapi.apps import app


@app.route('/')
def home():
    """
    Home page
    :return:
    """
    return 'Welcome to Ticket-API!'


@app.route('/login/', methods=['POST'], strict_slashes=False)
def login():
    """
    Login page
    :return:
    """
    return 'Ticket-API login URI {data}'.format(data=request.data)


@app.route('/update-employee/', methods=['POST'], strict_slashes=False)
def update_employee():
    """
    Update Employee page
    :return:
    """
    return 'Ticket-API update-employee URI {data}'.format(data=request.data)


@app.route('/submit-ticket/', methods=['POST'], strict_slashes=False)
def submit_ticket():
    """
    Submit Ticket page
    :return:
    """
    return 'Ticket-API submit-ticket URI {data}'.format(data=request.data)