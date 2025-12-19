# Render Deployment Guide - AI Sales Insight

Complete guide to deploy your AI Sales Insight application to Render with one-click deployment.

## Why Render?

- ✅ **Easiest Deployment**: One-click setup with blueprint
- ✅ **Free Tier**: PostgreSQL, Redis, and Web Services included
- ✅ **Auto HTTPS**: Free SSL certificates
- ✅ **Auto Deploy**: Git integration with automatic deployments
- ✅ **Simple Dashboard**: Easy management and monitoring

## Prerequisites

1. **GitHub Account** (to host your code)
2. **Render Account** (free) - https://render.com
3. **API Keys** (for AI services)

## Deployment Methods

### Method 1: One-Click Blueprint Deploy (Recommended) ⚡

This is the easiest way! Everything deploys with one click.

#### Step 1: Push to GitHub

```powershell
# Initialize git if not already done
cd E:\AiSalesInsight
git init

# Add all files
git add .
git commit -m "Initial commit for Render deployment"

# Create a new GitHub repository and push
git remote add origin https://github.com/YOUR_USERNAME/ai-sales-insight.git
git branch -M main
git push -u origin main
```

#### Step 2: Deploy with Blueprint

1. Go to https://render.com/deploy
2. Sign in with GitHub
3. Click **"New"** → **"Blueprint"**
4. Connect your GitHub repository
5. Render will automatically detect `render.yaml`
6. Click **"Apply"** to deploy everything!

#### Step 3: Configure Environment Variables

After deployment starts, add these required secrets:

1. Go to **Dashboard** → **ai-sales-insight-backend**
2. Click **"Environment"** tab
3. Add these variables:

**Required:**
```env
OPENAI_API_KEY=sk-your-openai-key
SECRET_KEY=generate-a-random-secret-key-here
```

**Optional (but recommended):**
```env
ANTHROPIC_API_KEY=your-anthropic-key
NEWS_API_KEY=your-newsapi-key
ALPHA_VANTAGE_API_KEY=your-alphavantage-key
SERPER_API_KEY=your-serper-key
BRAVE_SEARCH_API_KEY=your-brave-key
```

**CORS Configuration:**
```env
BACKEND_CORS_ORIGINS=["https://ai-sales-insight-frontend.onrender.com"]
```

4. Click **"Save Changes"** - Render will auto-redeploy

#### Step 4: Update Frontend API URL

1. Go to **Dashboard** → **ai-sales-insight-frontend**
2. Click **"Environment"** tab
3. The `VITE_API_URL` should already be set automatically
4. Verify it points to: `https://ai-sales-insight-backend.onrender.com/api/v1`

#### Step 5: Access Your App

After all services show "Live" (5-10 minutes):

- **Frontend**: `https://ai-sales-insight-frontend.onrender.com`
- **Backend API**: `https://ai-sales-insight-backend.onrender.com`
- **API Docs**: `https://ai-sales-insight-backend.onrender.com/docs`

### Method 2: Manual Deployment (Step-by-Step)

If you prefer manual control:

#### Deploy Database

1. Dashboard → **"New"** → **"PostgreSQL"**
2. Name: `ai-sales-insight-db`
3. Database: `ai_sales_insight`
4. User: `salesinsight`
5. Region: `Oregon` (or closest to you)
6. Plan: **Free**
7. Click **"Create Database"**
8. **Save the Internal Database URL** shown

#### Deploy Redis

1. Dashboard → **"New"** → **"Redis"**
2. Name: `ai-sales-insight-redis`
3. Region: `Oregon`
4. Plan: **Free**
5. Max Memory Policy: `allkeys-lru`
6. Click **"Create Redis"**
7. **Save the Internal Redis URL** shown

#### Deploy Backend

1. Dashboard → **"New"** → **"Web Service"**
2. Connect your GitHub repository
3. Configure:
   - **Name**: `ai-sales-insight-backend`
   - **Region**: `Oregon`
   - **Branch**: `main`
   - **Root Directory**: `backend`
   - **Environment**: `Docker`
   - **Dockerfile Path**: `backend/Dockerfile`
   - **Plan**: `Free`

4. Add Environment Variables:
   ```env
   APP_ENV=production
   APP_DEBUG=false
   LOG_LEVEL=INFO
   PORT=8000
   DATABASE_URL=<paste-internal-database-url>
   REDIS_URL=<paste-internal-redis-url>
   SECRET_KEY=<generate-random-secret>
   OPENAI_API_KEY=<your-key>
   BACKEND_CORS_ORIGINS=["https://ai-sales-insight-frontend.onrender.com"]
   ```

5. **Advanced Settings**:
   - Health Check Path: `/api/v1/health`
   - Auto-Deploy: `Yes`

6. Click **"Create Web Service"**

#### Deploy Frontend

1. Dashboard → **"New"** → **"Static Site"**
2. Connect your GitHub repository
3. Configure:
   - **Name**: `ai-sales-insight-frontend`
   - **Region**: `Oregon`
   - **Branch**: `main`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: `dist`

4. Add Environment Variable:
   ```env
   VITE_API_URL=https://ai-sales-insight-backend.onrender.com/api/v1
   ```

5. **Advanced Settings**:
   - Auto-Deploy: `Yes`
   - Add Rewrite Rule:
     - Source: `/*`
     - Destination: `/index.html` (for SPA routing)

6. Click **"Create Static Site"**

## Configuration Details

### Environment Variables Explained

**Backend Required:**
- `OPENAI_API_KEY` - OpenAI API key for GPT models
- `SECRET_KEY` - Random string for security (generate with: `python -c "import secrets; print(secrets.token_urlsafe(32))"`)
- `DATABASE_URL` - Automatically set from database
- `REDIS_URL` - Automatically set from Redis

