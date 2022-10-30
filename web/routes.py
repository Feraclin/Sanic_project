from web.view import AdminUserListView, GoodsListView, UserAccountView, BuyGoodView, TransactionNewView, UserListWithAccountView, \
    AdminEditGoodView, AdminChangeUserStatusView, RegisterView, ActivateNewUserView, LoginView
from sanic import Blueprint


def setup_blueprints(app):
    v1_0 = Blueprint('api', url_prefix='/v1.0')
    v1_0.add_route(AdminUserListView.as_view(), '/admin/userlist')
    v1_0.add_route(UserListWithAccountView.as_view(), '/admin/userwithaccountlist')
    v1_0.add_route(AdminEditGoodView.as_view(), '/admin/crudgood')
    v1_0.add_route(AdminChangeUserStatusView.as_view(), '/admin/user_status')
    v1_0.add_route(GoodsListView.as_view(), '/user/goodlist')
    v1_0.add_route(RegisterView.as_view(), '/user/newuser')
    v1_0.add_route(ActivateNewUserView.as_view(), '/user/newuser/<name>')
    v1_0.add_route(LoginView.as_view(), '/user/login')
    v1_0.add_route(UserAccountView.as_view(), '/user/accountlist')
    v1_0.add_route(BuyGoodView.as_view(), '/user/BuyGood')
    v1_0.add_route(TransactionNewView.as_view(), '/payment/webhook')
    app.blueprint(v1_0)
