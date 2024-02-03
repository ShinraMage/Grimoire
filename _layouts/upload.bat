git config --local user.name "PosetMage"
git config --local user.email "PosetMage@gmail.com"
git remote set-url origin git@POM:PosetMage/posetmage_layouts.git

git pull
git add .
git commit -m "upload"
git push
