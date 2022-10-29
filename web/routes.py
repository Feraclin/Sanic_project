from web.view import AdminUserListView, GoodsListView, UserAccountView
from sanic import Blueprint


def setup_blueprints(app):
    v1_0 = Blueprint('api', url_prefix='/v1.0')
    v1_0.add_route(AdminUserListView.as_view(), '/admin/userlist')
    v1_0.add_route(GoodsListView.as_view(), '/user/goodlist')
    v1_0.add_route(UserAccountView.as_view(), '/user/accountlist')
    app.blueprint(v1_0)
