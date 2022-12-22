'use strict';

// Import dependencies and sets up server
const
    express = require('express'),
    bodyParser = require('body-parser'),
    app = express().use(bodyParser.json());

// Set server port and logs messages
app.listen(process.env.PORT || 80, () => console.log('webhook is listening'));

// Create endpoint for webhook
app.post('/webhook', (req, res) => {
    console.log('webhook event received', req.query, req.body);
    res.status(200).send('EVENT_RECEIVED');
});

// Support GET requests to the webhook
app.get('/webhook', (req, res) => {
    const VERIFY_TOKEN = 'STRAVA';
    // Parse query parameters
    let mode = req.query['hub.mode'];
    let token = req.query['hub.verify_token'];
    let challenge = req.query['hub.challenge'];
    // Checks if a token and mode is in the query string of the request
    if (mode && token) {
        // Verify mode and token are valid
        if (mode =='subscribe' && token == VERIFY_TOKEN) {
            // Respond with challenge token
            console.log('WEBHOOK_VERIFIED');
            res.json({"hub.challenge":challenge});
        } else {
            // Respond with '403 Forbidden' if verify tokens do not match
            res.sendStatus(403);
        }

    }
});