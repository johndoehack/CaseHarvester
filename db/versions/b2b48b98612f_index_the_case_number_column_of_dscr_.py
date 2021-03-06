"""index the case_number column of dscr,dsk8,dscivil for better performance

Revision ID: b2b48b98612f
Revises: cff8b8f5d1fe
Create Date: 2018-05-11 14:35:50.472661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2b48b98612f'
down_revision = 'cff8b8f5d1fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('dscivil_complaints_case_number_fkey', 'dscivil_complaints')
    op.drop_constraint('dscivil_events_case_number_fkey', 'dscivil_events')
    op.drop_constraint('dscivil_trials_case_number_fkey', 'dscivil_trials')
    op.drop_constraint('dscivil_hearings_case_number_fkey', 'dscivil_hearings')
    op.drop_constraint('dscivil_judgments_case_number_fkey', 'dscivil_judgments')
    op.drop_constraint('dscivil_related_persons_case_number_fkey', 'dscivil_related_persons')

    op.create_index(op.f('ix_dscivil_case_number'), 'dscivil', ['case_number'], unique=True)
    op.drop_constraint('dscivil_case_number_key', 'dscivil', type_='unique')

    op.create_foreign_key(None, 'dscivil_complaints', 'dscivil', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dscivil_events', 'dscivil', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dscivil_trials', 'dscivil', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dscivil_hearings', 'dscivil', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dscivil_judgments', 'dscivil', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dscivil_related_persons', 'dscivil', ['case_number'], ['case_number'], ondelete='CASCADE')

    op.drop_constraint('dscr_charges_case_number_fkey', 'dscr_charges')
    op.drop_constraint('dscr_defendant_aliases_case_number_fkey', 'dscr_defendant_aliases')
    op.drop_constraint('dscr_defendants_case_number_fkey', 'dscr_defendants')
    op.drop_constraint('dscr_events_case_number_fkey', 'dscr_events')
    op.drop_constraint('dscr_related_persons_case_number_fkey', 'dscr_related_persons')
    op.drop_constraint('dscr_trials_case_number_fkey', 'dscr_trials')

    op.create_index(op.f('ix_dscr_case_number'), 'dscr', ['case_number'], unique=True)
    op.drop_constraint('dscr_case_number_key', 'dscr', type_='unique')

    op.create_foreign_key(None, 'dscr_charges', 'dscr', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dscr_defendant_aliases', 'dscr', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dscr_defendants', 'dscr', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dscr_events', 'dscr', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dscr_related_persons', 'dscr', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dscr_trials', 'dscr', ['case_number'], ['case_number'], ondelete='CASCADE')

    op.drop_constraint('dsk8_bail_and_bond_case_number_fkey', 'dsk8_bail_and_bond')
    op.drop_constraint('dsk8_charges_case_number_fkey', 'dsk8_charges')
    op.drop_constraint('dsk8_defendant_aliases_case_number_fkey', 'dsk8_defendant_aliases')
    op.drop_constraint('dsk8_defendants_case_number_fkey', 'dsk8_defendants')
    op.drop_constraint('dsk8_events_case_number_fkey', 'dsk8_events')
    op.drop_constraint('dsk8_related_persons_case_number_fkey', 'dsk8_related_persons')
    op.drop_constraint('dsk8_trials_case_number_fkey', 'dsk8_trials')
    op.drop_constraint('dsk8_bondsman_case_number_fkey', 'dsk8_bondsman')

    op.create_index(op.f('ix_dsk8_case_number'), 'dsk8', ['case_number'], unique=True)
    op.drop_constraint('dsk8_case_number_key', 'dsk8', type_='unique')

    op.create_foreign_key(None, 'dsk8_bail_and_bond', 'dsk8', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dsk8_charges', 'dsk8', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dsk8_defendant_aliases', 'dsk8', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dsk8_defendants', 'dsk8', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dsk8_events', 'dsk8', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dsk8_related_persons', 'dsk8', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dsk8_trials', 'dsk8', ['case_number'], ['case_number'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dsk8_bondsman', 'dsk8', ['case_number'], ['case_number'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('dsk8_case_number_key', 'dsk8', ['case_number'])
    op.drop_index(op.f('ix_dsk8_case_number'), table_name='dsk8')
    op.create_unique_constraint('dscr_case_number_key', 'dscr', ['case_number'])
    op.drop_index(op.f('ix_dscr_case_number'), table_name='dscr')
    op.create_unique_constraint('dscivil_case_number_key', 'dscivil', ['case_number'])
    op.drop_index(op.f('ix_dscivil_case_number'), table_name='dscivil')
    # ### end Alembic commands ###
