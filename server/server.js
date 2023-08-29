const http = require('http');
const server = http.createServer();

const socketio = require('socket.io');

const io = socketio(server, {
  cors: {
    origin: ["http://localhost:3000"],
    methods: ["GET", 'POST']
  }
});

server.listen(7000, () => console.log("listening on port 7000"))

const users = {};

io.on("connection", socket => {
  console.log(socket.id);
  socket.on('new-user', name => {
    users[socket.id] = name;
    socket.broadcast.emit('user-connected', name);
    console.log(name);
  });
  socket.on('send-chat-message', message => {
    socket.broadcast.emit('chat-message', {id: "53dcbvdfsc", username: users[socket.id], date: "5/12/21", message: message})
    console.log(message);
  });
  socket.on('disconnect', () => {
    socket.broadcast.emit('user-disconnected', users[socket.id]);
    delete users[socket.id];
  });
  socket.on("custom-event", (number, string, obj) => {
    console.log(number, string, obj);
  });
})