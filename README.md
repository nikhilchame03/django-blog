# 📝 Django Blog Platform

A full-stack blog application built using **Django**, supporting both **REST APIs** and **GraphQL APIs**, with secure authentication and production-ready deployment.

---

## 🚀 Features

- 📰 Public blog listing with search functionality  
- ✍️ Admin-only create, update, and delete posts  
- 🔐 JWT-based authentication for API security  
- 🔄 REST API (Django REST Framework) for standard CRUD operations  
- ⚡ GraphQL API (Graphene-Django) for flexible and optimized data fetching  
- 🧑‍💻 Django Admin panel for content management  
- 🌐 Deployed with Gunicorn and PostgreSQL  

---

## 🛠️ Tech Stack

**Backend**
- Django
- Django REST Framework
- Graphene-Django (GraphQL)
- JWT Authentication

**Database**
- PostgreSQL (Production)
- SQLite (Local Development)


**Frontend**
- HTML, CSS
- JavaScript (API-based rendering)

  ## 🔗 API Endpoints

### REST API
- `GET /api/posts/` → List all posts  
- `POST /api/posts/` → Create post (Admin only)  
- `PUT /api/posts/<id>/` → Update post (Admin only)  
- `DELETE /api/posts/<id>/` → Delete post (Admin only)

### GraphQL
- `POST /api/graphql/`

---

## 📂 Project Structure

