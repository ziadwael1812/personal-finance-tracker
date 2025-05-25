# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.user import User  # noqa
from app.models.transaction import Transaction  # noqa
from app.models.budget import Budget  # noqa
from app.models.goal import Goal  # noqa 