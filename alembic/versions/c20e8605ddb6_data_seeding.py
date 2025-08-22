"""data_seeding

Revision ID: c20e8605ddb6
Revises: ed93a1c4f111
Create Date: 2025-08-22 15:34:58.472229

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "c20e8605ddb6"
down_revision: Union[str, Sequence[str], None] = "ed93a1c4f111"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    text = """
    INSERT INTO public.permissions (created_at, updated_at, created_by, modified_by, "action", resource)  VALUES ('2025-08-22 15:29:33.219391+00', '2025-08-22 15:29:33.219396+00', NULL, NULL, 'create', '/admin/users');
    INSERT INTO public.permissions (created_at, updated_at, created_by, modified_by, "action", resource) VALUES ('2025-08-22 15:29:33.219397+00', '2025-08-22 15:29:33.219397+00', NULL, NULL, 'update', '/admin/users');
    INSERT INTO public.permissions (created_at, updated_at, created_by, modified_by, "action", resource) VALUES ('2025-08-22 15:29:33.219398+00', '2025-08-22 15:29:33.219398+00', NULL, NULL, 'delete', '/admin/users');
    INSERT INTO public.permissions (created_at, updated_at, created_by, modified_by, "action", resource) VALUES ('2025-08-22 15:29:33.219399+00', '2025-08-22 15:29:33.219399+00', NULL, NULL, 'read', '/admin/users');
    INSERT INTO public.permissions (created_at, updated_at, created_by, modified_by, "action", resource) VALUES ('2025-08-22 15:29:33.2194+00', '2025-08-22 15:29:33.2194+00', NULL, NULL,  'create', '/admin/roles');
    INSERT INTO public.permissions (created_at, updated_at, created_by, modified_by, "action", resource) VALUES ('2025-08-22 15:29:33.219401+00', '2025-08-22 15:29:33.219401+00', NULL, NULL,  'update', '/admin/roles');
    INSERT INTO public.permissions (created_at, updated_at, created_by, modified_by, "action", resource) VALUES ('2025-08-22 15:29:33.219402+00', '2025-08-22 15:29:33.219402+00', NULL, NULL,  'delete', '/admin/roles');
    INSERT INTO public.permissions (created_at, updated_at, created_by, modified_by, "action", resource) VALUES ('2025-08-22 15:29:33.219402+00', '2025-08-22 15:29:33.219403+00', NULL, NULL,  'read', '/admin/roles');
    INSERT INTO public.permissions (created_at, updated_at, created_by, modified_by, "action", resource) VALUES ('2025-08-22 15:29:33.219403+00', '2025-08-22 15:29:33.219404+00', NULL, NULL,  'create', '/catalogs/products');
    INSERT INTO public.permissions (created_at, updated_at, created_by, modified_by, "action", resource) VALUES ('2025-08-22 15:29:33.219404+00', '2025-08-22 15:29:33.219405+00', NULL, NULL,  'update', '/catalogs/products');
    INSERT INTO public.permissions (created_at, updated_at, created_by, modified_by, "action", resource) VALUES ('2025-08-22 15:29:33.219405+00', '2025-08-22 15:29:33.219405+00', NULL, NULL,  'delete', '/catalogs/products');
    INSERT INTO public.permissions (created_at, updated_at, created_by, modified_by, "action", resource) VALUES ('2025-08-22 15:29:33.219406+00', '2025-08-22 15:29:33.219406+00', NULL, NULL, 'read', '/catalogs/products');

    INSERT INTO public.roles (created_at, updated_at, created_by, modified_by, "name") VALUES ('2025-08-22 15:29:33.230873+00', '2025-08-22 15:29:33.230876+00', NULL, NULL,  'admin');
    INSERT INTO public.roles (created_at, updated_at, created_by, modified_by, "name") VALUES ('2025-08-22 15:29:33.230877+00', '2025-08-22 15:29:33.230878+00', NULL, NULL, 'anonymous');

    INSERT INTO public.role_permissions VALUES ('2025-08-22 15:29:33.238026+00', '2025-08-22 15:29:33.238029+00', NULL, NULL, 1, 9);
    INSERT INTO public.role_permissions VALUES ('2025-08-22 15:29:33.23803+00', '2025-08-22 15:29:33.23803+00', NULL, NULL, 1, 2);
    INSERT INTO public.role_permissions VALUES ('2025-08-22 15:29:33.238031+00', '2025-08-22 15:29:33.238031+00', NULL, NULL, 1, 4);
    INSERT INTO public.role_permissions VALUES ('2025-08-22 15:29:33.238032+00', '2025-08-22 15:29:33.238032+00', NULL, NULL, 1, 11);
    INSERT INTO public.role_permissions VALUES ('2025-08-22 15:29:33.238033+00', '2025-08-22 15:29:33.238033+00', NULL, NULL, 1, 6);
    INSERT INTO public.role_permissions VALUES ('2025-08-22 15:29:33.238034+00', '2025-08-22 15:29:33.238034+00', NULL, NULL, 1, 8);
    INSERT INTO public.role_permissions VALUES ('2025-08-22 15:29:33.238035+00', '2025-08-22 15:29:33.238035+00', NULL, NULL, 1, 1);
    INSERT INTO public.role_permissions VALUES ('2025-08-22 15:29:33.238036+00', '2025-08-22 15:29:33.238036+00', NULL, NULL, 1, 10);
    INSERT INTO public.role_permissions VALUES ('2025-08-22 15:29:33.238037+00', '2025-08-22 15:29:33.238037+00', NULL, NULL, 1, 3);
    INSERT INTO public.role_permissions VALUES ('2025-08-22 15:29:33.238038+00', '2025-08-22 15:29:33.238038+00', NULL, NULL, 1, 12);
    INSERT INTO public.role_permissions VALUES ('2025-08-22 15:29:33.238038+00', '2025-08-22 15:29:33.238039+00', NULL, NULL, 2, 12);
    INSERT INTO public.role_permissions VALUES ('2025-08-22 15:29:33.238039+00', '2025-08-22 15:29:33.23804+00', NULL, NULL, 1, 5);
    INSERT INTO public.role_permissions VALUES ('2025-08-22 15:29:33.23804+00', '2025-08-22 15:29:33.238041+00', NULL, NULL, 1, 7);

    INSERT INTO public.users (created_at, updated_at, created_by, modified_by, username, fullname, email, hashed_password, is_active) VALUES ('2025-08-22 15:29:33.757438+00', '2025-08-22 15:29:33.757441+00', NULL, NULL, 'admin', 'Full Name Admin', 'admin@example.com', '$2b$12$6VfSX3GLFRpZgcLGdSOKkOAmt/oIoKs1UvUAGrDI6RRqatZoKd2PS', true);
    INSERT INTO public.users (created_at, updated_at, created_by, modified_by, username, fullname, email, hashed_password, is_active) VALUES ('2025-08-22 15:29:33.757442+00', '2025-08-22 15:29:33.757443+00', NULL, NULL,'anonymous', 'Full Name Anonymous', 'anonymous@example.com', '$2b$12$dDWH7vBIHVrVoTTmaYPBiu2YVZwNg.yWtyXFs958N3wDHwytY8UFu', true);

    INSERT INTO public.user_roles VALUES ('2025-08-22 15:29:33.767933+00', '2025-08-22 15:29:33.767936+00', NULL, NULL, 1, 1);
    INSERT INTO public.user_roles VALUES ('2025-08-22 15:29:33.767937+00', '2025-08-22 15:29:33.767937+00', NULL, NULL, 2, 2);

    """
    op.execute(text)


def downgrade() -> None:
    """Downgrade schema."""
    pass
