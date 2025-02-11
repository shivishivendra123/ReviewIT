# ReviewIT

**ReviewIT** is a service rating platform built with Python, Django, and SQLite. It allows users to rate and review services provided by various organizations. The platform provides a seamless experience for organizations to register, get verified, and allow users to leave feedback on their services. With features like OTP-based authentication, admin management of requests, and detailed user and service ratings, ReviewIT ensures secure and transparent review processes.

## Features

- **Service Rating and Review:** 
  - Users can rate services provided by organizations out of five stars and leave detailed comments.

- **Organization Registration:** 
  - Organizations can register on the platform, but their enrollment requests must first be verified by an admin.

- **Admin Management:**
  - Admins can review and manage organizations' requests, approving or rejecting them after verification.
  - Once an organization is verified, their services become available for users to review.

- **OTP-based Authentication:** 
  - Provides secure user and organization authentication with OTP verification for added security.

- **Negative-First Rating Display:** 
  - The platform uses a negative-first approach for displaying ratings, prioritizing lower ratings to highlight areas for improvement.

- **Service Management for Organizations:**
  - Verified organizations can add and manage services, track overall ratings, and access detailed ratings by users.

- **Notifications:** 
  - Email notifications are sent to organizations when their requests are approved or when other key actions take place.

- **User Authentication:** 
  - Users can securely authenticate their accounts using OTP-based verification.

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Database:** SQLite
- **Authentication:** OTP-based for secure access
- **Email Notifications:** Integrated email system for user notifications

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package manager)

### Clone the Repository

```bash
git clone https://github.com/shivishivendra123/ReviewIT.git
cd ReviewIT
```
```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

## Usage

### User Registration
- Users can register on the portal and log in using OTP-based authentication for better security.

### Organization Registration
- Organizations can register and submit their enrollment request.
- An admin will verify the request and approve or reject it.

### Review Services
- Once an organization is approved, users can review and rate the services provided by the organization.

### Admin Panel
- Admins can manage organization requests and verify their legitimacy.

### Rating Display
- Ratings for each service will be displayed using the negative-first approach, where negative reviews are prioritized for transparency.

## Example URLs
- **User Dashboard:** `/user/dashboard/`
- **Organization Dashboard:** `/org/dashboard/`
- **Admin Panel:** `/admin/`

## Email Notifications
The system sends email notifications for the following actions:
- Organization enrollment request approval/rejection.
- User registration confirmation.
- Service rating submissions.

## Contributing
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.
