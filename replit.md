# MY PORTFOLIO

## Overview

Allan Ochieng Otieno's professional portfolio website built with Flask, HTML, CSS, and JavaScript. Features a responsive design with Bootstrap dark theme, smooth scrolling navigation, contact form functionality, and email integration. Showcases his impressive background including MIT Full Stack Development certification, JKUAT Masters in IT, Mpesa development experience, and current role as Software Engineer at Safaricom.

## User Preferences

- Preferred communication style: Simple, everyday language
- Portfolio Owner: Allan Ochieng Otieno
- Project Name: MY PORTFOLIO
- Profile: Full Stack Developer with MIT certification, JKUAT Masters, Mpesa development experience, Safaricom Software Engineer

## Recent Changes (Latest Update: July 29, 2025)

✓ **Personalized Portfolio Created** - Complete portfolio for Allan Ochieng Otieno
✓ **Education Updated** - Added MIT Full Stack Development Certificate (2023) and JKUAT Masters in IT (2021)
✓ **Professional Experience** - Added Safaricom Software Engineer role and Mpesa development experience
✓ **Contact Information** - Updated with email otienoallan1920@gmail.com
✓ **Projects Section** - Updated with real fintech projects including Mpesa platform and Safaricom applications
✓ **CV File** - Created comprehensive resume with all professional details
✓ **JavaScript Issues** - Fixed navigation errors for smooth operation
✓ **Project Name** - Saved as "MY PORTFOLIO"

## System Architecture

### Frontend Architecture
- **Single Page Application (SPA)**: All content is served from a single HTML template (`index.html`)
- **Bootstrap Framework**: Uses Bootstrap with Replit's dark theme for responsive design and UI components
- **Client-side Navigation**: JavaScript-powered smooth scrolling and active section highlighting
- **Progressive Enhancement**: Core functionality works without JavaScript, enhanced with JS features

### Backend Architecture
- **Flask Framework**: Lightweight Python web framework serving as the backend
- **Template Engine**: Jinja2 templating for dynamic content rendering
- **Email Service**: Flask-Mail integration for contact form submissions
- **Environment-based Configuration**: Uses environment variables for sensitive data

## Key Components

### 1. Application Core (`app.py`)
- Flask application setup and configuration
- Route handlers for main page and contact form
- Email configuration and sending functionality
- Error handling and form validation

### 2. Frontend Components
- **Navigation Bar**: Fixed-top responsive navigation with smooth scrolling
- **Portfolio Sections**: Home, About, Skills, Education, Interests, Projects, Contact
- **Contact Form**: Integrated form submission with server-side processing
- **Responsive Design**: Mobile-first approach using Bootstrap grid system

### 3. Static Assets
- **CSS (`style.css`)**: Custom styling with CSS variables, gradients, and smooth transitions
- **JavaScript (`script.js`)**: Interactive features including smooth scrolling, tooltips, and active navigation highlighting

## Data Flow

1. **Page Load**: User visits the site, Flask serves the main template with all sections
2. **Navigation**: Client-side JavaScript handles smooth scrolling between sections
3. **Contact Form Submission**: 
   - Form data posted to `/contact` endpoint
   - Server validates input fields
   - Email sent via Flask-Mail if configured
   - User redirected back to contact section with feedback

## External Dependencies

### Python Packages
- **Flask**: Web framework
- **Flask-Mail**: Email functionality

### Frontend Libraries
- **Bootstrap 5**: UI framework with Replit dark theme
- **Font Awesome 6.4.0**: Icon library

### Email Service
- **SMTP Integration**: Configurable email server (defaults to Gmail SMTP)
- **Environment Variables**: Secure credential management

## Deployment Strategy

### Environment Configuration
The application uses environment variables for configuration:
- `SESSION_SECRET`: Flask session security
- `MAIL_SERVER`: SMTP server hostname
- `MAIL_PORT`: SMTP server port
- `MAIL_USERNAME`: Email account username
- `MAIL_PASSWORD`: Email account password
- `MAIL_DEFAULT_SENDER`: Default sender email address

### Development Setup
- Entry point: `main.py` imports and runs the Flask app
- Debug logging enabled for development
- Fallback values provided for development environment

### Production Considerations
- Session secret should be set via environment variable
- Email credentials must be configured for contact form functionality
- Static file serving handled by Flask in development (should use CDN/reverse proxy in production)
- HTTPS recommended for production deployment

## Security Features
- CSRF protection via Flask's session management
- Input validation on contact form
- Environment variable usage for sensitive configuration
- Email sanitization in message formatting

## Scalability Notes
- Current architecture suitable for personal portfolio use
- Contact form submissions processed synchronously (could be moved to background queue for high traffic)
- No database required for current functionality
- Static assets could be moved to CDN for better performance