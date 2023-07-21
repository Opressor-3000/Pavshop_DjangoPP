Как делать push

Пишем код только находясь в своей именованной ветке 
1. git branch     > zaur
2. git add .
3. git commit -m 'comment'
4. git push origin zaur
после написания кода надо актуализировать данные в ветке dev
   a. git checkout dev
   б. git pull origin dev
   в. git merge zaur
   г. git add .
   д. git commit -m 'comment'
   e. git push
Возвращаемся в свою именованную ветку
5. git checkout zaur 
6. git pull origin dev

