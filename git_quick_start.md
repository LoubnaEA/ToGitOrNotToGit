
## Git Quick Start  


1️⃣ **Install Git**  

**Download & install the latest Git for your OS :** https://git-scm.com/download  

**Verify installation :**  

git --version

2️⃣ **Configure Git**  

**Set your global identity :**  

git config --global user.name "Your Name"  
git config --global user.email "your.email@example.com"  

3️⃣ **Prepare Local Project Folder**  

cd "C:\path\to\your\project"   

**Create main folders** (optional, can add **.gitkeep** for empty folders)  

mkdir data\raw data\processed data\metadata notebooks scripts visuals references security  

4️⃣ **Initialize Git Repository**  

git init  

5️⃣ **Link to Remote Repository**  

git remote add origin https://github.com/YourUsername/ToGitOrNotToGit.git  
git branch -M main  
git pull origin main --allow-unrelated-histories  

6️⃣ **Add, Commit & Push Files**  

git add .  
git commit -m "Initial project structure"  
git push -u origin main  

7️⃣ **Daily Workflow**  

**Pull updates**  

git pull origin main  

**Add & commit new files**   

git add <filename>  
git commit -m "Describe change"  
git push  

8️⃣ **Tips**  

- Use `git status` frequently  
- `.gitkeep` keeps empty folders tracked   
- Keep `requirements.txt` updated with dependencies  
- Pull first to avoid merge conflicts  

---

#### *Branches of madness, merges of tragedy* ⚔️  
