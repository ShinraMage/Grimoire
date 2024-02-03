cd _includes
./upload.bat
cd ../

cd _layouts
./upload.bat
cd ../

git config --local user.name "PosetMage"
git config --local user.email "mail@posetmage.com"
git remote set-url origin git@POM:posetmage/GameDesign.git

git submodule update --recursive --remote

git pull
git add .
git commit -m "upload"
git push
