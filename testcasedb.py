import unittest

from .engine import Engine


class TestCaseDB(unittest.TestCase):

    def assertNoRows(self, query, msg=None, output_columns=None):

        res = Engine.run_query(query)

        details_msg = f'Expected 0 rows got {len(res)}'
        output = ""

        for column in output_columns:
            output = f'{output}\n{column}:\n'
            for row in res:
                if row[column]:
                    output = f'{output}   {column}: {row[column]}\n'

        self.assertEqual(len(res), 0, msg=f'{msg} - {details_msg}\n{output}')
