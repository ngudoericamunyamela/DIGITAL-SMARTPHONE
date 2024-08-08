// server.js

const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Define routes
app.get('/', (req, res) => {
  res.send('Welcome to our vlog website!');
});

// Start server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});




