"""Web Routes."""

from masonite.routes import Get, Post, RouteGroup

ROUTES = [
    # Home
    Get("/", "WelcomeController@inertia").name("welcome"),
    Get("/login", "auth.LoginController@show").name("login"),
    Get("/logout", "auth.LoginController@logout").name("logout"),
    Post("/login", "auth.LoginController@store"),
    # Problems
    RouteGroup(
        [
            Get("/", "ProblemsController@show").name("list"),
            Get("/@id", "ProblemsController@single").name("single"),
            Get("/@id/details", "ProblemsController@single_details").name(
                "single-details"
            ),
            Post("/@id/light", "ProblemsController@toggle_light").name("light"),
        ],
        prefix="/problems",
        name="problems.",
    ),
    # Admin
    RouteGroup(
        [
            Get("/board", "admin.BoardSettingsController@show").name("board.settings"),
            Get("/settings", "admin.SettingsController@show").name("settings"),
            Get("/sync", "admin.SyncController@show").name("sync").middleware("auth"),
            Post("/sync", "admin.SyncController@sync"),
        ],
        middleware=("auth",),
        prefix="/admin",
        # namespace="admin",
        name="admin.",
    ),
    # Get("/register", "auth.RegisterController@show").name("register"),
    # Post("/register", "auth.RegisterController@store"),
    Get("/admin", "auth.HomeController@show").name("home"),
    # Get("/email/verify", "auth.ConfirmController@verify_show").name("verify"),
    # Get("/email/verify/@id:signed", "auth.ConfirmController@confirm_email"),
    # Get("/email/verify/@id:signed", "auth.ConfirmController@confirm_email"),
    # Get("/password", "auth.PasswordController@forget").name("forgot.password"),
    # Post("/password", "auth.PasswordController@send"),
    # Get("/password/@token/reset", "auth.PasswordController@reset").name(
    #     "password.reset"
    # ),
    # Post("/password/@token/reset", "auth.PasswordController@update"),
]

# from masonite.auth import Auth
# ROUTES += Auth.routes()
