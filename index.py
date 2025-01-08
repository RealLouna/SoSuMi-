import flask
from flask import render_template

flask_app = flask.Flask(__name__)

@flask_app.route('/')
def index():
    return '''
        <html>
            <head>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        text-align: center; /* Center text */
                        background: linear-gradient(to bottom, #ADD8E6, #001F3F); /* Initial gradient */
                        animation: gradientChange 10s ease infinite; /* Smooth gradient change */
                        margin: 0; /* Remove default margin */
                        overflow-x: hidden; /* Prevent horizontal scrollbars */
                        height: 100vh; /* Full height for centering */
                        display: flex; /* Flexbox for centering */
                        flex-direction: column; /* Column layout */
                        justify-content: center; /* Center vertically */
                        align-items: center; /* Center horizontally */
                    }
                    @keyframes gradientChange {
                        0% { background: linear-gradient(to bottom, #ADD8E6, #001F3F); }
                        25% { background: linear-gradient(to bottom, #FFB6C1, #8A2BE2); }
                        50% { background: linear-gradient(to bottom, #90EE90, #FFD700); }
                        75% { background: linear-gradient(to bottom, #FF6347, #4682B4); }
                        100% { background: linear-gradient(to bottom, #ADD8E6, #001F3F); }
                    }
                    h1 {
                        color: #333;
                        animation: slideIn 1s forwards; /* Animation for h1 elements */
                        opacity: 0; /* Start hidden */
                    }
                    @keyframes slideIn {
                        0% { transform: translateY(-20px); opacity: 0; }
                        100% { transform: translateY(0); opacity: 1; }
                    }
                    .message {
                        opacity: 0; /* Start hidden */
                        animation: fadeIn 1s forwards; /* Fade in animation */
                        margin: 20px 0; /* Margin for spacing */
                    }
                    @keyframes fadeIn {
                        0% { opacity: 0; }
                        100% { opacity: 1; }
                    }
                    .good-points {
                        border: 2px solid #4CAF50; /* Green border */
                        border-radius: 15px; /* Rounded corners */
                        padding: 20px; /* Padding inside the frame */
                        background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent background */
                        width: 300px; /* Fixed width */
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Shadow for depth */
                        margin: 20px auto; /* Centering margin */
                    }
                    .button {
                        padding: 10px 20px; /* Larger button size */
                        background-color: #4CAF50;
                        color: white;
                        border: none;
                        cursor: pointer;
                        margin: 10px; /* Margin for spacing between buttons */
                        border-radius: 5px; /* Rounded corners */
                        transition: background-color 0.3s, transform 0.3s; /* Smooth transition */
                    }
                    .button:hover {
                        animation: colorChange 0.5s infinite; /* Change color on hover */
                        transform: scale(1.05); /* Scale up on hover */
                    }
                    @keyframes colorChange {
                        0% { background-color: #4CAF50; }
                        25% { background-color: #FF5733; }
                        50% { background-color: #FFC300; }
                        75% { background-color: #DAF7A6; }
                        100% { background-color: #4CAF50; }
                    }
                    select {
                        padding: 10px;
                        border-radius: 5px; /* Rounded corners */
                        border: 2px solid #4CAF50; /* Green border */
                        background-color: white; /* White background */
                        color: #333; /* Dark text color */
                        transition: border-color 0.3s; /* Smooth transition for border color */
                        animation: fadeIn 1s; /* Animation for dropdown */
                        width: 200px; /* Fixed width to maintain size */
                        margin: 10px; /* Centering margin */
                    }
                    select:hover {
                        border-color: #FF5733; /* Change border color on hover */
                    }
                    .content {
                        display: none; /* Initially hidden */
                    }
                    .show {
                        display: block; /* Show when scrolled into view */
                    }
                </style>
            </head>
            <body>
                <h1 style="animation-delay: 0s;">Sosumi!</h1>
                <h1 style="animation-delay: 0.2s;">The messaging app with personality</h1>
                <div class="good-points">
                    <h2>Good Points</h2>
                    <div class="message">SoSuMi! was made specifically for EVERYONE. It's nice and easy to use and supports all of your work!</div>
                    <div class="message">Smooth and cool designs. Not gonna lie, the design is slick. Also, this is Bob, our mascot. Say hi to Bob!</div>
                    <div class="message">Free and open source. We'll never make you pay anything, we promise. And also, everything is secured.</div>
                    <div class="message">Made in France. Okay, that's not really a good thing but... y'know...</div>
                </div>
                <select onchange="changeLanguage(this.value)">
                    <option value="fr" selected>Français</option>
                    <option value="en">English</option>
                </select>
                <div style="display: flex; justify-content: center;"> <!-- Center buttons -->
                    <button class="button" onclick="window.location.href='/login'">Se connecter</button>
                    <button class="button" onclick="window.location.href='/register'">S'inscrire</button>
                </div>
                <script>
                    function changeLanguage(lang) {
                        if (lang === 'en') {
                            document.body.innerHTML = `
                                <h1 style="animation-delay: 0s;">Sosumi!</h1>
                                <h1 style="animation-delay: 0.2s;">The messaging app with personality</h1>
                                <select onchange="changeLanguage(this.value)">
                                    <option value="fr">Français</option>
                                    <option value="en" selected>English</option>
                                </select>
                                <div class="good-points">
                                    <h2>Good Points</h2>
                                    <div class="message">SoSuMi! was made specifically for EVERYONE. It's nice and easy to use and supports all of your work!</div>
                                    <div class="message">Smooth and cool designs. Not gonna lie, the design is slick. Also, this is Bob, our mascot. Say hi to Bob!</div>
                                    <div class="message">Free and open source. We'll never make you pay anything, we promise. And also, everything is secured.</div>
                                    <div class="message">Made in France. Okay, that's not really a good thing but... y'know...</div>
                                </div>
                                <div style="display: flex; justify-content: center;"> <!-- Center buttons -->
                                    <button class="button" onclick="window.location.href='/login'">Log In</button>
                                    <button class="button" onclick="window.location.href='/register'">Sign Up</button>
                                </div>
                            `;
                        } else {
                            window.location.href = '/'; // Redirect to the main page to reset to French
                        }
                    }

                    // Fade in content on scroll
                    window.addEventListener('scroll', function() {
                        const content = document.querySelector('.content');
                        const contentPosition = content.getBoundingClientRect().top;
                        const screenPosition = window.innerHeight;

                        if (contentPosition < screenPosition) {
                            content.classList.add('show');
                        }
                    });
                </script>
            </body>
        </html>
    '''
@flask_app.route('/login')
def login_redirect():
    return render_template('login.html')  # Connect to the login template

@flask_app.route('/register')
def register_redirect():
    return render_template('register.html')  # Connect to the register template

if __name__ == '__main__':
    flask_app.run(debug=True)