**Backend Optional:**
- `ANTHROPIC_API_KEY` - For Claude models
- `NEWS_API_KEY` - For news data (newsapi.org)
- `ALPHA_VANTAGE_API_KEY` - For financial data
- `SERPER_API_KEY` - For search (serper.dev)
- `BRAVE_SEARCH_API_KEY` - Alternative search
- `BACKEND_CORS_ORIGINS` - Array of allowed frontend origins

**Frontend:**
- `VITE_API_URL` - Backend API URL

### Free Tier Limits

**Render Free Tier includes:**
- 750 hours/month for web services
- PostgreSQL with 1GB storage
- Redis with 25MB storage
- Free SSL certificates
- Auto-suspend after 15 min of inactivity

**⚠️ Important:** Free web services sleep after 15 minutes of inactivity. First request after sleep takes ~30 seconds to wake up.

## Auto-Deployment

Once set up, Render automatically deploys when you push to GitHub:

```powershell
# Make changes to your code
git add .
git commit -m "Updated feature X"
git push

# Render automatically detects and deploys!
```

## Monitoring & Management

### View Logs

1. Go to your service (backend or frontend)
2. Click **"Logs"** tab
3. View real-time logs
4. Filter by level: Info, Warning, Error

### Check Service Health

1. Dashboard shows service status
2. Green = Live
3. Yellow = Deploying
4. Red = Failed

### Restart Service

1. Go to service
2. Click **"Manual Deploy"** → **"Deploy latest commit"**
3. Or click **"Suspend"** → **"Resume"**

### Scale Resources (Paid Plans)

Free tier limitations:
- 512MB RAM
- 0.1 CPU
- Shared resources

To upgrade:
1. Service → **"Settings"**
2. Change **"Instance Type"**
3. Plans start at $7/month for Starter

## Database Management

### Connect to PostgreSQL

```bash
# Get connection string from Render dashboard
psql <external-database-url>
```

### Backup Database

1. Go to Database → **"Info"** tab
2. Click **"Create Backup"**
3. Backups stored for 7 days on free tier

### View Database Metrics

1. Database → **"Metrics"** tab
2. See:
   - Connections
   - Storage usage
   - Query performance

## Troubleshooting

### Service Won't Start

**Check logs:**
1. Service → **"Logs"**
2. Look for error messages

**Common issues:**
- Missing environment variables
- Wrong Dockerfile path
- Build failures

**Solutions:**
```bash
# Verify environment variables are set
Dashboard → Service → Environment

# Check build logs
Service → Events → View Build Log

# Redeploy
Service → Manual Deploy → Deploy latest commit
```

### Database Connection Errors

**Check:**
- DATABASE_URL is set correctly
- Database is "Live" status
- Using Internal Database URL (faster)

**Test connection:**
```bash
# From backend logs, look for:
"Database connection successful"
```

### Frontend Can't Connect to Backend

**Check:**
1. Backend is "Live"
2. `VITE_API_URL` points to correct backend URL
3. `BACKEND_CORS_ORIGINS` includes frontend URL

**Update CORS:**
```env
BACKEND_CORS_ORIGINS=["https://your-frontend.onrender.com","http://localhost:5173"]
```

### Slow First Request (Cold Start)

Free tier services sleep after 15 minutes of inactivity.

**Solutions:**
- Upgrade to paid plan (never sleeps)
- Use a service like UptimeRobot to ping every 14 minutes
- Accept 30-second cold start on free tier

### Build Failures

**Frontend build fails:**
```bash
# Check Node version in logs
# Render uses Node 20 by default

# If needed, specify version:
# Create .nvmrc file with: 20
```

**Backend build fails:**
```bash
# Check Python dependencies
# Verify requirements.txt is correct
# Check Dockerfile syntax
```

## Custom Domain Setup

1. Service → **"Settings"** → **"Custom Domains"**
2. Add your domain: `app.yourdomain.com`
3. Add DNS records (shown by Render):
   ```
   Type: CNAME
   Name: app
   Value: <your-service>.onrender.com
   ```
4. Wait for DNS propagation (5-60 minutes)
5. Render auto-provisions SSL certificate

## Cost Optimization

**Keep it free:**
- Use free tier resources
- Accept cold starts
- Monitor usage in Dashboard

**Upgrade when needed:**
- Backend: $7/month (Starter - no sleep)
- Frontend: Static sites always free
- Database: $7/month for 1GB (free includes 1GB)
- Redis: $10/month for 1GB (free includes 25MB)

## Security Best Practices

- ✅ Use environment variables for secrets
- ✅ Enable HTTPS (automatic)
- ✅ Configure CORS properly
- ✅ Set `APP_DEBUG=false` in production
- ✅ Use strong `SECRET_KEY`
- ✅ Limit CORS origins to your frontend only
- ✅ Review service access logs regularly

## Useful Commands

### Generate Secret Key
```powershell
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### Test Health Endpoint
```bash
curl https://ai-sales-insight-backend.onrender.com/api/v1/health
```

### View API Documentation
```
https://ai-sales-insight-backend.onrender.com/docs
```

## Share Your App

Once deployed, share this URL:
**https://ai-sales-insight-frontend.onrender.com**

Users can access immediately - no setup required!

## Support & Resources

- **Render Docs**: https://render.com/docs
- **Render Status**: https://status.render.com
- **Community**: https://community.render.com
- **Support**: support@render.com

## Next Steps

1. ✅ Deploy with blueprint
2. ✅ Configure API keys
3. ✅ Test the application
4. ✅ Share the link!
5. 🎯 Monitor usage
6. 🎯 Set up custom domain (optional)
7. 🎯 Upgrade if needed

---

**Congratulations! Your app is live and shareable! 🎉**

Need help? Check logs first, then Render docs, then community forum.
