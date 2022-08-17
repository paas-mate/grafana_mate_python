# grafana_mate
## env
### AUTH_ENABLED
default value is false

> quickly deploy grafana.

## quick start

please configure optional environment variables.

`GRAFANA_HOST`: The host to connect to grafana host, default is `localhost`

`GRAFANA_PORT`: The port to connect to grafana port, default is `3000`

`PROM_HOST`: default is `localhost`

`ES_HOST`: The host to connect to elasticsearch host, default is `localhost`

`INFLUX1_HOST`: The host to connect to influx host, default is `localhost`

`LOKI_HOST`: The host to connect to loki host, default is `localhost`

`TEMPO_HOST`: The host to connect to tempo host, default is `localhost`

`JAEGER_HOST`: The host to connect to jaeger host, default is `localhost`

```bash
# pull image
docker pull ttbb/grafana:mate
# deploy
docker run -it -d --name grafana_mate --network=host -e JAEGER_HOST=10.0.0.10 -e LOKI_HOST=10.0.0.11 ttbb/grafana:mate
```