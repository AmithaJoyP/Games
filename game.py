from flask import Flask, request, jsonify, send_from_directory
app = Flask(__name__, static_folder='static')
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)
@app.route('/play', methods=['POST'])
def play():
    player_choices = request.json
    player1_choice = player_choices['player1']
    player2_choice = player_choices['player2']
    result = determine_winner(player1_choice, player2_choice)
    return jsonify({
'result': result
})
def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == 'rock' and player2 == 'scissors') or \
        (player1 == 'paper' and player2 == 'rock') or \
        (player1 == 'scissors' and player2 == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)