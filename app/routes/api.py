from app.controllers.prime_no import PrimeNoView
from app.controllers.login import LoginView


urlpatterns = [
    { 'suffix':'prime-no', 'view': PrimeNoView.as_view() },
    { 'suffix':'login', 'view': LoginView.as_view() },
]
