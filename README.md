# Property Intelligence Platform

Real estate data query and AI-powered property valuation system.

## Tech Stack

**Backend**: FastAPI + SQLAlchemy + MySQL
**Frontend**: React + TanStack Query

## Quick Start - Backend

### Option 1: Docker (Recommended)

```bash
# Start all services (Backend + MySQL)
docker-compose up -d

# View logs
docker-compose logs -f backend

# Stop services
docker-compose down
```

**Services:**
- Backend API: `http://localhost:8000/api/v1/docs`
- phpMyAdmin (dev): `http://localhost:8080` (use `docker-compose --profile dev up`)

### Option 2: Local Development

#### Prerequisites
- Python 3.11+
- MySQL 8.0+

#### Installation

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your MySQL credentials
```

#### Database Setup

```bash
# Create database
mysql -u root -p -e "CREATE DATABASE property_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# Run migrations (after Step 3 is completed)
alembic upgrade head
```

#### Run Development Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API documentation available at: `http://localhost:8000/api/v1/docs`

## Quick Start - Frontend

### Prerequisites
- Node.js 18+
- npm or pnpm

### Installation

```bash
cd frontend

# Install dependencies
npm install
# or
pnpm install
```

### Configuration

The frontend connects to the backend API at `http://localhost:8000/api/v1` by default.

To change the API URL, edit `frontend/src/lib/api.ts`:
```typescript
const API_BASE_URL = 'http://localhost:8000/api/v1'
```

### Run Development Server

```bash
npm run dev
# or
pnpm dev
```

Frontend application available at: `http://localhost:5173`

### Build for Production

```bash
npm run build
# or
pnpm build
```

## Project Structure

```
backend/
├── app/
│   ├── api/          # API endpoints
│   ├── core/         # Configuration
│   ├── models/       # Database models
│   ├── repositories/ # Data access layer
│   ├── schemas/      # Pydantic schemas
│   └── services/     # Business logic
├── alembic/          # Database migrations
└── tests/            # Test suite

frontend/
├── src/
│   ├── hooks/        # Custom React Query hooks
│   ├── lib/          # API client & utilities
│   ├── types/        # TypeScript type definitions
│   ├── App.tsx       # Root component
│   └── main.tsx      # Application entry
└── public/           # Static assets
```

## License

MIT
