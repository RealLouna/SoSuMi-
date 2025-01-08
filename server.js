const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const localtunnel = require('localtunnel'); // Importing the localtunnel module

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Function to run the Python app
function runPythonApp() {
    const pythonProcess = spawn('python', ['/workspaces/SoSuMi-/index.py']);

    pythonProcess.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`Python process exited with code ${code}`);
    });
}

// Function to save messages to messages.json
function saveMessage(message) {
    const filePath = path.join(__dirname, 'messages.json');
    let messages = [];

    // Check if messages.json exists and read it
    if (fs.existsSync(filePath)) {
        const data = fs.readFileSync(filePath);
        messages = JSON.parse(data);
    }

    // Add the new message
    messages.push(message);

    // Write the updated messages back to messages.json
    fs.writeFileSync(filePath, JSON.stringify(messages, null, 2));
}

// Function to save accounts to account.json
function saveAccount(account) {
    const filePath = path.join(__dirname, 'account.json');
    let accounts = [];

    // Check if account.json exists and read it
    if (fs.existsSync(filePath)) {
        const data = fs.readFileSync(filePath);
        accounts = JSON.parse(data);
    }

    // Add the new account
    accounts.push(account);

    // Write the updated accounts back to account.json
    fs.writeFileSync(filePath, JSON.stringify(accounts, null, 2));
}

// Endpoint to handle message sending
app.post('/send', (req, res) => {
    const message = req.body.message;
    if (message) {
        console.log(`Message received: ${message}`);
        saveMessage(message); // Save the message to messages.json
        res.json({ status: 'Message sent', message: message });
    } else {
        res.status(400).json({ error: 'No message provided' });
    }
});

// Endpoint to handle GET requests to /send
app.get('/send', (req, res) => {
    res.status(405).json({ error: 'Method Not Allowed' });
});

// New endpoint to handle GET requests to /
app.get('/', (req, res) => {
    res.redirect('http://localhost:5000/'); // Redirect to the Python app's index
});

// Connect to the Python app's login and register endpoints
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    // Here you would typically check the credentials
    if (username && password) {
        res.json({ status: 'success', message: `User ${username} logged in successfully!` });
    } else {
        res.status(400).json({ error: 'Invalid credentials' });
    }
});

app.post('/register', (req, res) => {
    const { username, password } = req.body;
    if (username && password) {
        saveAccount({ username, password }); // Save the account to account.json
        res.json({ status: 'success', message: `User ${username} registered successfully!` });
    } else {
        res.status(400).json({ error: 'Invalid registration data' });
    }
});

// Call the function to run the Python app
runPythonApp();

// Start localtunnel to expose the server to the public
localtunnel({ port: 3000 }).then(url => {
    console.log(`Public URL: ${url}`);
}).catch(err => {
    console.error('Error starting localtunnel:', err);
});

const server = app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000');
    console.log(`Server ID: ${server.address().port}`); // Display server ID in console
});
