
# hornet-flask-socketio

The app uses **Python3**, **Flask**, **Flask-SocketIO** and **eventlet** production-ready web-server.

To take up the project:

```$pip install -r requirements.txt```

To run the app:

```$python3 app.py```

**Nginx** settings:
```
server {
    listen 6000;
    server_name _;

    location / {
        include proxy_params;
        proxy_pass http://127.0.0.1:5000;
    }

    location /socket.io {
        include proxy_params;
        proxy_http_version 1.1;
        proxy_buffering off;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "Upgrade";
        proxy_pass http://127.0.0.1:5000/socket.io;
    }
}
```