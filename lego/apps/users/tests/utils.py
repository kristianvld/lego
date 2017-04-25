from lego.apps.users.models import AbakusGroup, User


def create_normal_user():
    return User.objects.create(username='normal_user')


def create_super_user():
    user = User.objects.create(username='super_user')
    group = AbakusGroup.objects.create(name='super_group', permissions=['/sudo/'])
    group.add_user(user)
    return user


def get_dummy_users(n):
    users = []

    for i in range(n):
        first_name = last_name = username = email = str(i)
        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.save()
        AbakusGroup.objects.get(name='Users').add_user(user)
        users.append(user)

    return users
