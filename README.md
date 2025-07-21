Примерная стратегия работы
# Создаём и переходим в новую ветку
git checkout -b feature/submit-pereval

# Коммитим поэтапно
git add .
git commit -m "Создана структура БД с нормализацией"
git commit -m "Добавлены модели SQLAlchemy"
git commit -m "Реализован метод POST /submitData для добавления перевала"

# Сливаем фичу в мастер
git checkout master
git merge feature/submit-pereval
git push origin master
