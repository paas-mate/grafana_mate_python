#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

import json
from urllib import request

from app.const.constant import Const
from app.service.grafana_req_util import GrafanaReqUtil


class DataSourceService:
    def init_datasource(self):
        self.init_prometheus()
        self.init_elasticsearch()
        self.init_influxdb()
        self.init_loki()
        self.init_tempo()
        self.init_jaeger()

    @staticmethod
    def init_prometheus():
        print("begin to init prometheus")
        dumps = json.dumps(
            {"name": "Prometheus", "type": "prometheus", "url": "http://" + Const.prom_host + ":9090",
             "access": "proxy"})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(GrafanaReqUtil.new_datasource_post_req(), body)
        print(f.status)

    @staticmethod
    def init_elasticsearch():
        print("begin to init elasticsearch")
        dumps = json.dumps(
            {"name": "Elasticsearch", "type": "elasticsearch", "url": "http://" + Const.es_host + ":9200",
             "access": "proxy"})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(GrafanaReqUtil.new_datasource_post_req(), body)
        print(f.status)

    @staticmethod
    def init_influxdb():
        print("begin to init influx")
        dumps = json.dumps(
            {"name": "InfluxDB", "type": "influxdb", "url": "http://" + Const.influx1_host + ":8086",
             "access": "proxy", "database": "_internal"})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(GrafanaReqUtil.new_datasource_post_req(), body)
        print(f.status)

    @staticmethod
    def init_loki():
        print("begin to init loki")
        dumps = json.dumps(
            {"name": "Loki", "type": "loki", "url": "http://" + Const.loki_host + ":3100",
             "access": "proxy"})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(GrafanaReqUtil.new_datasource_post_req(), body)
        print(f.status)

    @staticmethod
    def init_tempo():
        print("begin to init tempo")
        dumps = json.dumps(
            {"name": "Tempo", "type": "tempo", "url": "http://" + Const.tempo_host + ":3200",
             "access": "proxy"})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(GrafanaReqUtil.new_datasource_post_req(), body)
        print(f.status)

    @staticmethod
    def init_jaeger():
        print("begin to init jaeger")
        dumps = json.dumps(
            {"name": "Jaeger", "type": "jaeger", "url": "http://" + Const.jaeger_host + ":16686",
            "access": "proxy"})
        body = dumps.encode(encoding='utf-8')
        f = request.urlopen(GrafanaReqUtil.new_datasource_post_req(), body)
        print(f.status)
