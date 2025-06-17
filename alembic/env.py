# alembic/env.py

from logging.config import fileConfig
import os
import sys
from alembic import context
from sqlalchemy import engine_from_config, pool

# ✅ Add project root to sys.path for imports to work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Load .env file early
from dotenv import load_dotenv
load_dotenv()

# ✅ Import SQLAlchemy Base and models
from app.database.session import Base
from app.models import user  # Make sure all models are imported

# Alembic Config object
config = context.config

# ✅ FIX: Use correct env var key
database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise ValueError("❌ DATABASE_URL is not set in the environment")

config.set_main_option("sqlalchemy.url", database_url)

# ✅ Setup logging
if config.config_file_name:
    fileConfig(config.config_file_name)

# ✅ Metadata used for autogenerate
target_metadata = Base.metadata

# --- Offline migration ---
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

# --- Online migration ---
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

# Entry point
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
