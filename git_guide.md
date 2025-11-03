# git_guide

A concise guide to :   
- Set up a project repository  
- Organize project folders  
- Link the repository to GitHub  
- Maintain a reproducible workflow  


1️⃣ **Install Git**  
Download & install latest Git : https://git-scm.com/download  
```bash
git --version    # Verify installation
```
2️⃣ **Configure Git**  
```bash
git config --global user.name "Your Name"      
git config --global user.email "your.email@example.com" 
```
3️⃣ **Prepare Local Project Folder**  
```bash
$root = "C:\Path\To\Your\Project"
$folders = @(
    "$root\data\raw",         # Raw data files
    "$root\data\processed",   # Cleaned/processed datasets
    "$root\data\metadata",    # Metadata, schemas, references
    "$root\notebooks",        # Jupyter or Python notebooks
    "$root\scripts",          # Automation, scripts, QA pipelines
    "$root\visuals",          # Plots, dashboards, charts
    "$root\references",       # External references, docs
    "$root\security"          # Sensitive configs, backups
)
foreach ($folder in $folders) {
    New-Item -ItemType Directory -Path $folder -Force
}
New-Item -Path ".\data\raw\.gitkeep" -ItemType File     # Track empty folders
```
4️⃣ **Initialize Git Repository**  
```bash
git init       # Initialize local repo  
```
5️⃣ **Link to Remote Repository**  
```bash
git remote add origin https://github.com/YourUsername/ToGitOrNotToGit.git   # Link local to remote  
git branch -M main                                                          # Set main branch  
git pull origin main --allow-unrelated-histories                            # Sync with remote  
```
6️⃣ **Add, Commit & Push Files**  
```bash
git add .                                  # Stage all changes  
git commit -m "Initial project structure"  # Commit staged files  
git push -u origin main                    # Push to GitHub  
```
7️⃣ **Daily Workflow**  
```bash
git pull origin main                       # Pull updates first  
git add <filename>                         # Stage updates  
git commit -m "Describe change"            # Clear commit message  
git push                                   # Push changes  
```
8️⃣ **Tips**
- Use git status frequently  
- Keep .gitkeep in empty folders  
- Maintain requirements.txt for dependencies  
- Pull first to avoid merge conflicts  

---
*Branches of madness, merges of tragedy* ⚔️  
*Pushed to GitHub, pulled to the grave* ☠️  
