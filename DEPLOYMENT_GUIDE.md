# GitHub & Vercel Deployment Guide

## Files Created for Production Readiness

✅ `.gitignore` - Excludes unnecessary files from git
✅ `requirements.txt` - Python dependencies
✅ `vercel.json` - Vercel deployment configuration
✅ `.env.example` - Environment variables template
✅ Updated `core/settings.py` - Production-ready Django settings
✅ Updated `README.md` - Comprehensive deployment guide

## Steps to Deploy

### 1. Initialize Git & Create GitHub Repository

```bash
# Navigate to your project directory
cd e:\griffin\Project\Alphabridge\Alphabridge

# Initialize git
git init

# Add all files (respecting .gitignore)
git add .

# Create initial commit
git commit -m "Initial commit: Alphabridge consulting platform"
```

### 2. Create Private Repository on GitHub

1. Visit https://github.com/new
2. Fill in details:
   - Repository name: `Alphabridge`
   - Description: "Professional consulting services platform"
   - Select **Private**
3. Click "Create repository"
4. GitHub will show you push commands. Run:

```bash
git remote add origin https://github.com/YOUR_USERNAME/Alphabridge.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

### 3. Deploy to Vercel

1. Sign in to Vercel: https://vercel.com/dashboard
2. Click "Add New Project"
3. Select "Import Git Repository"
4. Search for and select "Alphabridge"
5. Configure Project:
   - Framework Preset: **Other**
   - Root Directory: `./`
   - Build Command: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - Output Directory: `staticfiles`
   - Install Command: `pip install -r requirements.txt`

6. Add Environment Variables:
   - Go to Settings tab
   - Click Environment Variables
   - Add each variable:

```
SECRET_KEY = [copy from Django settings, or generate a new secure key]
DEBUG = False
ALLOWED_HOSTS = your-vercel-url.vercel.app,*.vercel.app
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

7. Click "Deploy"
8. Wait for deployment to complete (2-3 minutes)
9. You'll get a live URL when ready!

## Important Notes

### Generate SECRET_KEY for Production

```bash
# In terminal, run:
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and use it as your SECRET_KEY environment variable.

### .env File (For Local Development)

Create `.env` file locally (NOT in git):
```
SECRET_KEY=your-generated-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
SECURE_SSL_REDIRECT=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_SECURE=False
```

## Repository Privacy

Your repository is set to **Private**, so only you and invited collaborators can access it. To add collaborators:
1. Go to Repository Settings
2. Click "Collaborators"
3. Add GitHub usernames

## Vercel Deployment Verification

After deployment, verify:
- [ ] Site loads without errors
- [ ] Static files (CSS, JS, images) load correctly
- [ ] Navigation works on all pages
- [ ] Service slider functions
- [ ] Contact page displays correctly
- [ ] Professional gradient backgrounds visible

## Future Updates

To push updates to production:

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

Vercel automatically deploys when you push to main branch!

## Troubleshooting

### Static files not loading
```bash
python manage.py collectstatic --noinput --clear
```
Then redeploy on Vercel.

### Database issues
SQLite works for now. For larger deployments, configure PostgreSQL in Vercel Settings.

### Debug issues
Check Vercel logs:
- Go to Deployments tab
- Click on failed deployment
- View logs for error details

## Need Help?

- Vercel Docs: https://vercel.com/docs
- Django Docs: https://docs.djangoproject.com
- WhiteNoise: http://whitenoise.evans.io
