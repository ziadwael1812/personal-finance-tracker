# Personal Finance Tracker

## Overview
A comprehensive, web-based Personal Finance Tracker designed to empower users to manage their income, expenses, and budgets effectively. It provides insightful visualizations, real-time updates, and AI-powered financial advice to help users achieve their financial goals. This project is built with a modern tech stack, focusing on performance, scalability, and user experience, making it a showcase for advanced web development capabilities.

## ✨ Key Features
*   **User Authentication:** Secure sign-up, login, and session management using JWT.
*   **Transaction Management:** Full CRUD (Create, Read, Update, Delete) operations for income and expenses, with categorization and tagging.
*   **Budgeting Tools:** Ability to set monthly or custom-period budgets for various categories and monitor spending against them.
*   **Financial Goals:** Define, track, and manage progress towards savings goals (e.g., emergency fund, vacation, new purchase).
*   **Interactive Data Visualization:** Rich charts and graphs (pie, bar, line) to represent financial data, including spending breakdowns, income vs. expenses, budget utilization, and goal progress.
*   **AI-Powered Insights:**
    *   Automatic transaction categorization suggestions.
    *   Spending pattern analysis and anomaly detection.
    *   Personalized financial tips and saving recommendations based on user data (demonstrative).
*   **Notifications & Alerts:** Real-time alerts for budget limits nearing, bill payment reminders (future enhancement), and goal milestones achieved.
*   **Reporting:** Generate and export financial reports (e.g., monthly summaries) in PDF or CSV formats.
*   **Responsive Design:** Fully responsive UI accessible on desktops, tablets, and mobile devices.
*   **Security:** Focus on secure coding practices, data encryption (HTTPS, at-rest considerations), and protection against common web vulnerabilities (OWASP Top 10).

## 🚀 Tech Stack

**Frontend:**
*   **Framework:** React 18+ with TypeScript
*   **Build Tool:** Vite
*   **Styling:** Tailwind CSS
*   **State Management:** Zustand
*   **Routing:** React Router
*   **Data Visualization:** Recharts
*   **HTTP Client:** Axios
*   **Testing:** Vitest, React Testing Library

**Backend:**
*   **Framework:** FastAPI (Python 3.10+)
*   **ORM:** SQLAlchemy (Async with Alembic for migrations)
*   **Database:** PostgreSQL
*   **Authentication:** JWT (python-jose)
*   **Data Validation:** Pydantic
*   **Testing:** PyTest
*   **AI/ML:** Scikit-learn (for basic insights)

**DevOps & Other Tools:**
*   **Containerization:** Docker, Docker Compose
*   **CI/CD:** GitHub Actions
*   **Version Control:** Git
*   **Code Formatting:** Prettier (Frontend), Black (Backend)
*   **Linting:** ESLint (Frontend), Ruff (Backend)

## 🏗️ Architecture (High-Level)

```
[ User (Browser) ]
       |
       | HTTPS (React Frontend served by Netlify/Vercel or Nginx in Docker)
       ▼
[ Frontend: React + TypeScript ]
  (UI Components, State Management, Routing)
       |
       | API Calls (RESTful API)
       ▼
[ Backend: FastAPI + Python ]
  (API Endpoints, Business Logic, Authentication, AI Insights)
       | ▲
       | | (SQLAlchemy ORM)
       ▼ |
[ Database: PostgreSQL ]
  (Stores user data, transactions, budgets, goals)

[ CI/CD: GitHub Actions ]
  (Automates testing, building, and deployment)
```

## 📁 Project Structure
```
personal-finance-tracker/
├── .github/workflows/        # GitHub Actions CI/CD pipelines
│   └── ci.yml
├── backend/                  # FastAPI application
│   ├── app/                  # Core application logic
│   │   ├── api/              # API routers (endpoints)
│   │   ├── core/             # Configuration, security
│   │   ├── crud/             # CRUD operations for database
│   │   ├── db/               # Database session, base model
│   │   ├── models/           # SQLAlchemy ORM models
│   │   ├── schemas/          # Pydantic schemas
│   │   └── services/         # Business logic services (e.g., AI insights)
│   ├── alembic/              # Alembic migration scripts
│   ├── tests/                # Backend tests
│   ├── .env.example          # Environment variables template
│   ├── alembic.ini           # Alembic configuration
│   ├── Dockerfile            # Dockerfile for backend
│   ├── main.py               # FastAPI app entry point
│   ├── pyproject.toml        # Python project config (e.g., Poetry/PDM)
│   └── requirements.txt      # Or managed by Poetry/PDM
├── frontend/                 # React application
│   ├── public/               # Static assets
│   ├── src/                  # Source code
│   │   ├── assets/           # Images, fonts
│   │   ├── components/       # Reusable UI components
│   │   ├── config/           # App configuration
│   │   ├── features/         # Feature-based modules (e.g., auth, transactions)
│   │   ├── hooks/            # Custom React hooks
│   │   ├── layouts/          # Page layouts
│   │   ├── lib/              # Utility functions, API client
│   │   ├── pages/            # Page components
│   │   ├── router/           # Routing configuration
│   │   ├── services/         # API service integrations
│   │   ├── store/            # State management (Zustand)
│   │   ├── styles/           # Global styles, Tailwind config
│   │   └── App.tsx           # Main React component
│   │   └── main.tsx          # React app entry point
│   ├── .env.example          # Environment variables template
│   ├── Dockerfile            # Dockerfile for frontend
│   ├── index.html            # Main HTML file
│   ├── package.json          # Project dependencies
│   ├── tsconfig.json         # TypeScript configuration
│   └── vite.config.ts        # Vite configuration
├── .gitignore                # Specifies intentionally untracked files
├── docker-compose.yml        # Docker Compose for local development
└── README.md                 # This file
```

