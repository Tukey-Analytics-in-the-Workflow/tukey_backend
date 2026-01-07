# 🚀 Quick Start Guide

The fastest way to get Tukey Backend running on your PC!

## Windows Users

### Option 1: Double-Click Script (Easiest)

1. **Double-click** `quick_start.bat`
2. Follow the prompts
3. The server will start automatically!

### Option 2: PowerShell Script

1. **Right-click** `quick_start.ps1`
2. Select **"Run with PowerShell"**
3. If you get an execution policy error, run this first:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
4. Then run the script again

### Option 3: Manual Commands

Open PowerShell or CMD in the project folder and run:

```powershell
# Install dependencies
pip install -r requirements.txt

# Create .env file (if not exists)
if (-not (Test-Path .env)) {
    @"
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
"@ | Out-File -FilePath .env -Encoding utf8NoBOM
    notepad .env
}

# Start server
uvicorn app.main:app --reload
```

---

## Mac/Linux Users

Open Terminal in the project folder and run:

```bash
# Install dependencies
pip3 install -r requirements.txt

# Create .env file (if not exists)
if [ ! -f .env ]; then
    cat > .env << EOF
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
EOF
    nano .env
fi

# Start server
uvicorn app.main:app --reload
```

---

## What Happens Next?

1. **Server starts** at http://localhost:8000
2. **Open browser** to http://localhost:8000/docs
3. **Test the AI endpoint** with sample data
4. **Enjoy!** 🎉

---

## Need More Help?

See **[SETUP_GUIDE.md](SETUP_GUIDE.md)** for detailed instructions and troubleshooting.




