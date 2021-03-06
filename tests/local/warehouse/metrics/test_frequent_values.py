#  Copyright 2020 Soda
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from sodasql.scan.metric import Metric
from sodasql.scan.scan_yml_parser import KEY_METRICS
from tests.common.sql_test_case import SqlTestCase


class TestFrequentValues(SqlTestCase):

    def test_scan_mins_maxs(self):
        self.sql_recreate_table(
            [f"name {self.dialect.data_type_integer}"],
            ["(1)",
             "(2)",
             "(2)",
             "(3)",
             "(3)",
             "(3)",
             "(null)"])

        scan_result = self.scan({
            KEY_METRICS: [
                Metric.FREQUENT_VALUES
            ]
        })

        self.assertEqual(scan_result.get(Metric.FREQUENT_VALUES, 'name'),
                         [{'frequency': 3, 'value': 3},
                          {'frequency': 2, 'value': 2},
                          {'frequency': 1, 'value': 1}])
