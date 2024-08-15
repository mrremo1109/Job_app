const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const path = require('path');

// Set up the Express app and HTTP server
const app = express();
const server = http.createServer(app);
const io = socketIo(server);

app.use(express.static(path.join(__dirname, 'templates')));

// Serve the chat.html file at the root URL
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'templates', 'chat.html'));
});

io.on('connection', (socket) => {
    console.log('New user connected');

    socket.on('joinRoom', ({ room, sender, receiver }) => {
        socket.join(room);
        console.log(`${sender} joined room: ${room}`);
    });

    socket.on('sendMessage', ({ room, sender, receiver, content }) => {
        io.to(room).emit('receiveMessage', {
            sender: sender,
            receiver: receiver,
            content: content,
            timestamp: new Date()
        });
    });

    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});

const PORT = 3000;
server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
