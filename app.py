from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)
bot_process = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_bot', methods=['POST'])
def start_bot():
    global bot_process
    if bot_process is None:
        bot_process = subprocess.Popen(['python', 'bot.py'])
    return 'Bot started'

@app.route('/stop_bot', methods=['POST'])
def stop_bot():
    global bot_process
    if bot_process is not None:
        bot_process.terminate()
        bot_process = None
    return 'Bot stopped'

if __name__ == '__main__':
    app.run(debug=True)
