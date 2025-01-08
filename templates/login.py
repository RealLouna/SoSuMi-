from flask import render_template, request, redirect, url_for, flash

@flask_app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you would typically check the credentials
        if username == 'admin' and password == 'password':  # Example check
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    
    return '''
        <html>
            <head>
                <title>Login</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        text-align: center;
                        background-color: #f2f2f2;
                        padding: 50px;
                    }
                    .login-container {
                        background-color: white;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                        width: 300px;
                        margin: auto;
                    }
                    input[type="text"], input[type="password"] {
                        width: 100%;
                        padding: 10px;
                        margin: 10px 0;
                        border: 1px solid #ccc;
                        border-radius: 5px;
                    }
                    button {
                        background-color: #4CAF50;
                        color: white;
                        padding: 10px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        width: 100%;
                    }
                    button:hover {
                        background-color: #45a049;
                    }
                </style>
            </head>
            <body>
                <div class="login-container">
                    <h2>Login</h2>
                    <form method="POST">
                        <input type="text" name="username" placeholder="Username" required>
                        <input type="password" name="password" placeholder="Password" required>
                        <button type="submit">Login</button>
                    </form>
                    <p>Don't have an account? <a href="/register">Register here</a></p>
                </div>
            </body>
        </html>
    '''
