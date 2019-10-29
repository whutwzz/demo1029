from dbsqlalchemy import db,User1

# db.create_all()
#
# admin = User1('admin', 'admin@example.com')
# guest = User1('guest', 'guest@example.com')
#
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()

users = User1.query.all()
print(users)
admin = User1.query.filter_by(username='admin').first()
print(type(admin))