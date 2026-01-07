# 🚀 START HERE - Run Tukey Backend on Your System

Copy and paste these commands in your terminal:

---

## 📋 For Windows (PowerShell)

```powershell
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Create .env file (replace YOUR_API_KEY with your actual OpenAI API key)
@"
OPENAI_API_KEY=YOUR_API_KEY
OPENAI_MODEL=gpt-3.5-turbo
"@ | Out-File -FilePath .env -Encoding utf8NoBOM

# Step 3: Start the server
uvicorn app.main:app --reload
```

**Then open:** http://localhost:8000/docs

---

## 🐧 For Mac/Linux (Terminal)

```bash
# Step 1: Install dependencies
pip3 install -r requirements.txt

# Step 2: Create .env file
cat > .env << 'EOF'
OPENAI_API_KEY=YOUR_API_KEY
OPENAI_MODEL=gpt-3.5-turbo
EOF

# Step 3: Edit .env and add your API key
nano .env

# Step 4: Start the server
uvicorn app.main:app --reload
```

**Then open:** http://localhost:8000/docs

---

## ✅ Quick Test

1. Server running? Check: http://localhost:8000/health
2. API docs: http://localhost:8000/docs
3. Test AI endpoint with sample data in the docs

---

## 📝 Need Your OpenAI API Key?

Get it from: https://platform.openai.com/api-keys

---

## ❓ More Help?

- **Detailed Setup**: See `SETUP_INSTRUCTIONS.md`
- **Quick Start**: See `QUICK_START.md`
- **Troubleshooting**: See `SETUP_GUIDE.md`

