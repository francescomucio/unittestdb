from os import getenv

import sqlalchemy as sa


class Engine:
    @staticmethod
    def _create_engine():
        host = getenv('REDSHIFT_HOST')
        port = getenv('REDSHIFT_PORT')
        database = getenv('REDSHIFT_DATABASE')
        username = getenv('REDSHIFT_USERNAME')
        password = getenv('REDSHIFT_PW')
        return sa.create_engine(f'redshift+psycopg2://{username}:{password}@{host}:{port}/{database}',
                                connect_args={'sslmode': 'verify-ca'})

    @staticmethod
    def run_query(query):
        engine = Engine._create_engine()
        return engine.execute(query).fetchall()
