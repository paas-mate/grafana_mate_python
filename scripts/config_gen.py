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

import os
import sys

if len(sys.argv) == 1:
    GRAFANA_CONF_DIR = "../config/"
else:
    GRAFANA_CONF_DIR = sys.argv[1] + "/conf/"
GRAFANA_CONF = GRAFANA_CONF_DIR + "grafana.ini"

with open(GRAFANA_CONF, "a") as file:
    auth_enabled = os.getenv("AUTH_ENABLED")
    if auth_enabled is None:
        file.write("enabled = true\n")
        file.write("org_name = Main Org.\n")
        file.write("org_role = Admin\n")
        file.write("hide_version = false\n")
    else:
        file.write("enabled = false\n")
        file.write("org_name = Main Org.\n")
        file.write("org_role = Viewer\n")
        file.write("hide_version = false\n")
    smtp_enabled = os.getenv("GRAFANA_SMTP_ENABLED")
    if smtp_enabled is None:
        exit()
    file.write("\n")
    file.write("[smtp]\n")
    file.write("enabled = " + smtp_enabled)
    file.write("\n")
    if smtp_enabled == "false":
        exit()
    file.write("host = " + os.getenv("GRAFANA_SMTP_HOST"))
    file.write("\n")
    file.write("user = " + os.getenv("GRAFANA_SMTP_USER"))
    file.write("\n")
    file.write("password = " + os.getenv("GRAFANA_SMTP_PASSWORD"))
    file.write("\n")
    file.write("skip_verify = " + os.getenv("GRAFANA_SMTP_SKIP_VERIFY"))
    file.write("\n")
    file.write("from_address = " + os.getenv("GRAFANA_SMTP_FROM_ADDRESS"))
    file.write("\n")
    file.write("from_name = " + os.getenv("GRAFANA_SMTP_FROM_NAME"))
    file.write("\n")
