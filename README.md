### Prometheus Histogram Metrics - Demo

* Histogram metric type is usually used to measure request durations or response sizes

* This repo contains a docker compose file that will
  - spin up a simple python app
    + that has `/timer` endpoint that will randomly take anytime between 0-0.9 seconds
    + exposes prometheus metrics under `/metrics`
    + `/timer` endpoint exposes a histogram metric type called `request_time`
  - prometheus container
    + that will scrape metrics of the above app
  - grafana container
    + that plots the following using the histogram metrics
      - count of total requests in the selected time interval
      - p95 of the request duration of `/timer` endpoint in the selected time interval


