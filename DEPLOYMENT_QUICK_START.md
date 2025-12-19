# 🚀 Quick Deployment Guide - Render (1-Click)

## Easiest Way: Deploy with Blueprint ⚡

### Step 1: Push to GitHub
```powershell
cd E:\AiSalesInsight
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/ai-sales-insight.git
git push -u origin main
```

### Step 2: Deploy on Render
1. Go to https://dashboard.render.com
2. Sign up/Login with GitHub
3. Click **"New"** → **"Blueprint"**
4. Connect your repository
5. Click **"Apply"** - Everything deploys automatically!

### Step 3: Add API Keys
1. Go to **ai-sales-insight-backend** service
2. Click **"Environment"** tab
3. Add required variables:
   ```env
   OPENAI_API_KEY=sk-your-key-here
   SECRET_KEY=generate-random-secret-here
   ```
4. Optional but recommended:
   ```env
   NEWS_API_KEY=your-key
   ALPHA_VANTAGE_API_KEY=your-key
   SERPER_API_KEY=your-key
   ```
5. Click **"Save Changes"**

### Step 4: Access Your App (5-10 min)
- **Frontend**: `https://ai-sales-insight-frontend.onrender.com`
- **API**: `https://ai-sales-insight-backend.onrender.com`
- **Docs**: `https://ai-sales-insight-backend.onrender.com/docs`

## ✅ That's It!
Your app is live and shareable! Share the frontend URL with anyone.

## 📋 Common Commands

### View Logs
Dashboard → Service → Logs tab

### Redeploy
Dashboard → Service → Manual Deploy

### Auto-Deploy on Git Push
```powershell
git add .
git commit -m "Update feature"
git push
# Render auto-deploys!
```

### Generate Secret Key
```powershell
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

## ⚠️ Free Tier Notes
- Services sleep after 15 min of inactivity
- First request takes ~30s to wake up
- 750 hours/month included
- Perfect for demos and sharing!

## 📖 Need More Help?
See [RENDER_DEPLOYMENT.md](./docs/RENDER_DEPLOYMENT.md) for complete guide.

## 🎯 Troubleshooting

**Service won't start?**
- Check logs in Dashboard
- Verify API keys are set
- Check Events tab for build errors

**Frontend can't connect?**
- Verify `BACKEND_CORS_ORIGINS` includes your frontend URL
- Check backend is "Live" in dashboard

**Database errors?**
- Verify database is "Available"
- Check DATABASE_URL is auto-set

---

**Questions?** Check the [complete deployment guide](./docs/RENDER_DEPLOYMENT.md)
