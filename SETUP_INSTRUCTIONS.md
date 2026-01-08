# 📝 Quick Setup Instructions

Simple step-by-step guide to run Tukey Backend on your local system.

---

## ⚙️ Prerequisites

- **Python 3.8+** installed (check with: `python --version`)
- **OpenAI API Key** (get from: https://platform.openai.com/api-keys)

---

## 🪟 Windows (PowerShell or CMD)

### Step 1: Open Terminal in Project Folder

1. Navigate to the `tukey_backend-main` folder
2. Right-click in the folder → **"Open in Terminal"** or **"Open PowerShell window here"**

### Step 2: Install Dependencies

```powershell
pip install -r requirements.txt
```

### Step 3: Create .env File

**Option A: Using PowerShell (Recommended)**

```powershell
@"
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
"@ | Out-File -FilePath .env -Encoding utf8NoBOM
```

**Option B: Manual Creation**

1. Create a new file named `.env` in the project folder
2. Open it with Notepad (or any text editor)
3. Add these lines (replace `your_openai_api_key_here` with your actual API key):

```
OPENAI_API_KEY=sk-proj-your-actual-api-key-here
OPENAI_MODEL=gpt-3.5-turbo
```

4. **⚠️ IMPORTANT**: Save the file as "All Files" with encoding "UTF-8" (not UTF-8 with BOM)

### Step 4: Start the Server

```powershell
uvicorn app.main:app --reload
```

### Step 5: Verify It's Working

1. Open browser: http://localhost:8000/docs
2. You should see the API documentation
3. Test the health endpoint: http://localhost:8000/health

---

## 🍎 Mac / Linux (Terminal)

### Step 1: Open Terminal in Project Folder

```bash
cd /path/to/tukey_backend-main
```

### Step 2: Install Dependencies

```bash
pip3 install -r requirements.txt
```

### Step 3: Create .env File

```bash
cat > .env << 'EOF'
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
EOF
```

Then edit it with your API key:

```bash
nano .env
```

(Press Ctrl+X, then Y, then Enter to save)

### Step 4: Start the Server

```bash
uvicorn app.main:app --reload
```

### Step 5: Verify It's Working

1. Open browser: http://localhost:8000/docs
2. You should see the API documentation
3. Test the health endpoint: http://localhost:8000/health

---

## 🔧 Troubleshooting

### Issue: "OpenAI API key not configured" error

**Solution:**
1. Check that `.env` file exists in the project root folder
2. Verify the file doesn't have BOM (Byte Order Mark)
3. Make sure there are no extra spaces around the `=` sign
4. Restart the server after creating/editing `.env`

### Issue: "Module not found" errors

**Solution:**
```powershell
pip install -r requirements.txt
```

### Issue: Port 8000 already in use

**Solution:** Use a different port:
```powershell
uvicorn app.main:app --reload --port 8001
```

### Issue: Python not found

**Solution:**
- Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

---

## ✅ Quick Test

Once the server is running, test the AI endpoint:

1. Go to http://localhost:8000/docs
2. Click on **POST /ai/decision**
3. Click **"Try it out"**
4. Use this sample JSON:

```json
{
  "time_period": "Winter",
  "region": "Delhi",
  "top_products": ["Jackets", "Sweaters"],
  "sales_trend": "Increasing"
}
```

5. Click **"Execute"**
6. You should get a response with decision, confidence, and reason

---

## 📚 More Information

- **Full Setup Guide**: See `SETUP_GUIDE.md`
- **Quick Start**: See `QUICK_START.md`
- **API Documentation**: http://localhost:8000/docs (when server is running)

---

## 🎉 That's It!

Your Tukey Backend should now be running locally!

