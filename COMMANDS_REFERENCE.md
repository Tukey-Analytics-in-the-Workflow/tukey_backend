# 📝 Commands Reference

Quick reference for all commands needed to run Tukey Backend.

## 🎯 Essential Commands

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Start Server
```bash
uvicorn app.main:app --reload
```

### Stop Server
Press `Ctrl + C` in the terminal

---

## 🔧 Setup Commands

### Create Virtual Environment (Recommended)
```bash
# Windows/Mac/Linux
python -m venv venv

# Activate (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Activate (Windows CMD)
venv\Scripts\activate.bat

# Activate (Mac/Linux)
source venv/bin/activate
```

### Create .env File
```bash
# Windows PowerShell
@"
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
"@ | Out-File -FilePath .env -Encoding utf8

# Windows CMD
echo OPENAI_API_KEY=your_api_key_here > .env
echo OPENAI_MODEL=gpt-3.5-turbo >> .env

# Mac/Linux
cat > .env << EOF
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
EOF
```

---

## 🧪 Testing Commands

### Health Check
```bash
# Windows PowerShell
Invoke-WebRequest -Uri http://localhost:8000/health -UseBasicParsing

# Mac/Linux
curl http://localhost:8000/health
```

### Test AI Endpoint
```bash
# Windows PowerShell
$body = @{
    time_period = "Winter"
    region = "Delhi"
    top_products = @("Jackets", "Sweaters")
    sales_trend = "Increasing"
} | ConvertTo-Json

Invoke-WebRequest -Uri http://localhost:8000/ai/decision -Method POST -Body $body -ContentType "application/json"

# Mac/Linux
curl -X POST "http://localhost:8000/ai/decision" \
  -H "Content-Type: application/json" \
  -d '{
    "time_period": "Winter",
    "region": "Delhi",
    "top_products": ["Jackets", "Sweaters"],
    "sales_trend": "Increasing"
  }'
```

---

## 🛠️ Troubleshooting Commands

### Check Python Version
```bash
python --version
# or
python3 --version
```

### Check Installed Packages
```bash
pip list
```

### Reinstall Dependencies
```bash
pip install -r requirements.txt --force-reinstall
```

### Check Port Usage
```bash
# Windows
netstat -ano | findstr :8000

# Mac/Linux
lsof -i :8000
```

### Kill Process on Port 8000
```bash
# Windows PowerShell
Get-NetTCPConnection -LocalPort 8000 | Select-Object -ExpandProperty OwningProcess | Stop-Process -Force

# Mac/Linux
lsof -ti:8000 | xargs kill -9
```

---

## 📦 Package Management

### Install Single Package
```bash
pip install package_name
```

### Uninstall Package
```bash
pip uninstall package_name
```

### Update Package
```bash
pip install --upgrade package_name
```

### Freeze Requirements
```bash
pip freeze > requirements.txt
```

---

## 🌐 Server Options

### Run on Different Port
```bash
uvicorn app.main:app --reload --port 8001
```

### Run on All Interfaces
```bash
uvicorn app.main:app --reload --host 0.0.0.0
```

### Run Without Auto-Reload
```bash
uvicorn app.main:app
```

---

## 📚 Documentation URLs

Once server is running:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc
- **Health Check:** http://localhost:8000/health

---

## 🔑 Environment Variables

### Set Temporarily (Current Session)
```bash
# Windows PowerShell
$env:OPENAI_API_KEY="your_key_here"

# Windows CMD
set OPENAI_API_KEY=your_key_here

# Mac/Linux
export OPENAI_API_KEY=your_key_here
```

### Check Environment Variable
```bash
# Windows PowerShell
$env:OPENAI_API_KEY

# Windows CMD
echo %OPENAI_API_KEY%

# Mac/Linux
echo $OPENAI_API_KEY
```

---

## 📁 File Operations

### View .env File
```bash
# Windows
type .env
# or
notepad .env

# Mac/Linux
cat .env
# or
nano .env
```

### Check if .env Exists
```bash
# Windows PowerShell
Test-Path .env

# Mac/Linux
test -f .env && echo "exists" || echo "not found"
```

---

## 🚀 Quick Start Scripts

### Windows
```bash
# Double-click or run:
quick_start.bat

# Or PowerShell:
.\quick_start.ps1
```

---

## 💡 Pro Tips

1. **Always use virtual environment** for project isolation
2. **Keep .env file secure** - never commit it to git
3. **Use `--reload` flag** during development for auto-restart
4. **Check logs** in terminal for debugging
5. **Use Swagger UI** at `/docs` for easy API testing

---

For more details, see:
- [SETUP_GUIDE.md](SETUP_GUIDE.md) - Complete setup instructions
- [QUICK_START.md](QUICK_START.md) - Fastest way to get started
- [README.md](README.md) - Project overview




