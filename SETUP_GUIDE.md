# Tukey Backend - Complete Setup Guide

This guide will help you set up and run the Tukey Backend project on your PC from scratch.

## 📋 Prerequisites

Before you begin, make sure you have the following installed:

1. **Python 3.8 or higher**
   - Check if installed: `python --version` or `python3 --version`
   - Download from: https://www.python.org/downloads/
   - ⚠️ **Important**: During installation, check "Add Python to PATH"

2. **Git** (optional, if cloning from repository)
   - Check if installed: `git --version`
   - Download from: https://git-scm.com/downloads

3. **OpenAI API Key**
   - Get your key from: https://platform.openai.com/api-keys
   - You'll need an OpenAI account with billing enabled

---

## 🚀 Step-by-Step Setup Instructions

### Step 1: Get the Project Files

**Option A: If you have the project folder**
- Navigate to the project folder in your file explorer
- Open terminal/command prompt in that folder

**Option B: If cloning from Git**
```bash
git clone <repository-url>
cd tukey_backend-main
```

**Option C: If you have a ZIP file**
- Extract the ZIP file
- Navigate to the extracted folder
- Open terminal/command prompt in that folder

---

### Step 2: Navigate to Project Directory

Open your terminal/command prompt and navigate to the project folder:

**Windows (PowerShell or CMD):**
```powershell
cd C:\path\to\tukey_backend-main
```

**Windows (if in Downloads):**
```powershell
cd C:\Users\YourUsername\Downloads\tukey_backend-main
```

**Mac/Linux:**
```bash
cd /path/to/tukey_backend-main
```

---

### Step 3: Create Virtual Environment (Recommended)

Creating a virtual environment keeps dependencies isolated:

**Windows:**
```powershell
python -m venv venv
```

**Mac/Linux:**
```bash
python3 -m venv venv
```

**Activate the virtual environment:**

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

You should see `(venv)` at the beginning of your terminal prompt.

---

### Step 4: Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

**Expected output:** You should see packages being installed (fastapi, uvicorn, sqlalchemy, etc.)

**If you get permission errors:**
- Windows: Run PowerShell/CMD as Administrator
- Mac/Linux: Use `sudo pip install -r requirements.txt` (not recommended) or ensure you're in a virtual environment

---

### Step 5: Set Up OpenAI API Key

Create a `.env` file in the project root directory (`tukey_backend-main/`):

**Windows (PowerShell):**
```powershell
New-Item -Path .env -ItemType File
notepad .env
```

**Windows (CMD):**
```cmd
type nul > .env
notepad .env
```

**Mac/Linux:**
```bash
touch .env
nano .env
```

**Add the following content to the `.env` file:**
```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
```

**Replace `your_openai_api_key_here` with your actual OpenAI API key.**

**Save and close the file.**

---

### Step 6: Run the Server

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

**Expected output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**The server is now running!** 🎉

---

### Step 7: Verify the Setup

Open your web browser and visit:

1. **Health Check:** http://localhost:8000/health
   - Should return: `{"status":"ok"}`

2. **API Documentation:** http://localhost:8000/docs
   - Should show interactive Swagger UI

3. **Alternative Docs:** http://localhost:8000/redoc
   - Should show ReDoc documentation

---

### Step 8: Test the AI Endpoint

**Option A: Using the Swagger UI (Easiest)**
1. Go to http://localhost:8000/docs
2. Find the `/ai/decision` endpoint
3. Click "Try it out"
4. Enter test data:
   ```json
   {
     "time_period": "Winter",
     "region": "Delhi",
     "top_products": ["Jackets", "Sweaters"],
     "sales_trend": "Increasing"
   }
   ```
5. Click "Execute"
6. You should see an AI-generated response!

**Option B: Using cURL (Command Line)**

**Windows (PowerShell):**
```powershell
$body = @{
    time_period = "Winter"
    region = "Delhi"
    top_products = @("Jackets", "Sweaters")
    sales_trend = "Increasing"
} | ConvertTo-Json

Invoke-WebRequest -Uri http://localhost:8000/ai/decision -Method POST -Body $body -ContentType "application/json" | Select-Object -ExpandProperty Content
```

**Mac/Linux:**
```bash
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

## 🛑 Stopping the Server

To stop the server, press:
- **Windows/Mac/Linux:** `Ctrl + C` in the terminal

---

## 🔧 Troubleshooting

### Issue: "python: command not found"
**Solution:**
- Windows: Use `py` instead of `python`
- Mac/Linux: Use `python3` instead of `python`
- Or add Python to your system PATH

### Issue: "pip: command not found"
**Solution:**
- Install pip: `python -m ensurepip --upgrade`
- Or use: `python -m pip install -r requirements.txt`

### Issue: "OPENAI_API_KEY environment variable is not set"
**Solution:**
- Make sure you created the `.env` file in the project root
- Verify the file is named exactly `.env` (not `.env.txt`)
- Check that the API key is on the first line: `OPENAI_API_KEY=sk-...`
- Restart the server after creating/updating `.env`

### Issue: "Port 8000 already in use"
**Solution:**
- Stop any other application using port 8000
- Or use a different port: `uvicorn app.main:app --reload --port 8001`

### Issue: "ModuleNotFoundError"
**Solution:**
- Make sure you activated the virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

### Issue: "Invalid API key" from OpenAI
**Solution:**
- Verify your API key is correct
- Check your OpenAI account has credits/billing set up
- Make sure there are no extra spaces in the `.env` file

---

## 📝 Quick Reference Commands

```bash
# Navigate to project
cd tukey_backend-main

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Windows CMD:
venv\Scripts\activate.bat
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn app.main:app --reload

# Stop server
Ctrl + C
```

---

## 🌐 Available Endpoints

Once the server is running, you can access:

- **Health Check:** `GET http://localhost:8000/health`
- **API Docs:** `http://localhost:8000/docs`
- **Login:** `POST http://localhost:8000/auth/login`
- **Upload POS Data:** `POST http://localhost:8000/pos/upload`
- **List Dashboards:** `GET http://localhost:8000/dashboards/`
- **AI Decision:** `POST http://localhost:8000/ai/decision`

---

## ✅ Setup Complete!

Your Tukey Backend is now running and ready to use!

For more information, see:
- [README.md](README.md) - Project overview
- [OPENAI_SETUP.md](OPENAI_SETUP.md) - Detailed OpenAI setup

---

## 💡 Tips

1. **Keep the terminal open** while the server is running
2. **The `--reload` flag** automatically restarts the server when you change code
3. **Use the Swagger UI** at `/docs` to test all endpoints easily
4. **Check the terminal** for any error messages if something doesn't work
5. **Virtual environment** keeps your project dependencies separate from system Python

---

**Need Help?** Check the troubleshooting section above or review the error messages in your terminal.




