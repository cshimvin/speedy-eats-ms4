import os
os.environ["SECRET_KEY"] = "app secret key"
os.environ["STRIPE_PUBLIC_KEY"] = "public key generated by Stripe"
os.environ["STRIPE_SECRET_KEY"] = "secret key generated by Stripe"
os.environ["STRIPE_WH_SECRET"] = "webhook secret key generated by Stripe"
os.environ["DEVELOPMENT"] = "True"
os.environ.setdefault("DATABASE_URL"] = 'URL of Postgres database'