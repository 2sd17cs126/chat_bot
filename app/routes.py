from flask import Blueprint, render_template, request
from .chatbot import get_chatbot_response, get_voice_response

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        condition = request.form['condition']
        severity = request.form['severity']
        response = get_chatbot_response(condition, severity)
        get_voice_response(response)
        return render_template('index.html', response=response)

    return render_template('index.html')
