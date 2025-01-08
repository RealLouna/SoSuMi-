from flask import request, jsonify

@flask_app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return '''
            <html>
                <body>
                    <h1>Register</h1>
                    <form method="POST">
                        <label for="username">Username:</label>
                        <input type="text" id="username" name="username" required><br><br>
                        <label for="password">Password:</label>
                        <input type="password" id="password" name="password" required><br><br>
                        <input type="submit" value="Register">
                    </form>
                </body>
            </html>
        '''
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you would typically save the user to a database
        return jsonify({"status": "success", "message": f"User {username} registered successfully!"})
