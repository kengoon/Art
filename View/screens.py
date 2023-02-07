# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController
from Model.signup_screen import SignupScreenModel
from Controller.signup_screen import SignupScreenController
from Model.home_screen import HomeScreenModel
from Controller.home_screen import HomeScreenController
from Model.splash_screen import SplashScreenModel
from Controller.splash_screen import SplashScreenController
from Model.profile_screen import ProfileScreenModel
from Controller.profile_screen import ProfileScreenController
from Model.art_screen import ArtScreenModel
from Controller.art_screen import ArtScreenController
from Model.payment_screen import PaymentScreenModel
from Controller.payment_screen import PaymentScreenController
from Model.collection_screen import CollectionScreenModel
from Controller.collection_screen import CollectionScreenController

screens = {
    'home screen': {
        'model': HomeScreenModel,
        'controller': HomeScreenController,
        'kv': 'View/HomeScreen/home_screen.kv'
    },
    'collection screen': {
        'model': CollectionScreenModel,
        'controller': CollectionScreenController,
        'kv': 'View/CollectionScreen/collection_screen.kv'
    },
    'login screen': {
        'model': LoginScreenModel,
        'controller': LoginScreenController,
        'kv': 'View/LoginScreen/login_screen.kv'
    },
    'splash screen': {
        'model': SplashScreenModel,
        'controller': SplashScreenController,
        'kv': 'View/SplashScreen/splash_screen.kv'
    },
    'profile screen': {
        'model': ProfileScreenModel,
        'controller': ProfileScreenController,
        'kv': 'View/ProfileScreen/profile_screen.kv'
    },
    'art screen': {
        'model': ArtScreenModel,
        'controller': ArtScreenController,
        'kv': 'View/ArtScreen/art_screen.kv'
    },
    'signup screen': {
        'model': SignupScreenModel,
        'controller': SignupScreenController,
        'kv': 'View/SignupScreen/signup_screen.kv'
    },
    'payment screen': {
        'model': PaymentScreenModel,
        'controller': PaymentScreenController,
        'kv': 'View/PaymentScreen/payment_screen.kv'
    },
}