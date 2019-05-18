"""Add DSCR bail event model

Revision ID: bf65425d1227
Revises: 5f3daa92e736
Create Date: 2019-05-17 20:40:42.215862

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf65425d1227'
down_revision = '5f3daa92e736'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dscr_bail_events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_name', sa.String(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('date_str', sa.String(), nullable=True),
    sa.Column('bail_amount', sa.Numeric(), nullable=True),
    sa.Column('code', sa.String(), nullable=True),
    sa.Column('percentage_required', sa.Numeric(), nullable=True),
    sa.Column('type_of_bond', sa.String(), nullable=True),
    sa.Column('judge_id', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['dscr.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dscr_bail_events_case_number'), 'dscr_bail_events', ['case_number'], unique=False)
    op.execute("""
INSERT INTO
    dscr_bail_events (
        case_number,
        event_name,
        date_str,
        date,
        bail_amount,
        code,
        percentage_required,
        type_of_bond,
        judge_id)
SELECT
    case_number,
    event_name,
    bail[1],
    TO_DATE(bail[1], 'YYMMDD'),
    CAST(bail[2] AS NUMERIC),
    TRIM(bail[3]),
    CAST(bail[4] AS NUMERIC),
    TRIM(bail[5]),
    TRIM(bail[6])
FROM (
    SELECT
        case_number,
        event_name,
        regexp_split_to_array(comment, ';') AS bail
    FROM
        dscr_events
    WHERE
        event_name = 'BALR'
        OR event_name = 'BSET'
        OR event_name = 'INIT') foo
    """)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_dscr_bail_events_case_number'), table_name='dscr_bail_events')
    op.drop_table('dscr_bail_events')
    # ### end Alembic commands ###
