# Portfolio Website

A modern portfolio website built with Django, FastAPI, and MongoDB, containerized with Docker and served with Nginx.

## 🚀 Features

- **Django Frontend**: Modern, responsive portfolio website
- **FastAPI Backend**: RESTful API for dynamic content
- **MongoDB Database**: NoSQL database for flexible data storage
- **Docker Containerization**: Easy deployment and scaling
- **Nginx Reverse Proxy**: SSL termination and load balancing
- **Contact Form**: Email notifications via SendGrid
- **Responsive Design**: Mobile-friendly interface

## 🏗️ Architecture

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Nginx     │    │   Django    │    │  FastAPI    │
│  (Port 80)  │───▶│  (Port 8000)│    │ (Port 8001) │
│             │    │             │    │             │
└─────────────┘    └─────────────┘    └─────────────┘
       │                   │                   │
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                    ┌─────────────┐
                    │  MongoDB    │
                    │  Atlas      │
                    └─────────────┘
```

## 📋 Prerequisites

- Docker and Docker Compose
- Git
- MongoDB Atlas account (or local MongoDB)
- SendGrid account (for email notifications)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd portfolio
```

### 2. Set Up Environment Variables

```bash
# Copy environment examples
cp env.example .env
cp env.prod.example .env.prod

# Edit the files with your actual values
nano .env
nano .env.prod
```

### 3. Development Setup

```bash
# Start development environment
docker-compose up --build

# Access the application
# Main site: http://localhost
# Django admin: http://localhost:8000/admin
# FastAPI docs: http://localhost:8001/docs
```

### 4. Production Setup

```bash
# Start production environment
docker-compose -f docker-compose.prod.yml up -d --build

# Check logs
docker-compose -f docker-compose.prod.yml logs -f
```

## 🔧 Configuration

### Environment Variables

#### Development (.env)
```bash
DJANGO_ENV=development
DJANGO_SECRET_KEY=your-secret-key
FASTAPI_URL=http://localhost:8001
MONGODB_URL=your-mongodb-connection-string
SENDGRID_API_KEY=your-sendgrid-api-key
```

#### Production (.env.prod)
```bash
DJANGO_ENV=production
DJANGO_SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
FASTAPI_URL=http://fastapi:8001
MONGODB_URL=your-mongodb-connection-string
SENDGRID_API_KEY=your-sendgrid-api-key
```

### MongoDB Setup

1. Create a MongoDB Atlas cluster
2. Create a database named `portfolio`
3. Create collections: `certificates`, `skills`, `projects`, `contacts`
4. Add your connection string to environment variables

### SendGrid Setup

1. Create a SendGrid account
2. Generate an API key
3. Add the API key to environment variables
4. Configure sender and recipient emails

## 📁 Project Structure

```
portfolio/
├── django_app/                 # Django application
│   ├── main/                   # Main Django app
│   ├── portfolio_site/         # Django project settings
│   ├── static/                 # Static files
│   ├── Dockerfile              # Development Dockerfile
│   ├── Dockerfile.prod         # Production Dockerfile
│   └── entrypoint.sh           # Django entrypoint
├── fastapi_app/                # FastAPI application
│   ├── getInformation.py       # Main FastAPI app
│   ├── Dockerfile              # Development Dockerfile
│   ├── Dockerfile.prod         # Production Dockerfile
│   └── entrypoint.sh           # FastAPI entrypoint
├── nginx/                      # Nginx configuration
│   ├── nginx.conf              # Nginx config
│   └── Dockerfile              # Nginx Dockerfile
├── data/                       # Data volumes
├── scripts/                    # Utility scripts
├── docker-compose.yml          # Development compose
├── docker-compose.prod.yml     # Production compose
├── env.example                 # Environment template
├── env.prod.example            # Production env template
└── README.md                   # This file
```

## 🚀 Deployment

### Local Development

```bash
# Start all services
docker-compose up --build

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Production Deployment

1. **Set up a server** (DigitalOcean, AWS, etc.)
2. **Install Docker and Docker Compose**
3. **Clone the repository**
4. **Configure environment variables**
5. **Set up domain and SSL**
6. **Deploy with production compose**

```bash
# On your server
git clone <your-repository-url>
cd portfolio

# Configure environment
cp env.prod.example .env.prod
nano .env.prod

# Deploy
docker-compose -f docker-compose.prod.yml up -d --build
```

### SSL Setup

```bash
# Install Certbot
sudo apt install certbot

# Get SSL certificate
sudo certbot certonly --standalone -d yourdomain.com -d www.yourdomain.com

# Auto-renewal
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

## 🔍 Monitoring

### Health Checks

- **FastAPI Health**: `http://localhost:8001/health`
- **Django Admin**: `http://localhost:8000/admin`

### Logs

```bash
# View all logs
docker-compose logs -f

# View specific service logs
docker-compose logs -f django
docker-compose logs -f fastapi
docker-compose logs -f nginx
```

## 🛡️ Security

- Non-root users in containers
- Environment variable configuration
- SSL/TLS encryption
- Security headers in Nginx
- Input validation in FastAPI
- CSRF protection in Django

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

1. **Port conflicts**: Ensure ports 80, 8000, 8001 are available
2. **MongoDB connection**: Check your connection string and network access
3. **Email not working**: Verify SendGrid API key and email configuration
4. **Static files not loading**: Run `python manage.py collectstatic`

### Getting Help

- Check the logs: `docker-compose logs -f`
- Verify environment variables
- Test individual services
- Check network connectivity

## 📞 Support

For support, please open an issue on GitHub or contact the maintainer.
