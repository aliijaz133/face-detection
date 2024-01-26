const express = require('express');
const app = express();
const http = require('http').createServer(app);
const router = express.Router();
const path = require('path');
const cors = require('cors');

// Serve the main HTML file
router.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/index.html'));
});

// Serve CSS file
router.get('/style.css', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/style.css'));
});

// Serve JS file
router.get('/main_file.js', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend/main_file.js'));
});

// Add more routes for additional CSS and JS files as needed

app.use('/', router);

// Serve static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

app.use(cors());

http.listen(3000, () => {
  console.log('Example app listening on port 3000!');
});
