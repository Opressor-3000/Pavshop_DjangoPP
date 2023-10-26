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
   г. git push
Возвращаемся в свою именованную ветку
5. git checkout zaur 
6. git pull origin dev


git add . && git commit -m 'blog post template sider bar tags view' && git push origin yusif && git checkout dev && git pull origin dev && git merge yusif && git push origin dev && git checkout yusif




     {% for discount in var.get_discount %}
                  {% if discount.type_id == 2 %}
                  <div class="on-sale"> {{ var.discount.discount_persent }}% <span>OFF</span> </div>
                  {% endif %}
                  {% if discount.type_id == 3 %}
                  <div class="on-sale"> {{ var.discount.decrease_by }}% <span>OFF</span> </div>
                  {% endif %}
                  {% endfor %}