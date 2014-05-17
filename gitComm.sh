git push origin master
git commit -m "README modified"
git add .

git rm $(git ls-files --deleted)