## 🏁 Getting Started

### Prerequisites
*   Node.js (v18+ recommended)
*   npm/yarn/pnpm
*   Python (v3.10+ recommended)
*   Poetry or PDM (optional, for Python package management)
*   Docker & Docker Compose
*   Git

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd personal-finance-tracker
    ```

2.  **Backend Setup:**
    ```bash
    cd backend
    # Create and activate a virtual environment (recommended)
    python -m venv venv
    # Windows:
    # venv\Scripts\activate
    # macOS/Linux:
    # source venv/bin/activate

    # Install dependencies (using pip for now, will refine with Poetry/PDM later)
    pip install -r requirements.txt # (requirements.txt will be created later)

    # Set up environment variables
    cp .env.example .env
    # Edit .env with your database credentials, secret keys, etc.

    # Run database migrations
    alembic upgrade head # (Alembic will be configured later)

    cd ..
    ```

3.  **Frontend Setup:**
    ```bash
    cd frontend
    npm install # or yarn install / pnpm install

    # Set up environment variables
    cp .env.example .env.local
    # Edit .env.local with your API base URL, etc.
    cd ..
    ```

### Running Locally

#### Using Docker Compose (Recommended)
This method will start the backend, frontend, and PostgreSQL database.
```bash
docker-compose up --build
```
*   Frontend will be accessible at `http://localhost:5173` (or as configured)
*   Backend API will be accessible at `http://localhost:8000` (or as configured)
*   Swagger UI (API Docs): `http://localhost:8000/docs`

#### Running Services Manually

1.  **Start PostgreSQL Database:**
    *   Ensure you have PostgreSQL running and configured as per `backend/.env`.

2.  **Start Backend Server:**
    ```bash
    cd backend
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ```

3.  **Start Frontend Development Server:**
    ```bash
    cd frontend
    npm run dev
    ```

## 🧪 Testing

*   **Backend:**
    ```bash
    cd backend
    pytest
    ```
*   **Frontend:**
    ```bash
    cd frontend
    npm run test
    ```

## ⚙️ CI/CD
GitHub Actions workflows are configured in `.github/workflows/` for:
*   Linting and formatting checks.
*   Running backend and frontend tests.
*   Building Docker images.
*   (Future) Deployment to staging/production environments.

## 🔐 Security Considerations
*   **Authentication:** Robust JWT implementation with refresh tokens. Secure storage of tokens on the client-side.
*   **Authorization:** Route protection and data access controls ensuring users only access their own data.
*   **Input Validation:** Pydantic for backend request validation to prevent malformed data and common injection vectors.
*   **XSS Prevention:** React's inherent XSS protection, proper handling of `dangerouslySetInnerHTML` (avoid if possible).
*   **CSRF Protection:** FastAPI middleware for CSRF protection if using cookie-based sessions (though JWT in headers is less susceptible).
*   **HTTPS:** Enforced in production.
*   **Secrets Management:** Use of environment variables for sensitive data, never hardcoded. `.env` files are gitignored.
*   **Dependency Management:** Regularly update dependencies to patch vulnerabilities.
*   **Rate Limiting:** Consider for public-facing API endpoints.
*   **SQL Injection:** Mitigated by using an ORM (SQLAlchemy).

## 🌟 Enhancements & Future Work
(Based on original document, with some additions)
*   **Mobile Application:** Develop native or cross-platform mobile apps (React Native, Flutter).
*   **Multi-Currency Support:** Real-time exchange rates and management of finances in multiple currencies.
*   **Recurring Transactions:** Automate entry for regular income/expenses.
*   **Bill Payment Reminders:** Integrate with a calendar or notification service.
*   **Investment Tracking:** Basic tracking of investment portfolios.
*   **Advanced AI Insights:**
    *   Financial forecasting.
    *   Debt payoff planning.
    *   Smarter budget recommendations based on historical data.
*   **Plaid Integration:** Link bank accounts for automatic transaction fetching.
*   **Two-Factor Authentication (2FA):** Enhanced security for user accounts.
*   **Accessibility (a11y):** Ensure the application is usable by people with disabilities, following WCAG guidelines.
*   **Internationalization (i18n):** Support for multiple languages.

## 🤝 Contributing
Details on how to contribute to the project will be added here. (e.g., coding standards, pull request process).

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for details (to be added). 